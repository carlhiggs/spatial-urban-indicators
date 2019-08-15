# Script:  _create_excel_indicators.py
# Purpose: Create indicators based on Excel data where accompanied by a 'map_this_dir_config.xlsx' file with appropriate entries
# Author:  Carl Higgs
# Date:    20190610

import time
import os
import pandas as pd
import numpy as np
import geopandas as gpd
from geoalchemy2 import Geometry, WKTElement
from sqlalchemy import create_engine, NVARCHAR
import folium
import re

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

# retrieve subset of datasets which are Excel or CSV files to be joined based on linkage
df = df_datasets[df_datasets.index.str.startswith('excel:') | df_datasets.index.str.startswith('csv:')]

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
    description = df.loc[row,'alias']
    heading = df.loc[row,'map_heading']
    map_name_suffix = df.loc[row,'table_out_name'].replace(' ','_',).replace('-','_')
    area_layer = df.loc[row,'linkage_layer']
    area_linkage_id = df.loc[row,'linkage_id']
    aggregation = df.loc[row,'aggregation_if_duplicates']
    linkage_id = df.loc[row,'linkage_id']
    display_id = area_layer
    map_field = df.loc[row,'map_field']
    if not area_layer in areas:
       print("Please check that the specified 'linkage_layer' corresponds to one of those set up in the Parameters sheet.")
       continue
    if not areas[area_layer]['id']==linkage_id:
       print("Please check that the specified 'linkage_id' corresponds to that of the specified linkage layer.")
       continue
    if description=='':
        description = map_field
        df.loc[row,'Description'] = map_field
    source = df.loc[row,'provider']
    mapxls = pd.ExcelFile('../{}'.format(dataset))
    mdf = pd.read_excel(mapxls,sheet)
    mdf = mdf.set_index(linkage_id)
    mdf.index.name = area_linkage_id
    # aggregate data by ID using specified method, if specified.
    # Note that currently only 'sum' and 'average' have been programmed as options.
    aggregation_text = ''
    if aggregation =='sum':
        mdf = mdf.groupby(mdf.index)[map_field].sum().to_frame()
        aggregation_text = " ({})".format(aggregation)
    elif aggregation == 'average':
        mdf = mdf.groupby(mdf.index)[map_field].mean().to_frame()
        aggregation_text = " ({})".format(aggregation)
    elif not '{}'.format(description)=='nan':
        print("Specified aggregation method has not been programmed as an option for this Excel file; no aggregation will be made if duplicate IDs are encountered.  If duplicate IDs exists, results are likely inaccurate,")
    # we create an alternate description field as it may be that the map_field variable is > 63 characters 
    # in which case it would be truncated.  So we use the map_name_suffix as the field name for the data, and populate 'description'
    # with the 
    mdf['description'] = map_field
    # Send to SQL database
    mdf.columns = [map_name_suffix,'description']
    mdf.to_sql(map_name_suffix, engine, if_exists='replace', index=True)
    # df.loc[row,:].to_frame().transpose().to_sql('data_sources', engine, if_exists='replace',index=False)
    # Create map
    attribution = '{} | {} | {}'.format(map_attribution,areas[area_layer]['attribution'],source)
    tables    = [buffered_study_region,study_region]
    fields    = ['Description','Description']
    sql = '''
        SELECT a.{area},
               {data_fields}
               b."{data}",
               b.description,
               ST_Transform(a.geom, 4326) AS geom 
        FROM {area} a
        LEFT JOIN {data} b 
        USING ({id})
        '''.format(area = area_layer,
                   data_fields = 'a."{}",'.format('","'.join(pop_data_fields_full)),
                   data = map_name_suffix,
                   id = linkage_id)
    map = gpd.GeoDataFrame.from_postgis(sql, engine, geom_col='geom')
    map.rename(columns = column_names, inplace=True)
    map.rename(columns = {'area_km\u00B2':'area (km\u00B2)'}, inplace=True)
    data_fields =[area_layer]+[f.replace('sqkm','km\u00B2').replace('area_km\u00B2','area (km\u00B2)') for f in pop_data_fields_full]+[map_name_suffix]    
    # get map centroid from study region
    xy = [float(map.centroid.y.mean()),float(map.centroid.x.mean())]    
    # initialise map
    m = folium.Map(location=xy, zoom_start=11, tiles=None,control_scale=True, prefer_canvas=True)
    m.add_tile_layer(tiles='Stamen Toner',
                    name='simple map', 
                    active=True,
                    attr=((
                        " {} | "
                        "Map tiles: <a href=\"http://stamen.com/\">Stamen Design</a>, " 
                        "under <a href=\"http://creativecommons.org/licenses/by/3.0\">CC BY 3.0</a>, featuring " 
                        "data by <a href=\"https://wiki.osmfoundation.org/wiki/Licence/\">OpenStreetMap</a>, "
                        "under ODbL.").format(attribution))
                            )
    # Create choropleth map
    layer = folium.Choropleth(data=map,
                    geo_data =map.to_json(),
                    name = map_field,
                    columns =[area_layer,map_name_suffix],
                    key_on="feature.properties.{}".format(area_layer),
                    fill_color='YlGn',
                    fill_opacity=0.7,
                    line_opacity=0.2,
                    legend_name='{}, by {}{}'.format(map_field.title(),area_layer,aggregation_text),
                    reset=True,
                    overlay = True
                    ).add_to(m)
    folium.features.GeoJsonTooltip(fields=data_fields,
                                        localize=True,
                                labels=True, 
                                sticky=True
                                ).add_to(layer.geojson)    
    # Add layer control
    # folium.LayerControl(collapsed=False).add_to(m)
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
    map_name = '{}_ind_{}'.format(locale,map_name_suffix)
    fid = open('{}/html/{}.html'.format(locale_maps,map_name), 'wb')
    fid.write(html.encode('utf8'))
    fid.close()
    folium_to_image(os.path.join(locale_maps,'html'),os.path.join(locale_maps,'png'),map_name,strip_elements=["leaflet-control-zoom"])
    print('\t- {}/html/{}.html'.format(locale_maps,map_name))
    print('\t- {}/png/{}.png'.format(locale_maps,map_name))
    print('')
# output to completion log					
script_running_log(script, task, start, locale)
engine.dispose()
