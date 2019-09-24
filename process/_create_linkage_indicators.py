"""

Create linkage indicators
~~~~~~~~~~~~~~~~~~~~~~~~~

Script:  
    _create_linkage_indicators.py
Purpose: 
    Create indicators based on linkage with boundary data from specification in datasets section of configuration file
Authors: 
    Carl Higgs

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

from script_running_log import script_running_log

# Import custom variables for National Liveability indicator process
from _project_setup import *

def main():
    # simple timer for log file
    start = time.time()
    script = os.path.basename(sys.argv[0])
    task = 'Create indicators from linkage files'
    
    engine = create_engine(f"postgresql://{db_user}:{db_pwd}@{db_host}/{db}")
    
    engine_sqlite = create_engine((
                      'sqlite:///{path}/{output_name}.gpkg'
                      ).format(output_name = '{}'.format(study_region),
                               path = os.path.join(locale_maps,'gpkg')),
                               module = sqlite3)
                      
    # retrieve subset of datasets which are files to be joined based on linkage
    df = df_datasets[df_datasets.index.str.startswith('linkage:')]
    
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
        dataset = df.loc[row,'data_dir']
        print('  - "{}"'.format(dataset))
        sheet = df.loc[row,'excel_sheet']
        data_type = valid_type(df.loc[row,'data_type'])
        description = df.loc[row,'alias']
        heading = '{}: {}'.format(full_locale,df.loc[row,'map_heading'])
        map_name_suffix = df.loc[row,'table_out_name'].replace(' ','_',).replace('-','_')
        area_layer = df.loc[row,'linkage_layer']
        area_linkage_id = df.loc[row,'linkage_id']
        aggregation = df.loc[row,'aggregation_if_duplicates']
        linkage_id = df.loc[row,'linkage_id']
        point_overlay_xy = df.loc[row,'point_overlay_xy']
        display_id = area_layer
        map_field = df.loc[row,'map_field']
        density = df.loc[row,'density']
        potential_column_width = len(map_field) + len(aggregation) + 1
        if potential_column_width < pd.get_option("display.max_colwidth"):
            pd.set_option("display.max_colwidth", potential_column_width)
            gpd.pd.set_option("display.max_colwidth", potential_column_width)   
        map_name = f'{locale}_ind_{map_name_suffix}'
        print('\t{}'.format(map_name))
        if os.path.isfile(f'{locale_maps}/html/{map_name}.html'):
            print('\t - File appears to already have been processed (HTML output exists); skipping.')
        else:
            if not area_layer in areas:
               print("\t - Please check that the specified 'linkage_layer' corresponds to one of those set up in the Parameters sheet.")
               continue
            if not areas[area_layer]['id']==linkage_id:
               print("\t - Please check that the specified 'linkage_id' corresponds to that of the specified linkage layer.")
               continue
            if description=='':
                description = map_field
                df.loc[row,'Description'] = map_field
            source = df.loc[row,'provider']
            mapxls = pd.ExcelFile('../{}'.format(dataset))
            mdf = pd.read_excel(mapxls,sheet)
            mdf = mdf.set_index(linkage_id)
            mdf.index.name = area_linkage_id
            fill_na = '{}'.format(df.loc[row,'fill_na'])
            if fill_na not in ['','nan']:
                fill_na = fill_na.split(',')
                for field in fill_na:
                    mdf[field] = mdf[field].fillna(method = 'ffill') 
            if '{}'.format(point_overlay_xy) not in ['','nan']:
                # this means an attempt has been made to define point data locations
                point_overlay_xy = point_overlay_xy.split(',')
                point_overlay_name = df.loc[row,'point_overlay_name']
                point_overlay_hover_field = df.loc[row,'point_overlay_hover_field']
                point_overlay = gpd.GeoDataFrame(mdf, geometry=gpd.points_from_xy(mdf[point_overlay_xy[0]],mdf[point_overlay_xy[1]]))
            # aggregate data by ID using specified method, if specified.
            # Note that currently only 'sum' and 'average' have been programmed as options.
            aggregation_text = ''
            popup_agg_text = ''
            if aggregation =='count':
                mdf[map_field] = 1
                mdf = mdf.groupby(mdf.index)[map_field].sum().to_frame()
                aggregation_text = f" ({aggregation})"
            if aggregation =='sum':
                mdf = mdf.groupby(mdf.index)[map_field].sum().to_frame()
                aggregation_text = f" ({aggregation})"
            elif aggregation == 'average':
                mdf = mdf.groupby(mdf.index)[map_field].mean().to_frame()
                aggregation_text = f" ({aggregation})"
                map_field = f'average {map_field}'
            elif not '{}'.format(description)=='nan':
                print("Specified aggregation method has not been programmed as an option for this Excel file; no aggregation will be made. If duplicate IDs exists, results are likely inaccurate,")
            if population_linkage != {} and density not in ['','nan']:
                # some sort of density calculation has been requested and must be processed
                if density.startswith('population'):
                    if len(density.split('.'))== 1:
                        # default for population density is per 10,000 population
                        density_units = 10000.0
                    else:
                        density_units = float(density.split('.')[1])
                    sql = '''
                        SELECT a.{area}_id,
                               population
                        FROM {area} a
                        '''.format(area = area_layer,
                                   data_fields = 'a."{}",'.format('","'.join(pop_data_fields_full)),
                                   data = map_name_suffix,
                                   map_field = map_field,
                                   id = linkage_id)
                    area_data = pandas.read_sql(sql, engine, index_col=f'{area_layer}_id')
                    mdf = mdf.join(area_data)
                    mdf[map_field] = mdf[map_field]/(mdf['population']/density_units)
                    mdf.drop('population', axis=1, inplace=True)
                elif density.startswith('sqkm'):
                    if len(density.split('.'))==1:
                        # default for area density is per sqkm
                        density_units = 1.0
                    else:
                        density_units = float(density.split('.')[1])
                    sql = '''
                        SELECT a.{area}_id,
                               area_sqkm
                        FROM {area} a
                        '''.format(area = area_layer,
                                   data_fields = 'a."{}",'.format('","'.join(pop_data_fields_full)),
                                   data = map_name_suffix,
                                   map_field = map_field,
                                   id = linkage_id)
                    area_data = pandas.read_sql(sql, engine, index_col=f'{area_layer}_id')
                    mdf = mdf.join(area_data)
                    mdf[map_field] = mdf[map_field]/(mdf['area_sqkm']/density_units)
                    mdf.drop('area_sqkm', axis=1, inplace=True)
                else:
                    print(f'undefined density "{density}"; please check configuration for this indicator')
            # we create an alternate description field as it may be that the map_field variable is > 63 characters 
            # in which case it would be truncated.  So we use the map_name_suffix as the field name for the data, and populate 'description'
            # with the 
            # mdf['description'] = map_field
            # Send to SQL database
            # print(mdf.columns)
            mdf.columns = [map_name_suffix]
            # if len(mdf.columns) == 1:
                # mdf.columns = [map_name_suffix]
            # else:
                # print([map_name_suffix]+mdf.columns[1:])
                # mdf.columns = [map_name_suffix]+mdf.columns[1:]
            mdf.to_sql(map_name_suffix, engine, if_exists='replace', index=True)
            print(f'\t- postgresql::{db}/{map_name_suffix}')
            mdf.to_sql(map_name_suffix, engine_sqlite, if_exists='replace',index=True)
            print('\t- {path}/{output_name}.gpkg/{layer}'.format(output_name = '{}'.format(study_region),
                                                            path = os.path.join(locale_maps,'gpkg'),
                                                            layer = map_name_suffix))
            mdf.to_csv('{path}/{output_name}.csv'.format(output_name = '{}_{}'.format(study_region,
                                                                                      map_name_suffix),
                                                         path = os.path.join(locale_maps,'csv')))
            print('\t- {path}/{output_name}.csv'.format(output_name = '{}_{}'.format(study_region,
                                                                                      map_name_suffix),
                                                         path = os.path.join(locale_maps,'csv')))
            # df.loc[row,:].to_frame().transpose().to_sql('data_sources', engine, if_exists='replace',index=False)
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
            # initialise map
            m = folium.Map(location=xy, zoom_start=11, tiles=None,control_scale=True, prefer_canvas=True,attr='{}'.format(attribution))
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
                            show =True,
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
                                " {attribution} | "
                                "Map tiles: <a href=\"http://openstreetmap.org/\">© OpenStreetMap contributors</a>, " 
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
                legend_title = map_field[0].upper()+map_field[1:]
            else:
                legend_title = map_field
            layer = folium.Choropleth(data=map,
                            geo_data =map.to_json(),
                            name = map_field,
                            columns =[area_layer,map_field],
                            key_on=f"feature.properties.{area_layer}",
                            fill_color='YlGn',
                            fill_opacity=0.7,
                            nan_fill_opacity=0.2,
                            line_opacity=0.2,
                            legend_name=f'{legend_title}, by {area_layer}{aggregation_text}',
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
            if '{}'.format(point_overlay_xy) not in ['','nan']:
                point_layer = folium.features.GeoJson(data=point_overlay.to_json(), 
                                                      name=point_overlay_name, 
                                                      tooltip=f"feature.properties.{point_overlay_hover_field}"
                                                      ).add_to(m)
                folium.features.GeoJsonTooltip(fields=[c for c in point_overlay.columns if c is not 'geometry'],
                                               localize=True,
                                               labels=True, 
                                               sticky=True
                                               ).add_to(point_layer)  
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