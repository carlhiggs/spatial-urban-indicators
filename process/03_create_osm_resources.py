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
ox.config(use_cache=True, log_console=True)
from shapely.geometry import shape, MultiPolygon, Polygon
import geopandas as gpd
import psycopg2 
from sqlalchemy import create_engine
from geoalchemy2 import Geometry, WKTElement
from script_running_log import script_running_log
# Import custom variables for National Liveability indicator process
from _project_setup import *
from osmnx_additional_custom_functions import *

# simple timer for log file
start = time.time()
script = os.path.basename(sys.argv[0])
task = 'create destination indicator tables'

region_dir = '../data/study_region/{}/'.format(locale)

conn = psycopg2.connect(database=db, user=db_user, password=db_pwd)
curs = conn.cursor()

engine = create_engine("postgresql://{user}:{pwd}@{host}/{db}".format(user = db_user,
                                                                      pwd  = db_pwd,
                                                                      host = db_host,
                                                                      db   = db))

# create polygon boundary .poly file for extracting OSM             
print("Create poly file, using command: "),
locale_poly = 'poly_10km_study_region_buffer.poly'
feature = (
 'PG:"dbname={db} host={host} port={port} user={user} password = {pwd}" {layer}'
 ).format(db  = db, 
          host= db_host, 
          port= db_port,
          user= db_user, 
          pwd = db_pwd, 
          layer = 'buffered_study_region_map')
command = 'python ogr2poly.py {feature} -f Description'.format(feature = feature)
print(command)
sp.call(command, shell=True)
command = 'mv {poly} {dir}{poly}'.format(dir = region_dir,poly = locale_poly)
print('\t{}'.format(command))
sp.call(command, shell=True)
print("Done.")

# Extract OSM
print("Extract OSM for studyregion"),
if os.path.isfile('{}/{}'.format(region_dir,osm_region)):
  print('...\r\n.osm file "{}/{}" already exists'.format(region_dir,osm_region))

if not os.path.isfile('{}/{}'.format(region_dir,osm_region)):
  print(" using command:")
  command = (
             '../../osmosis/bin/osmosis --read-pbf file="{osm_data}"' 
                     ' --bounding-polygon file="{dir}{poly}"' 
                     ' --write-xml file="{dir}{osm_region}"'
            ).format(osm_data = osm_data,
                     dir = region_dir,
                     poly = locale_poly,
                     osm_region = osm_region)
  print(command)
  sp.call(command, shell=True)
print('Done.')

# import buffered study region OSM excerpt to pgsql, 
# check if OSM excerpt has previously been imported
curs.execute('''SELECT 1 WHERE to_regclass('public.{}_line') IS NOT NULL;'''.format(osm_prefix))
res = curs.fetchone()
if res is None:
    print("Copying OSM excerpt to pgsql..."),
    command = (
            'osm2pgsql -U {user} -l -d {db} --host {host} --port {port}'
            ' {dir}{osm} --hstore --prefix {prefix}'
            ).format(user   = db_user, 
                    db     = db,
                    host   = db_host, 
                    port   = db_port,
                    dir    = region_dir,
                    osm    = osm_region,
                    prefix = osm_prefix) 
    print(command)
    sp.call(command, shell=True)                           
    print("Done.")
else:
    print("It appears that OSM data has already been imported for this region.")

# connect to the PostgreSQL server and ensure privileges are granted for all public tables
curs.execute(grant_query)
conn.commit()

required_fields_list = df_osm["required_tags"].dropna().tolist()

for shape in ['line','point','polygon','roads']:
  # Define tags for which presence of values is suggestive of some kind of open space 
  # These are defined in the _project_configuration worksheet 'open_space_defs' under the 'required_tags' column.
  required_tags = '\n'.join([(
    'ALTER TABLE {prefix}_{shape} ADD COLUMN IF NOT EXISTS "{field}" varchar;'
    ).format(prefix = osm_prefix,
             shape = shape, 
             field = x) for x in required_fields_list]
    )
  sql = ['''
  -- Add geom column to polygon table, appropriately transformed to project spatial reference system
  ALTER TABLE {osm_prefix}_{shape} ADD COLUMN geom geometry; 
  UPDATE {osm_prefix}_{shape} SET geom = ST_Transform(way,{srid}); 
  CREATE INDEX {osm_prefix}_{shape}_idx ON {osm_prefix}_{shape} USING GIST (geom);
  '''.format(osm_prefix = osm_prefix, shape = shape,srid=srid),
  '''
  -- Add other columns which are important if they exists, but not important if they don't
  -- --- except that there presence is required for ease of accurate querying.
  {}'''.format(required_tags)]
  for query in sql:
    start = time.time()
    print("\nExecuting: {}".format(query))
    curs.execute(query)
    conn.commit()
    print("Executed in {} mins".format((time.time()-start)/60))

