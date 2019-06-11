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
from sqlalchemy import create_engine
import folium

from script_running_log import script_running_log

# Import custom variables for National Liveability indicator process
from _project_setup import *

# simple timer for log file
start = time.time()
script = os.path.basename(sys.argv[0])
task = 'create study region boundary'

engine = create_engine("postgresql://{user}:{pwd}@{host}/{db}".format(user = db_user,
                                                                      pwd  = db_pwd,
                                                                      host = db_host,
                                                                      db   = db))

# Prepare folders
if not os.path.exists(locale_maps):
    os.makedirs(locale_maps)    
for dir in ['html','png','pdf','gpkg']:
    path = os.path.join(locale_maps,dir)
    if not os.path.exists(path):
        os.makedirs(path)   

# Iterate over data directory
print("Check folders in data directory for 'map_this_dir_config.xlsx' files... "),
for root, dirs, files in os.walk('../data'):
    for file in files:
        if file == 'map_this_dir_config.xlsx':
            config = os.path.join(root,file)
            print()
            xls = pd.ExcelFile(config)
            df = pd.read_excel(xls, 'map_config')
            for row in df.index.values:
                dataset = df.loc[row,'File']
                sheet = df.loc[row,'Sheet']
                description = df.loc[row,'Description']
                map_name_suffix = df.loc[row,'map_name_suffix']
                area_layer = df.loc[row,'Area layer']
                area_linkage_id = df.loc[row,'Area linkage ID']
                linkage_id = df.loc[row,'Linkage ID']
                display_id = df.loc[row,'Display ID']
                map_field = df.loc[row,'Map field']
                source = df.loc[row,'Source']
                mapxls = pd.ExcelFile(os.path.join(root,dataset))
                mdf = pd.read_excel(mapxls, 'map_config')
                
                



map_attribution = '{} | {}'.format(map_attribution,areas[area]['attribution'])
        
map_layers={}
tables    = [buffered_study_region,study_region]
fields    = ['Description','Description']
names     =  [buffered_study_region_name,'Study region']
opacity   =  [0,0.4]
highlight =  [False,False]
for i in range(0,len(tables)):
    table = tables[i]
    field = fields[i]
    sql = '''SELECT "{}",geom_4326 geom FROM {}'''.format(field,table)
    map_layers[table] = gpd.GeoDataFrame.from_postgis(sql, engine, geom_col='geom' )

# get map centroid from study region
xy = [float(map_layers[study_region].centroid.y),float(map_layers[study_region].centroid.x)]    
# initialise map
m = folium.Map(location=xy, zoom_start=10, tiles=None,control_scale=True, prefer_canvas=True)
m.add_tile_layer(tiles='Stamen Toner',
                 name='simple map', 
                 active=True,
                 attr=((
                       " {} | "
                       "Map tiles: <a href=\"http://stamen.com/\">Stamen Design</a>, " 
                       "under <a href=\"http://creativecommons.org/licenses/by/3.0\">CC BY 3.0</a>, featuring " 
                       "data by <a href=\"https://wiki.osmfoundation.org/wiki/Licence/\">OpenStreetMap</a>, "
                       "under ODbL.").format(map_attribution))
                        )
                        
# add layers (not true choropleth - for this it is just a convenient way to colour polygons)
map_groups = {}
for i in range(0,len(tables)):
    feature = folium.Choropleth(map_layers[tables[i]].to_json(),
                  name=names[i],
                  fill_color=colours['qualitative'][i],
                  fill_opacity=opacity[i],
                  line_color=colours['qualitative'][i], 
                  highlight=highlight[i])
    feature.add_to(m)
    folium.features.GeoJsonTooltip(fields=[fields[i]],
                               labels=True, 
                               sticky=True
                              ).add_to(feature.geojson)

folium.LayerControl(collapsed=False).add_to(m)
# m.fit_bounds(m.get_bounds(),padding=(3, 3))
m.fit_bounds(m.get_bounds())
m.get_root().html.add_child(folium.Element(map_style))
# checkout https://nbviewer.jupyter.org/gist/jtbaker/57a37a14b90feeab7c67a687c398142c?flush_cache=true
# save map
map_name = '{}_01_study_region'.format(locale)
m.save('{}/html/{}.html'.format(locale_maps,map_name))
folium_to_png(os.path.join(locale_maps,'html'),os.path.join(locale_maps,'png'),map_name)

print("\nPlease inspect results using interactive map saved in project maps folder:".format(map_name))
print('\t- {}/html/{}.html'.format(locale_maps,map_name))
print('\t- {}/png/{}.png'.format(locale_maps,map_name))

print('')
# output to completion log					
script_running_log(script, task, start, locale)
engine.dispose()
