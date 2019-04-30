# Script:  create_pedestrian_networks.py
# Purpose: Create pedestrian street networks for specified city (2019)
# Author:  Carl Higgs 
# Date:    20190226

import time
import os
import sys
import subprocess as sp
from datetime import datetime
import networkx as nx
import osmnx as ox
ox.config(use_cache=True, log_console=False)
import requests
import fiona
from shapely.geometry import shape, MultiPolygon, Polygon
# from sqlalchemy import *
from sqlalchemy import create_engine
import geopandas as gpd
from geoalchemy2 import Geometry, WKTElement
import requests
import json
from script_running_log import script_running_log
# Import custom variables for National Liveability indicator process
from _project_setup import *

# simple timer for log file
start = time.time()
script = os.path.basename(sys.argv[0])
task = 'create destination indicator tables'

engine = create_engine("postgresql://{user}:{pwd}@{host}/{db}".format(user = db_user,
                                                                      pwd  = db_pwd,
                                                                      host = db_host,
                                                                      db   = db))
                                                                      
# define pedestrian network custom filter (based on OSMnx 'walk' network type, without the cycling exclusion)
pedestrian = (
             '["area"!~"yes"]' 
             '["highway"!~"motor|proposed|construction|abandoned|platform|raceway"]'
             '["foot"!~"no"]'  
             '["service"!~"private"]' 
             '["access"!~"private"]'
             )

# conversion settings

# output suffix
suffix = osm_prefix.strip('osm')

# print("Create poly file, using command: "),
# locale_poly = 'poly_10km_study_region_buffer.poly'
# feature = (
 # 'PG:"dbname={db} host={host} port={port} user={user} password = {pwd}" {layer}'
 # ).format(db  = db, 
          # host= db_host, 
          # port= db_port,
          # user= db_user, 
          # pwd = db_pwd, 
          # layer = 'buffered_study_region_map')
# command = 'python ogr2poly.py {feature} -f Description'.format(feature = feature)
# # print('{}'.format(command))
# sp.call(command, shell=True)
# command = 'mv {poly} ../data/study_region/{locale}/{poly}'.format(locale = locale,poly = locale_poly)
# # print('\t{}'.format(command))
# sp.call(command, shell=True)
# print("Done.")

# # Extract OSM
# print("Extract OSM for studyregion... "),
# osm_region = '../data/study_region/{}/{}'.format(locale,osm_region)
# if os.path.isfile('{}'.format(osm_region)):
  # print('.osm file {} already exists'.format(osm_region))
 
# if not os.path.isfile('{}'.format(osm_region)):
  # command = (
             # '../../osmosis/bin/osmosis --read-xml file="{}"' 
                     # '--bounding-polygon file="{}"' 
                     # '--write-xml file="{}"'
            # ).format(osm_data,locale_poly,osm_region)
  # sp.call(command, shell=True)
# print('Done.')

# # import buffered study region OSM excerpt to pgsql, 
# print("Copying OSM excerpt to pgsql..."),
# command = (
          # 'osm2pgsql -U {user} -l -d {db} --host {host} --port {port}'
          # '{osm} --hstore --style {style} --prefix {prefix}'
          # ).format(user   = db_user, 
                   # db     = db,
                   # host   = db_host, 
                   # port   = db_port,
                   # osm    = osm_source,
                   # style  = osm2pgsql_style,
                   # prefix = osm_prefix) 
# print(command)
# sp.call(command, shell=True)                           
# print("Done.")

print('Get networks and save as graphs (retain_all = False*** ie. only main network segment is retained).  Ensure this is appropriate for your study region.  In future, we could make this an optional parameter (false by default, but true if a region is known to have islands.  The problem with network islands is that, in many cases they are artifacts of cartography, not true islands.')
retain_all = False
root = '../data/study_region/{locale}'
filename = '{}_{}'.format(buffered_study_region,year)