curs.execute(grant_query)
conn.commit()    

print("Create filtered networks using Osmosis")
print("  -- all highways")
command = '''
../../osmosis/bin/osmosis \
--read-xml {dir}/{osm} \
--tf accept-ways highway=* \
--tf reject-relations \
--used-node \
--write-xml {dir}/routable_all_{osm}
'''.format(dir = region_dir, osm = osm_region)
print(command)
sp.call(command, shell=True)  
print("  -- pedestrian ways")
command = '''../../osmosis/bin/osmosis \
--read-xml {dir}/routable_all_{osm} \
--tf accept-ways highway=* \
--tf reject-ways highway=motorway,motor,proposed,construction,abandoned,platform,raceway \
--tf reject-ways foot=no \
--tf reject-ways service=private \
--tf reject-ways access=private \
--tf reject-relations \
--used-node \
--write-xml {dir}/routable_pedestrian_{osm}
'''.format(dir = region_dir, osm = osm_region)
print(command)
sp.call(command, shell=True)  
print("Done.\n")

print("Get networks and save as graphs.")
if osmnx_retain_all == 'False':
    osmnx_retain_all = False
    print('''
    Note: "retain_all = False" ie. only main network segment is retained.
        Please ensure this is appropriate for your study region 
        (ie. networks on real islands may be excluded).
    ''') 
else:
    osmnx_retain_all = True
    print('''
    Note: "retain_all = True" ie. all network segments will be retained.
        Please ensure this is appropriate for your study region 
        (ie. networks on real islands will be included, however network 
        artifacts resulting in isolated network segments, or network islands,
        may also exist.  These could be problematic if sample points are 
        snapped to erroneous, mal-connected segments.  Check results.).
    ''') 

if os.path.isfile(os.path.join(region_dir,
      '{studyregion}_pedestrian_{osm_prefix}.graphml'.format(studyregion = buffered_study_region,
                                                            osm_prefix = osm_prefix))):
  print('Pedestrian road network for {} has already been processed; loading this up.'.format(buffered_study_region))
  W = ox.load_graphml(os.path.join(region_dir,
      '{studyregion}_pedestrian_{osm_prefix}.graphml'.format(studyregion = buffered_study_region,
                                                            osm_prefix = osm_prefix)))
else:
  subtime = datetime.now()
  # # load buffered study region in EPSG4326 from postgis
  # polygon =  gpd.GeoDataFrame.from_postgis("buffered_study_region_map", engine, geom_col='geom' )['geom'][0]
  print('Creating and saving all roads network... '),
  W = graph_from_file_modified(filename='{dir}/routable_all_{osm}'.format(dir = region_dir, 
                                                                    osm = osm_region),
                                                                    retain_all = osmnx_retain_all)
  ox.save_graphml(W, 
     filename=os.path.join('..',region_dir,
                           '{studyregion}_all_{osm_prefix}.graphml'.format(studyregion = buffered_study_region,
                           osm_prefix = osm_prefix)), 
     folder=None, 
     gephi=False)
  ox.save_graph_shapefile(W, 
     filename=os.path.join('..',region_dir,
                           '{studyregion}_all_{osm_prefix}'.format(studyregion = buffered_study_region,
                                                                       osm_prefix = osm_prefix)))
  print('Done.')
  print('Creating and saving pedestrian roads network... '),
  W = graph_from_file_modified(filename='{dir}/routable_pedestrian_{osm}'.format(dir = region_dir, 
                                                                    osm = osm_region),
                                                                    retain_all = osmnx_retain_all)
  ox.save_graphml(W, filename=os.path.join('..',region_dir,
      '{studyregion}_pedestrian_{osm_prefix}_unsimplified.graphml'.format(studyregion = buffered_study_region,
                                                            osm_prefix = osm_prefix)), 
      folder=None, 
      gephi=False)
  ox.save_graph_shapefile(W, 
      filename=os.path.join('..',region_dir,
      '{studyregion}_pedestrian_{osm_prefix}'.format(studyregion = filename,
                                                    osm_prefix = osm_prefix)))
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
