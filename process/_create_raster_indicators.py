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

    engine = create_engine(f"postgresql://{db_user}:{db_pwd}@{db_host}/{db}")
    gpkg_path = os.path.join(locale_maps,'gpkg')
    engine_sqlite = create_engine(f'sqlite:///{gpkg_path}/{study_region}.gpkg',module = sqlite3)
    sql = f'''SELECT geom FROM {buffered_study_region}'''
    clipping_boundary = gpd.GeoDataFrame.from_postgis(sql, engine, geom_col='geom' )   
    
    # retrieve subset of datasets which are relate to raster data
    df = df_datasets.query('type=="raster"').copy()
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
        dataset = '../{}'.format(df.loc[row,'data_file'])
        print(f'  - "{dataset}"')
        source_name = df.loc[row,'data_name']
        source = df.loc[row,'provider']
        description = df.loc[row,'alias']
        map_field = df.loc[row,'map_field']
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
        raster_offset = float(df.loc[row,'raster_offset'])
        raster_nodata = int(df.loc[row,'raster_nodata'])
        scale_factor = float(df.loc[row,'scale_factor'])
        raster_dtype = df.loc[row,'data_type'].split(":")[1]  
        map_name = f'{locale}_ind_{map_name_suffix}'
        potential_column_width = len(map_field)+1
        if potential_column_width < pd.get_option("display.max_colwidth"):
            pd.set_option("display.max_colwidth", potential_column_width)
            gpd.pd.set_option("display.max_colwidth", potential_column_width)   
        if engine.has_table(map_name_suffix):
            print(f"    - {map_name_suffix} already exists in database.")
            print("      Please drop this table if you wish it to be reprocessed.")
        else:
            if 'skip_tables' not in sys.argv:
                if '.tif' not in dataset:
                    sys.exit("This code is designed to run with Geotiff's with the extension. tif")
                if '.zip:' in dataset:
                    zip,tif = dataset.split(':')
                    zip = os.path.abspath(zip)
                    dataset = f'zip:///{zip}!/{tif}'
                else:
                    dataset = os.path.abspath(dataset)
                # clip and save raster
                with rasterio.open(dataset) as full_raster:
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
                              new_crs = f'EPSG:{srid}')   
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
                print(f'\t- postgresql::{db}/{map_name_suffix}')
                analysis_area.to_sql(map_name_suffix, engine_sqlite, if_exists='replace',index=True)
                path = os.path.join(locale_maps,'gpkg')
                print(f'\t- {path}/{study_region}.gpkg/{map_name_suffix}')
                path = os.path.join(locale_maps,'csv')
                analysis_area.to_csv(f'{path}/{study_region}_{map_name_suffix}.csv')
                print(f'\t- {path}/{study_region}_{map_name_suffix}.csv')
        
        # Create map
        if 'skip_maps' not in sys.argv:
            print('      Creating map...')
            attribution = '{} | {} | {} data: {}'.format(map_attribution,areas[area_layer]['attribution'],map_field,source)
            tables    = [buffered_study_region,study_region]
            fields    = ['Description','Description']
            data_fields = 'a."{}",'.format('","'.join(pop_data_fields_full))
            coalesce_na = '{}'.format(df.loc[row,'coalesce_na'])
            if coalesce_na in ['','nan']:
                sql = f'''
                    SELECT a.{linkage_id},
                           a.{area_layer},
                           {data_fields}
                           b.{map_name_suffix},
                           ST_Transform(a.geom, 4326) AS geom 
                    FROM {area_layer} a
                    LEFT JOIN {map_name_suffix} b 
                    USING ({linkage_id})
                    '''
            else:
                sql = f'''
                    SELECT a.{linkage_id},
                           a.{area_layer},
                           {data_fields}
                           COALESCE(b.{map_name_suffix},{coalesce_na}) AS "{map_name_suffix}",
                           ST_Transform(a.geom, 4326) AS geom 
                    FROM {area_layer} a
                    LEFT JOIN {map_name_suffix} b 
                    USING ({linkage_id})
                    '''
            map = gpd.GeoDataFrame.from_postgis(sql, engine, geom_col='geom')
            map.rename(columns = {map_name_suffix : map_field}, inplace=True)
            map.rename(columns = column_names, inplace=True)
            map.rename(columns = {'area_km\u00B2':'area (km\u00B2)'}, inplace=True)
            data_fields =[area_layer]+[f.replace('sqkm','km\u00B2').replace('area_km\u00B2','area (km\u00B2)') for f in pop_data_fields_full]+[map_field]    
            # get map centroid from study region
            xy = [float(map.centroid.y.mean()),float(map.centroid.x.mean())]    
            bounds = map.bounds.transpose().to_dict()[0]
            # initialise map
            m = folium.Map(location=xy, zoom_start=11, tiles=None,control_scale=True, prefer_canvas=True,attr=f'{attribution}')
            # Add in location names
            folium.TileLayer(tiles='http://tile.stamen.com/toner-labels/{z}/{x}/{y}.png',
                            name='Location labels', 
                            show =False,
                            overlay=True,
                            attr=(
                               f" {attribution} | "
                                "Map tiles: <a href=\"http://stamen.com/\">Stamen Design</a>, " 
                                "under <a href=\"http://creativecommons.org/licenses/by/3.0\">CC BY 3.0</a>, featuring " 
                                "data by <a href=\"https://wiki.osmfoundation.org/wiki/Licence/\">OpenStreetMap</a>, "
                                "under ODbL.")
                                 ).add_to(m)
            # Add in the actual basemap to be shown
            folium.TileLayer(tiles='http://tile.stamen.com/toner-background/{z}/{x}/{y}.png',
                            name='Basemap: Simple', 
                            show =False,
                            overlay=False,
                            attr=(
                               f" {attribution} | "
                                "Map tiles: <a href=\"http://stamen.com/\">Stamen Design</a>, " 
                                "under <a href=\"http://creativecommons.org/licenses/by/3.0\">CC BY 3.0</a>, featuring " 
                                "data by <a href=\"https://wiki.osmfoundation.org/wiki/Licence/\">OpenStreetMap</a>, "
                                "under ODbL.")
                                 ).add_to(m)
            # Add in alternate basemap
            folium.TileLayer(tiles='OpenStreetMap',
                            name='Basemap: OpenStreetMap', 
                            show =False,
                            overlay=False,
                            attr=(
                               f" {map_attribution} | "
                                "Map tiles: <a href=\"http://openstreetmap.org/\">© OpenStreetMap contributors</a>, " 
                                "under <a href=\"http://creativecommons.org/licenses/by/3.0\">CC BY 3.0</a>, featuring " 
                                "data by <a href=\"https://wiki.osmfoundation.org/wiki/Licence/\">OpenStreetMap</a>, "
                                "under ODbL.")
                                    ).add_to(m)
            # Add in satellite basemap
            folium.TileLayer(tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}' ,
                            name='Basemap: ESRI World Imagery (satellite)', 
                            show =True,
                            overlay=False,
                            attr=(
                               f" {map_attribution} | "
                                "Map tiles: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community', " 
                                "under <a href=\"http://creativecommons.org/licenses/by/3.0\">CC BY 3.0</a>, featuring " 
                                "data by <a href=\"https://wiki.osmfoundation.org/wiki/Licence/\">OpenStreetMap</a>, "
                                "under ODbL.")
                                    ).add_to(m)
            # We add empty tile set in order to force display of data attribution; Basemaps are not overlay layers, so they are easily switchable
            folium.TileLayer(tiles='Null tiles',
                            name='Basemap: off', 
                            show =False,
                            overlay=False,
                            attr=f" {attribution}"
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
                legend_title = description[0].upper()+description[1:]
            else:
                legend_title = description
            legend_name = f'{legend_title}, by {area_layer}'
            layer = folium.Choropleth(data=map,
                            geo_data =map.to_json(),
                            name = map_field,
                            columns =[linkage_id,map_field],
                            key_on=f"feature.properties.{linkage_id}",
                            fill_color='YlGn',
                            fill_opacity=0.7,
                            nan_fill_opacity=0.2,
                            line_opacity=0.2,
                            legend_name=legend_name,
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
            ## load up the clipped raster (assumed to be epsg4326)
            #with rasterio.open(raster_clipped) as src:
            #    boundary = src.bounds
            #    nodata = raster_nodata
            #    raster_layer = src.read(1)
            #    # raster_layer = raster_layer.astype(float)
            #    # raster_layer[raster_layer==raster_nodata] = np.nan
            #    # TECHNICALLY INVALID WORKAROUND FOR DISPLAY PURPOSES ONLY
            #    # ie. no data over water, display as though 'zero' so it does not show
            #    raster_layer[raster_layer==raster_nodata] = 0
            #    raster_layer = scale_factor*(raster_layer + raster_offset)
            ## colormap=lambda x: (0, x, 0, x),#R,G,B,alpha,
            #m.add_child(folium.raster_layers.ImageOverlay(raster_layer, 
            #                    name=source_name,
            #                    opacity=.7,
            #                    bounds=[[boundary[1],boundary[0]], 
            #                            [boundary[3], boundary[2]]],
            #                    colormap=plt.get_cmap('YlGn'), 
            #                    legend_name=source_name,
            #                    overlay=True,
            #                    show=False
            #                    )) 
            # Add layer control
            folium.LayerControl(collapsed=False).add_to(m)
            m.fit_bounds(m.get_bounds())
            m.get_root().html.add_child(folium.Element(map_style))
            # Modify map 
            html = m.get_root().render()
            ## Wrap legend text if too long 
            ## (67 chars seems to work well, conservatively)
            if len(legend_name) > 65:
                import textwrap
                legend_lines = textwrap.wrap(legend_name, 65)
                legend_length = len(legend_name)
                n_lines = len(legend_lines)
                legend_height = 25 + 15 * n_lines
                old = f'''.attr("class", "caption")
        .attr("y", 21)
        .text('{legend_name}');'''
                new = ".append('tspan')".join(['''.attr('class','caption')
        .attr("x", 0)
        .attr("y", {pos})
        .text('{x}')'''.format(x=x,pos=21+15*legend_lines.index(x)) for x in legend_lines])
                html = html.replace(old,new)
                html = html.replace('.attr("height", 40);',f'.attr("height", {legend_height});')
            # move legend to lower right corner
            html = html.replace('''legend = L.control({position: \'topright''',
                                '''legend = L.control({position: \'bottomright''')
            # save map
            # map_name = '{}_ind_{}'.format(locale,map_name_suffix)
            fid = open(f'{locale_maps}/html/{map_name}.html', 'wb')
            fid.write(html.encode('utf8'))
            fid.close()
            folium_to_image(os.path.join(locale_maps,'html'),
                            os.path.join(locale_maps,'png'),
                            map_name)
            print(f'\t- {locale_maps}/html/{map_name}.html')
            print(f'\t- {locale_maps}/png/{map_name}.png')
            print('')
    # output to completion log                  
    script_running_log(script, task, start, locale)
    engine.dispose()

if __name__ == '__main__':
    main()