# Script:  01_study_region_setup.py
# Purpose: Python set up study region boundaries
# Author:  Carl Higgs
# Date:    2018 06 05

import time
import geopandas as gpd
from geoalchemy2 import Geometry, WKTElement
from sqlalchemy import create_engine
import folium
# import selenium.webdriver
from PIL import Image
from io import BytesIO

from script_running_log import script_running_log

# Import custom variables for National Liveability indicator process
from _project_setup import *

# simple timer for log file
start = time.time()
script = os.path.basename(sys.argv[0])
task = 'create study region boundary files in new geodatabase'

engine = create_engine("postgresql://{user}:{pwd}@{host}/{db}".format(user = db_user,
                                                                      pwd  = db_pwd,
                                                                      host = db_host,
                                                                      db   = db))

print("Import administrative boundaries for study region... "),
for area in areas:
  if areas[area]['data'].endswith('zip'):
    # Open zipped file as geodataframe
    gdf = gpd.read_file('zip://{}'.format(areas[area]['data']))
  else:
    # Open spatial file as geodataframe
    gdf = gpd.read_file(areas[area]['data'])
  # Restrict to relevant region based on filter value 
  # (this assumes filter value and field is common to 
  gdf = gdf[gdf[area_filter_field]==area_filter_value]
  
  # Set index
  gdf.set_index(areas[area]['id'],inplace=True)
  # Transform to project projection
  gdf.to_crs(epsg=srid, inplace=True)
  # Create WKT geometry (postgis won't read shapely geometry)
  gdf['geom'] = gdf['geometry'].apply(lambda x: WKTElement(x.wkt, srid=srid))
  # Drop original shapely geometry
  gdf.drop('geometry', 1, inplace=True)
  # Copy to project Postgis database
  gdf.to_sql(areas[area]['name_s'], engine, if_exists='replace', index=True, dtype={'geom': Geometry('POLYGON', srid=srid)})
  print('\t{} {}'.format(len(gdf),areas[area]['name_f'])), 

print("\nCreate analytical boundaries...")
print("\tCreate study region boundary... ")
engine.execute('''
DROP TABLE IF EXISTS {study_region}; 
CREATE TABLE {study_region} AS 
      SELECT '{study_region}'::text AS "Description",
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
      SELECT '{buffered_study_region_name}'::text AS "Description", 
             ST_Transform(ST_Buffer(geom,{buffer}),4326) AS geom_4326,
             ST_Buffer(geom,{buffer}) AS geom 
        FROM {study_region};
'''.format(study_region = study_region,
           buffered_study_region = buffered_study_region,
           buffered_study_region_name = buffered_study_region_name,
           buffer = study_buffer))

print("\tCalculate area in Hectares (Ha) and square kilometres (sqkm) and set up display formats for mapping for each area scale... ".format(study_buffer))           
for area in areas:
    engine.execute('''
    ALTER TABLE {area_analysis} 
    ADD COLUMN IF NOT EXISTS "{display_name}" text,
    ADD COLUMN IF NOT EXISTS area_ha double precision,
    ADD COLUMN IF NOT EXISTS area_sqkm double precision,
    ADD COLUMN IF NOT EXISTS geom_4326 geometry;
    UPDATE {area_analysis} 
    SET "{display_name}" = {display_sql},
        area_ha   = (ST_Area(geom)/10000.0)::double precision,
        area_sqkm = (ST_Area(geom)/1000000.0)::double precision,
        geom_4326 = ST_Transform(geom,4326);
    '''.format(area_analysis = areas[area]['name_s'],
               display_name  = areas[area]['name_f'],
               display_sql   = areas[area]['display'],
               buffered_study_region = buffered_study_region,
               buffer = study_buffer))
print("Done.")
          
# Prepare map
if not os.path.exists(locale_maps):
    os.makedirs(locale_maps)    
    
map_layers={}
tables    = [study_region,buffered_study_region,area_analysis]
fields    = ['Description','Description',analysis_field]
names     =  ['Study region',buffered_study_region_name,analysis_field]
opacity   =  [0.4,0,.7]
highlight =  [False,False,True]
for i in range(0,len(tables)):
    table = tables[i]
    field = fields[i]
    sql = '''SELECT "{}",geom_4326 geom FROM {}'''.format(field,table)
    map_layers[table] = gpd.GeoDataFrame.from_postgis(sql, engine, geom_col='geom' )

# get map centroid from study region
xy = [float(map_layers[study_region].centroid.y),float(map_layers[study_region].centroid.x)]    
# initialise map
m = folium.Map(location=xy, zoom_start=10, control_scale=True, prefer_canvas=True)
m.add_tile_layer(tiles='Stamen Toner',name='simple map', overlay=True,active=True)

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

# checkout https://nbviewer.jupyter.org/gist/jtbaker/57a37a14b90feeab7c67a687c398142c?flush_cache=true
# save map
map_name = '{}_01_study_region'.format(locale)
m.save('{}/{}.html'.format(locale_maps,map_name))
png = m._to_png()
im = Image.open(BytesIO(png))
im.save('{}/{}.png'.format(locale_maps,map_name))
print("\nPlease inspect results using interactive map saved in project maps folder: {}\n".format(map_name))
# output to completion log					
script_running_log(script, task, start, locale)
engine.dispose()
