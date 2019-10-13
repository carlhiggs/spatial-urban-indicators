"""

Create indicators from raster data sources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Script:  
    _create_raster_indicators.py
Purpose: 
    Create indicators from raster data sources based on aggregation to vector boundaries, from specification in datasets section of configuration file

"""

import time
import os
import pandas as pd
import numpy as np
import geopandas as gpd
from geoalchemy2 import Geometry, WKTElement
from sqlalchemy import create_engine, NVARCHAR, event
import folium
import re
import sqlite3
import rasterio
from rasterio.mask import mask
from rasterstats import zonal_stats
from folium import plugins
# import branca
import psycopg2
import json
import matplotlib.pyplot as plt

from script_running_log import script_running_log

# Import custom variables for National Liveability indicator process
from _project_setup import *

def main():
    # simple timer for log file
    start = time.time()
    script = os.path.basename(sys.argv[0])
    task = 'Create indicators from raster files'

    engine = create_engine("postgresql://{user}:{pwd}@{host}/{db}".format(user = db_user,
                                                                          pwd  = db_pwd,
                                                                          host = db_host,
                                                                          db   = db))

    engine_sqlite = create_engine((
                      'sqlite:///{path}/{output_name}.gpkg'
                      ).format(output_name = '{}'.format(study_region),
                               path = os.path.join(locale_maps,'gpkg')),
                               module = sqlite3)
    clipping_boundary = gpd.GeoDataFrame.from_postgis('''SELECT geom FROM {table}'''.format(table = buffered_study_region), engine, geom_col='geom' )   
                  
    # retrieve subset of datasets which are files to be joined based on linkage
    df = df_datasets[df_datasets.index.str.startswith('raster:')]

    # get key fields from the specified population dataset
    population = pandas.read_csv(population_linkage[analysis_scale]['data'],index_col=population_linkage[analysis_scale]['linkage']) 
    population_numeric = [c for c in population.columns if np.issubdtype(population[c].dtype, np.number)]
    pop_data_fields = population_map_fields.split(',')
    pop_data_fields_full = ['area_sqkm']
    pop_data_fields_to_map = []
    for f in pop_data_fields:
        pop_data_fields_full.append(f)
        if f in population_numeric:
            pop_data_fields_full.append(f'{f} per sqkm')
            pop_data_fields_to_map.append(f'{f} per sqkm')
    column_names = {}
    # format to display superscript 2 for square kilometres
    for f in pop_data_fields_full:
        column_names[f] = f.replace('sqkm','km\u00B2')

    for row in df.index:
        dataset = '../{}'.format(df.loc[row,'data_dir'])
        print(f'  - "{dataset}"')
        source_name = df.loc[row,'data_name']
        source = df.loc[row,'provider']
        map_field = df.loc[row,'map_field']
        heading = '{}: {}'.format(full_locale,df.loc[row,'map_heading'])
        map_name_suffix = df.loc[row,'table_out_name'].replace(' ','_',).replace('-','_')
        area_layer = df.loc[row,'linkage_layer']
        area_linkage_id = df.loc[row,'linkage_id']
        linkage_id      = df.loc[row,'linkage_id']
        # Must define a list of statistics in config file
        # options are:
        # ['count', 'min', 'max', 'mean', 'sum', 'std', 'median', 'majority', 'minority', 'unique', 'range', 'nodata', 'nan']
        # Note that 'std' refers to standard deviation (ie. indicates within area variation about the mean)
        raster_statistic = df.loc[row,'raster_statistic']
        raster_clipped  = f'{dataset}_clipped.tif'
        raster_projected  = f'{dataset}_projected.tif'
        raster_band = int(df.loc[row,'raster_band'])
        # raster_mult = int(df.loc[row,'raster_mult'])
        raster_offset = float(df.loc[row,'raster_offset'])
        raster_nodata = int(df.loc[row,'raster_nodata'])
        scale_factor = float(df.loc[row,'scale_factor'])
        # raster_range = [int(x) for x in df.loc[row,'raster_range'].split(',')]
        # if len(raster_range) == 2:
            # scale_factor = (1/raster_range[1]) * raster_mult
        # else:
            # scale_factor = 1
        raster_dtype = df.loc[row,'data_type'].split(":")[1]
        # potential_column_width = len(map_field)
        # if potential_column_width < pd.get_option("display.max_colwidth"):
            # pd.set_option("display.max_colwidth", potential_column_width)
            # gpd.pd.set_option("display.max_colwidth", potential_column_width)   
        map_name = f'{locale}_ind_{map_name_suffix}'
        potential_column_width = len(map_field)+1
        if potential_column_width < pd.get_option("display.max_colwidth"):
            pd.set_option("display.max_colwidth", potential_column_width)
            gpd.pd.set_option("display.max_colwidth", potential_column_width)   
        # clip and save raster
        with rasterio.open(os.path.abspath(dataset)) as full_raster:
            # set pop_vector to match crs of input raster
            # the above works as tested (raster is epsg 4326)
            # in theory, works if epsg is otherwise detectable in rasterio
            clipping_boundary.to_crs({'init':full_raster.crs['init']},inplace=True)
            coords = [json.loads(clipping_boundary.to_json())['features'][0]['geometry']]
            out_img, out_transform = mask(full_raster, coords, crop=True)
            out_meta = full_raster.meta.copy()
            out_meta.update({
                            "driver": "GTiff",
                            "height": out_img.shape[1],
                            "width":  out_img.shape[2],
                            "transform": out_transform,
                            "nodata": raster_nodata
                            }) 
        with rasterio.open(raster_clipped, "w", **out_meta) as dest:
            dest.write(out_img)    
        # reproject and save the re-projected clipped raster
        # (see config file for reprojection function)
        reproject_raster(inpath = raster_clipped, 
                      outpath = raster_projected, 
                      new_crs = 'EPSG:{}'.format(srid))   
        # Aggregate raster in each subdistrict according to datasource set up (e.g. sum or average)
        sql = '''SELECT "{}",geom FROM {}'''.format(areas[area_layer]['id'],areas[area_layer]['table'])
        analysis_area = gpd.GeoDataFrame.from_postgis(sql,engine, geom_col='geom', index_col=area_linkage_id)
        # create null field for population values
        stats = zonal_stats(analysis_area,
                             raster_projected,
                             band_num=raster_band,
                             no_data=raster_nodata,
                             stats=raster_statistic,
                             all_touched=True,
                             geojson_out=True)
        analysis_area[map_name_suffix] = np.nan    
        analysis_area[map_name_suffix] = analysis_area[map_name_suffix].astype(raster_dtype)
        for x in range(0,len(stats)):
            analysis_area.loc[int(stats[x]['id']),map_name_suffix]=scale_factor*stats[x]['properties'][raster_statistic]+raster_offset
        
        # output vector layers with new summary statistic
        analysis_area.drop(['geom'], axis=1, inplace=True)
        analysis_area.to_sql(map_name_suffix, engine, if_exists='replace', index=True)
        print('\t- postgresql::{}/{}'.format(db,map_name_suffix))
        analysis_area.to_sql(map_name_suffix, engine_sqlite, if_exists='replace',index=True)
        print('\t- {path}/{output_name}.gpkg/{layer}'.format(output_name = '{}'.format(study_region),
                                                        path = os.path.join(locale_maps,'gpkg'),
                                                        layer = map_name_suffix))
        analysis_area.to_csv('{path}/{output_name}.csv'.format(output_name = '{}_{}'.format(study_region,
                                                                                  map_name_suffix),
                                                     path = os.path.join(locale_maps,'csv')))
        print('\t- {path}/{output_name}.csv'.format(output_name = '{}_{}'.format(study_region,
                                                                                  map_name_suffix),
                                                     path = os.path.join(locale_maps,'csv')))
        # Create map
        attribution = '{} | {} | {} data: {}'.format(map_attribution,areas[area_layer]['attribution'],map_field,source)
        tables    = [buffered_study_region,study_region]
        fields    = ['Description','Description']
        coalesce_na = '{}'.format(df.loc[row,'coalesce_na'])
        if coalesce_na in ['','nan']:
            sql = '''
                SELECT a.{area},
                       {data_fields}
                       b.{data},
                       ST_Transform(a.geom, 4326) AS geom 
                FROM {area} a
                LEFT JOIN {data} b 
                USING ({id})
                '''.format(area = area_layer,
                           data_fields = 'a."{}",'.format('","'.join(pop_data_fields_full)),
                           data = map_name_suffix,
                           map_field = map_field,
                           id = linkage_id)
        else:
            sql = '''
                SELECT a.{area},
                       {data_fields}
                       COALESCE(b.{data},{coalesce_na}) AS "{data}",
                       ST_Transform(a.geom, 4326) AS geom 
                FROM {area} a
                LEFT JOIN {data} b 
                USING ({id})
                '''.format(area = area_layer,
                           data_fields = 'a."{}",'.format('","'.join(pop_data_fields_full)),
                           data = map_name_suffix,
                           map_field = map_field,
                           id = linkage_id,
                           coalesce_na = coalesce_na)
        map = gpd.GeoDataFrame.from_postgis(sql, engine, geom_col='geom')
        map.rename(columns = {map_name_suffix : map_field}, inplace=True)
        map.rename(columns = column_names, inplace=True)
        map.rename(columns = {'area_km\u00B2':'area (km\u00B2)'}, inplace=True)
        data_fields =[area_layer]+[f.replace('sqkm','km\u00B2').replace('area_km\u00B2','area (km\u00B2)') for f in pop_data_fields_full]+[map_field]    
        # get map centroid from study region
        xy = [float(map.centroid.y.mean()),float(map.centroid.x.mean())]    
        bounds = map.bounds.transpose().to_dict()[0]
        # initialise map
        m = folium.Map(location=xy, zoom_start=11, tiles=None,control_scale=True, prefer_canvas=True,attr='{}'.format(attribution))
        # Add in location names
        folium.TileLayer(tiles='http://tile.stamen.com/toner-labels/{z}/{x}/{y}.png',
                        name='Location labels', 
                        show =False,
                        overlay=True,
                        attr=((
                            " {} | "
                            "Map tiles: <a href=\"http://stamen.com/\">Stamen Design</a>, " 
                            "under <a href=\"http://creativecommons.org/licenses/by/3.0\">CC BY 3.0</a>, featuring " 
                            "data by <a href=\"https://wiki.osmfoundation.org/wiki/Licence/\">OpenStreetMap</a>, "
                            "under ODbL.").format(attribution))
                                ).add_to(m)
        # Add in the actual basemap to be shown
        folium.TileLayer(tiles='http://tile.stamen.com/toner-background/{z}/{x}/{y}.png',
                        name='Basemap: Simple', 
                        show =False,
                        overlay=False,
                        attr=((
                            " {} | "
                            "Map tiles: <a href=\"http://stamen.com/\">Stamen Design</a>, " 
                            "under <a href=\"http://creativecommons.org/licenses/by/3.0\">CC BY 3.0</a>, featuring " 
                            "data by <a href=\"https://wiki.osmfoundation.org/wiki/Licence/\">OpenStreetMap</a>, "
                            "under ODbL.").format(attribution))
                                ).add_to(m)
        # Add in alternate basemap
        folium.TileLayer(tiles='OpenStreetMap',
                        name='Basemap: OpenStreetMap', 
                        show =False,
                        overlay=False,
                        attr=((
                            " {} | "
                            "Map tiles: <a href=\"http://openstreetmap.org/\">© OpenStreetMap contributors</a>, " 
                            "under <a href=\"http://creativecommons.org/licenses/by/3.0\">CC BY 3.0</a>, featuring " 
                            "data by <a href=\"https://wiki.osmfoundation.org/wiki/Licence/\">OpenStreetMap</a>, "
                            "under ODbL.").format(map_attribution))
                                ).add_to(m)
        # Add in satellite basemap
        folium.TileLayer(tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}' ,
                        name='Basemap: ESRI World Imagery (satellite)', 
                        show =True,
                        overlay=False,
                        attr=((
                            " {} | "
                            "Map tiles: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community', " 
                            "under <a href=\"http://creativecommons.org/licenses/by/3.0\">CC BY 3.0</a>, featuring " 
                            "data by <a href=\"https://wiki.osmfoundation.org/wiki/Licence/\">OpenStreetMap</a>, "
                            "under ODbL.").format(map_attribution))
                                ).add_to(m)
        # We add empty tile set in order to force display of data attribution; Basemaps are not overlay layers, so they are easily switchable
        folium.TileLayer(tiles='Null tiles',
                        name='Basemap: off', 
                        show =False,
                        overlay=False,
                        attr=((
                            " {}"
                           ).format(attribution))
                                ).add_to(m)
        # Create choropleth map
        bins = 6
        # determine how to bin data (depending on skew, linear scale with 6 equal distance groups may not be appropriate)
        legend_bins = '{}'.format(df.loc[row,'coalesce_na'])
        if legend_bins in ['quartiles']:
            bins = list(map[map_field].quantile([0, 0.25, 0.5, 0.75, 1]))
        if legend_bins.startswith('equal'):
            legend_bins = legend_bins.split(':')
            if len(legend_bins) != 2:
                bins = 6
            else:
                bins = legend_bins[1]
        if legend_bins.startswith('custom'):
            legend_bins = legend_bins.split(':')
            if len(legend_bins) != 2:
                bins = 6
            else:
                legend_bins = legend_bins[1].split(',')
                bins = legend_bins
        if bins == 6:
            value_list = set(map[map_field].dropna().unique())
            if len(value_list) < 6:
                bins = len(value_list)
                if len(value_list) < 3:
                    bins = list(value_list)+[max(value_list)+1]+[max(value_list)+2]
        if len(map_field) > 1:
            # make first letter of map field upper case for legend
            legend_title = map_field[0].upper()+map_field[1:]
        else:
            legend_title = map_field
        layer = folium.Choropleth(data=map,
                        geo_data =map.to_json(),
                        name = map_field,
                        columns =[area_layer,map_field],
                        key_on="feature.properties.{}".format(area_layer),
                        fill_color='YlGn',
                        fill_opacity=0.7,
                        nan_fill_opacity=0.2,
                        line_opacity=0.2,
                        legend_name='{}, by {}'.format(legend_title,area_layer),
                        bins = bins,
                        smooth_factor = None,
                        reset=True,
                        overlay = True
                        ).add_to(m)
        folium.features.GeoJsonTooltip(fields=data_fields,
                                       localize=True,
                                       labels=True, 
                                       sticky=True
                                       ).add_to(layer.geojson)    
        # load up the clipped raster (assumed to be epsg4326)
        with rasterio.open(raster_clipped) as src:
            boundary = src.bounds
            nodata = raster_nodata
            raster_layer = src.read(1)
            # raster_layer = raster_layer.astype(float)
            # raster_layer[raster_layer==raster_nodata] = np.nan
            # TECHNICALLY INVALID WORKAROUND FOR DISPLAY PURPOSES ONLY
            # ie. no data over water, display as though 'zero' so it does not show
            raster_layer[raster_layer==raster_nodata] = 0
            raster_layer = scale_factor*(raster_layer + raster_offset)
        # colormap=lambda x: (0, x, 0, x),#R,G,B,alpha,
        m.add_child(folium.raster_layers.ImageOverlay(raster_layer, 
                            name=source_name,
                            opacity=.7,
                            bounds=[[boundary[1],boundary[0]], 
                                    [boundary[3], boundary[2]]],
                            colormap=plt.get_cmap('YlGn'), 
                            legend_name=source_name,
                            overlay=True,
                            show=False
                            )) 
        # Add layer control
        folium.LayerControl(collapsed=False).add_to(m)
        m.fit_bounds(m.get_bounds())
        m.get_root().html.add_child(folium.Element(map_style))
        # Modify map heading (above legend)
        html = m.get_root().render()
        color_map =  re.search(r"color_map_[a-zA-Z0-9_]*\b|$",html).group()
        old = '{}.svg = d3.select(".legend.leaflet-control").append("svg")'.format(color_map)
        new = '''
        {color_map}.title = d3.select(".legend.leaflet-control").append("div")
                .attr("style",'vertical-align: text-top;font-weight: bold;')
                .text("{heading}");
        {color_map}.svg = d3.select(".legend.leaflet-control").append("svg")
        '''.format(color_map=color_map,heading=heading)
        html = html.replace(old,new)
        # move legend to lower right corner
        html = html.replace('''legend = L.control({position: \'topright''',
                            '''legend = L.control({position: \'bottomright''')
        # save map
        # map_name = '{}_ind_{}'.format(locale,map_name_suffix)
        fid = open('{}/html/{}.html'.format(locale_maps,map_name), 'wb')
        fid.write(html.encode('utf8'))
        fid.close()
        folium_to_image(os.path.join(locale_maps,'html'),
                        os.path.join(locale_maps,'png'),
                        map_name)
        print('\t- {}/html/{}.html'.format(locale_maps,map_name))
        print('\t- {}/png/{}.png'.format(locale_maps,map_name))
        print('')
    # output to completion log                  
    script_running_log(script, task, start, locale)
    engine.dispose()

if __name__ == '__main__':
    main()