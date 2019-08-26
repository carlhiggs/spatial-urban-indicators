# Script:  01_study_region_setup.py
# Purpose: Python set up study region boundaries
# Author:  Carl Higgs
# Date:    2018 06 05

import time
import os
import pandas as pd
import numpy as np
import geopandas as gpd
from geoalchemy2 import Geometry, WKTElement
from sqlalchemy import create_engine
from shapely.geometry import Polygon, MultiPolygon
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

print("Import administrative boundaries for study region... "),

gdf = {}
if len(list(set([areas[area]['data'] for area in areas])))==1:
  for area in areas:
    if area==analysis_scale:
      area = analysis_scale
      # if aggregate_from_smallest and area != area_meta['areas_of_interest'][0]:
      if areas[area]['data'].endswith('zip'):
        # Open zipped file as geodataframe
        gdf[area] = gpd.read_file('zip://../{}'.format(areas[area]['data']))
      if '.gpkg:' in areas[area]['data']:
        gpkg = areas[area]['data'].split(':')
        gdf[area] = gpd.read_file('../{}'.format(gpkg[0]), layer=gpkg[1])
      else:
        # Open spatial file as geodataframe
        gdf[area] = gpd.read_file('../{}'.format(areas[area]['data']))
      # retain only known ids and geometry , and set index using analysis scale
      # FUTURE >>> consider adding optional retain fields
      if area_sqkm != '':
        gdf[area] = gdf[area][area_ids+[area_sqkm,'geometry']]
        gdf[area].rename(columns={area_sqkm: "area_sqkm"},inplace=True)
        gdf[area]['area_sqkm'] = gdf[area]['area_sqkm'].astype(float)
      else:
        gdf[area] = gdf[area][area_ids+['geometry']]
      for i in area_id_types:
        if i[1] == 'integer':
            t = np.int64
        else:
            t = str
        gdf[area][i[0]] = gdf[area].loc[:,i[0]].astype(t)
      gdf[area] = gdf[area].set_index(areas[area]['id'])
      if population_linkage != {}:
        if population_linkage[area]['data'].endswith('csv'):
          population = pd.read_csv(population_linkage[area]['data'],index_col=population_linkage[area]['linkage']) 
          gdf[area] = gdf[area].join(population)
        else:
          print("Population linkage has only been coded to work with CSV files for now.")
      # Transform to project projection
      gdf[area].to_crs(epsg=srid, inplace=True)
    else:
      # Aggregate other area scales
      # test = gdf[analysis_scale].dissolve(by=areas['district']['id'], aggfunc='sum')
      agg_functions = {}
      for a in [areas[area][x] for x in areas[area] if areas[area][x] in area_ids and  areas[area][x] != areas[area]['id']]:
        agg_functions[a] = 'first'
      if area_sqkm != '':
        agg_functions['area_sqkm'] = 'sum'
      if population_linkage != {}:
        for c in population.columns:
          agg_functions[c] = 'sum'
      gdf[area] = gdf[analysis_scale].dissolve(by=areas[area]['id'], aggfunc=agg_functions)
  # now finalise area output for PostGIS 
  # area density based measures
  for area in areas: 
    if area_sqkm == '':
        gdf[area]['area_sqkm'] = gdf[area]['geometry'].area/10**6
        if population_linkage != {}:
            # Calculate density measures for numeric population linkage fields")
            population_numeric = [c for c in population.columns if np.issubdtype(population[c].dtype, np.number)]
            for field in population_numeric:
                # print(" - {}".format(field))
                gdf[area]['{} per sqkm'.format(field)] = gdf[area][field]/gdf[area]['area_sqkm']
    if areas[area]['display_bracket'] != '':
        gdf[area][area] = gdf[area][areas[area]['display_main']]+' ('+gdf[area][areas[area]['display_bracket']]+')'
    else:
        gdf[area][area] = gdf[area][areas[area]['display_main']]
    # Create WKT geometry (postgis won't read shapely geometry)
    gdf[area]["geometry"] = [MultiPolygon([feature]) if type(feature) == Polygon else feature for feature in gdf[area]["geometry"]]
    gdf[area]['geom'] = gdf[area]['geometry'].apply(lambda x: WKTElement(x.wkt, srid=srid))
    # Drop original shapely geometry
    gdf[area].drop('geometry', 1, inplace=True)
    # Ensure all geometries are multipolygons (specifically - can't be mixed type; complicates things)
    # Copy to project Postgis database
    gdf[area].to_sql(areas[area]['table'], engine, if_exists='replace', index=True, dtype={'geom': Geometry('MULTIPOLYGON', srid=srid)})
    print('\t{} {}'.format(len(gdf[area]),areas[area]['name']))

