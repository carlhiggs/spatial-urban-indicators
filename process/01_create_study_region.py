# Script:  01_study_region_setup.py
# Purpose: Python set up study region boundaries
# Author:  Carl Higgs
# Date:    2018 06 05

import time
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
  print('\t{} {} imported'.format(len(gdf),areas[area]['name_f'])), 

print("\nCreate analytical boundaries...")
print("\tCreate study region boundary... ")
engine.execute('''
DROP TABLE IF EXISTS {study_region}; 
CREATE TABLE {study_region} AS SELECT '{study_region}'::text,geom FROM {region_shape} where {where};
'''.format(study_region = study_region,
           region_shape = region_shape,
           where = region_where_clause))

print("\tCreate {} km buffered study region... ".format(study_buffer))
engine.execute('''
DROP TABLE IF EXISTS {buffered_study_region}; 
CREATE TABLE {buffered_study_region} AS SELECT'{study_region} with {buffer} km buffer'::text, ST_Buffer(geom,{buffer}) FROM {study_region};
'''.format(study_region = study_region,
           buffered_study_region = buffered_study_region,
           buffer = study_buffer))

sr = gpd.GeoDataFrame.from_postgis('SELECT ST_Transform(geom,4326) geom FROM {}'.format(study_region), engine, geom_col='geom' )       
xy = [float(sr.centroid.y),float(sr.centroid.x)]    
m = folium.Map(location=xy, tiles='Stamen Toner', zoom_start=10, control_scale=True, prefer_canvas=True)
m.save('../maps/study_region.html')

# output to completion log					
script_running_log(script, task, start, locale)
engine.dispose()