if os.path.isfile(os.path.join(root,
      'osm_{studyregion}_pedestrian_{suffix}.graphml'.format(studyregion = filename,
                                                            suffix = suffix))):
  print('Pedestrian road network for {} has already been processed; loading this up.'.format(filename))
  W = ox.load_graphml(os.path.join(root,
      'osm_{studyregion}_pedestrian_{suffix}.graphml'.format(studyregion = filename,
                                                            suffix = suffix)))
else:
  subtime = datetime.now()
  # load buffered study region in EPSG4326 from postgis
  polygon =  gpd.GeoDataFrame.from_postgis("buffered_study_region_map", engine, geom_col='geom' )['geom'][0]
  print('Creating and saving all roads network... '),
  W = ox.graph_from_polygon(polygon,  network_type= 'all', retain_all = retain_all)
  ox.save_graphml(W, 
     filename=os.path.join(root,
                           'osm_{studyregion}_all_{suffix}.graphml'.format(studyregion = filename,
                           suffix = suffix)), 
     folder=None, 
     gephi=False)
  ox.save_graph_shapefile(W, 
     filename=os.path.join(root,
                           'osm_{studyregion}_all_{suffix}'.format(studyregion = filename,
                                                                       suffix = suffix)))
  print('Done.')
  print('Creating and saving pedestrian roads network... '),
  W = ox.graph_from_polygon(polygon,  custom_filter= pedestrian, retain_all = retain_all)
  ox.save_graphml(W, filename=os.path.join(root,
      'osm_{studyregion}_pedestrian_{suffix}.graphml'.format(studyregion = filename,
                                                            suffix = suffix)), 
      folder=None, 
      gephi=False)
  ox.save_graph_shapefile(W, 
      filename=os.path.join(root,
      'osm_{studyregion}_pedestrian_{suffix}'.format(studyregion = filename,
                                                    suffix = suffix)))
  print('Done.')                                                            

# Copy network to postgis
print("Copy the network edges and nodes from gdb to postgis..."),
command = (
        ' ogr2ogr -overwrite -progress -f "PostgreSQL" ' 
        ' PG:"host={host} port=5432 dbname={db}'
        ' user={user} password = {pwd}" '
        ' {gdb} {feature} '
        ' -lco geometry_name="geom"'.format(host = db_host,
                                     db = db,
                                     user = db_user,
                                     pwd = db_pwd,
                                     gdb = gdb_path,
                                     feature = '"edges" "nodes"') 
        )
print(command)
sp.call(command, shell=True)
print("Done (although, if it didn't work you can use the printed command above to do it manually)")  
  
# Clean intersections
print("Prepare cleaned intersections... "),

G_proj = ox.project_graph(W)
intersections = ox.clean_intersections(G_proj, tolerance=12, dead_ends=False)
intersections.crs = G_proj.graph['crs']
intersections_latlon = intersections.to_crs(epsg=4326)
intersections_table = "clean_intersections_12m"
# to sql  - works well!
engine = create_engine("postgresql://{user}:{pwd}@{host}/{db}".format(user = db_user,
                                                                      pwd  = db_pwd,
                                                                      host = db_host,
                                                                      db   = db))
conn = engine.connect()
statement = '''
  DROP TABLE IF EXISTS {table};
  CREATE TABLE {table} (point_4326 geometry);
  INSERT INTO {table} (point_4326) VALUES {points};
  ALTER TABLE {table} ADD COLUMN geom geometry;
  UPDATE {table} SET geom = ST_Transform(point_4326,{srid});
  ALTER TABLE {table} DROP COLUMN point_4326;
'''.format(table = intersections_table,
           points = ', '.join(["(ST_GeometryFromText('{}',4326))".format(x.wkt) for x in intersections_latlon]),
           srid = srid)  
conn.execute(statement)      
print("Done.")
  

script_running_log(script, task, start)

# clean up
conn.close()