print("\nCreate analytical boundaries...")
print("\tCreate study region boundary... ")
engine.execute('''
DROP TABLE IF EXISTS {study_region}; 
CREATE TABLE {study_region} AS 
      SELECT {region_shape} AS "Study region",
            ST_Transform(geom,4326) AS geom_4326,
            geom 
        FROM {region_shape} 
       WHERE {where};
'''.format(study_region = study_region,
           region_shape = region_shape,
           where = region_where_clause))

print("\tCreate {} km buffered study region... ".format(study_buffer))
engine.execute('''
DROP TABLE IF EXISTS {buffered_study_region}; 
CREATE TABLE {buffered_study_region} AS 
      SELECT '{buffered_study_region_name}'::text AS "Study region buffer", 
             ST_Transform(ST_Buffer(geom,{buffer}),4326) AS geom_4326,
             ST_Buffer(geom,{buffer}) AS geom 
        FROM {study_region};
'''.format(study_region = study_region,
           buffered_study_region = buffered_study_region,
           buffered_study_region_name = '{} km'.format(study_buffer/1000,1),
           buffer = study_buffer))
          
# Prepare map
if not os.path.exists(locale_maps):
    os.makedirs(locale_maps)    
for dir in ['html','png','pdf','gpkg','csv','geojson']:
    path = os.path.join(locale_maps,dir)
    if not os.path.exists(path):
        os.makedirs(path)   

map_attribution = '{} | {}'.format(map_attribution,areas[area]['attribution'])
# if population_linkage != {}:
    # map_attribution = '{} | {}'.format(map_attribution,population_linkage[analysis_scale]['attribution'])


map_layers={}
tables    = [buffered_study_region,study_region]
fields    = ["Study region buffer","Study region"]
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
folium.TileLayer(tiles='Stamen Toner',
                        name='simple map', 
                        show =True,
                        overlay=True,
                        attr=((
                            " {} | "
                            "Map tiles: <a href=\"http://stamen.com/\">Stamen Design</a>, " 
                            "under <a href=\"http://creativecommons.org/licenses/by/3.0\">CC BY 3.0</a>, featuring " 
                            "data by <a href=\"https://wiki.osmfoundation.org/wiki/Licence/\">OpenStreetMap</a>, "
                            "under ODbL.").format(map_attribution))
                                ).add_to(m)
                        
# add layers (not true choropleth - for this it is just a convenient way to colour polygons)
map_groups = {}
for i in range(0,len(tables)):
    feature = folium.Choropleth(map_layers[tables[i]].to_json(),
                  name=names[i],
                  fill_color=colours['qualitative'][i],
                  fill_opacity=opacity[i],
                  nan_fill_opacity=0.2,
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
folium_to_image(os.path.join(locale_maps,'html'),os.path.join(locale_maps,'png'),map_name)

print("\nPlease inspect results using interactive map saved in project maps folder:".format(map_name))
print('\t- {}/html/{}.html'.format(locale_maps,map_name))
print('\t- {}/png/{}.png'.format(locale_maps,map_name))

print('')
# output to completion log					
script_running_log(script, task, start, locale)
engine.dispose()
