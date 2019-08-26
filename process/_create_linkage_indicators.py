# Script:  _create_linkage_indicators.py
# Purpose: Create indicators based on linkage with boundary data from specification in Datasets section of configuration file
# Author:  Carl Higgs
# Date:    20190812

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

# simple timer for log file
start = time.time()
script = os.path.basename(sys.argv[0])
task = 'Create indicators from linkage files'

engine = create_engine("postgresql://{user}:{pwd}@{host}/{db}".format(user = db_user,
                                                                      pwd  = db_pwd,
                                                                      host = db_host,
                                                                      db   = db))

engine_sqlite = create_engine((
                  'sqlite:///{path}/{output_name}.gpkg'
                  ).format(output_name = '{}'.format(study_region),
                           path = os.path.join(locale_maps,'gpkg')),
                           module = sqlite3)
                  
# engine_sqlite = sqlite3.connect((
                  # 'sqlite://{path}/{output_name}.gpkg'
                  # ).format(output_name = '{}'.format(study_region),
                           # path = os.path.join(folderPath,locale_maps,'gpkg')))
# engine_sqlite =  create_engine('sqlite:///../maps/bangkok_thailand_2018/gpkg/bangkok_thailand_2018.gpkg')


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
        pop_data_fields_full.append('{} per sqkm'.format(f))
        pop_data_fields_to_map.append('{} per sqkm'.format(f))
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
    display_id = area_layer
    map_field = df.loc[row,'map_field']
    map_name = '{}_ind_{}'.format(locale,map_name_suffix)
    print('\t{}'.format(map_name))
    if os.path.isfile('{}/html/{}.html'.format(locale_maps,map_name)):
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
        # aggregate data by ID using specified method, if specified.
        # Note that currently only 'sum' and 'average' have been programmed as options.
        aggregation_text = ''
        popup_agg_text = ''
        if aggregation =='sum':
            mdf = mdf.groupby(mdf.index)[map_field].sum().to_frame()
            aggregation_text = " ({})".format(aggregation)
        elif aggregation == 'average':
            mdf = mdf.groupby(mdf.index)[map_field].mean().to_frame()
            aggregation_text = " ({})".format(aggregation)
            map_field = 'average {}'.format(map_field)
        elif not '{}'.format(description)=='nan':
            print("Specified aggregation method has not been programmed as an option for this Excel file; no aggregation will be made if duplicate IDs are encountered.  If duplicate IDs exists, results are likely inaccurate,")
        # we create an alternate description field as it may be that the map_field variable is > 63 characters 
        # in which case it would be truncated.  So we use the map_name_suffix as the field name for the data, and populate 'description'
        # with the 
        # mdf['description'] = map_field
        # Send to SQL database
        mdf.columns = [map_name_suffix]
        mdf.to_sql(map_name_suffix, engine, if_exists='replace', index=True)
        print('\t- postgresql::{}/{}'.format(db,map_name_suffix))
        mdf.to_sql(map_name_suffix, engine_sqlite, if_exists='replace',index=True)
        print('\t- {path}/{output_name}.gpkg/{}'.format(output_name = '{}'.format(study_region),
                                                        path = os.path.join(locale_maps,'gpkg'),
                                                        map_name_suffix))
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
                       b.{data} AS "{map_field}",
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
                       COALESCE(b.{data},{coalesce_na}) AS "{map_field}",
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
        map.rename(columns = column_names, inplace=True)
        map.rename(columns = {'area_km\u00B2':'area (km\u00B2)'}, inplace=True)
        map[map_field] = map[map_field].astype(data_type)
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
                        show =True,
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
                        legend_name='{}, by {}{}'.format(legend_title,area_layer,aggregation_text),
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
        html = html.replace('''legend = L.control({position: \'topright''',                     '''legend = L.control({position: \'bottomright''')
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
