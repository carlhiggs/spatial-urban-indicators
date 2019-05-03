# Script:  create_pedestrian_networks.py
# Purpose: Create pedestrian street networks for specified city (2019)
# Author:  Carl Higgs 
# Date:    20190226

import time
import os
import sys
import subprocess as sp
from datetime import datetime
import psycopg2 
import networkx as nx
import osmnx as ox
ox.config(use_cache=True, log_console=True)
from shapely.geometry import shape, MultiPolygon, Polygon
import geopandas as gpd
from sqlalchemy import create_engine
from geoalchemy2 import Geometry, WKTElement
from script_running_log import script_running_log
# Import custom variables for National Liveability indicator process
from _project_setup import *

# simple timer for log file
start = time.time()
script = os.path.basename(sys.argv[0])
task = 'create destination indicator tables'

region_dir = '../data/study_region/{}/'.format(locale)

conn = psycopg2.connect(database=db, user=db_user, password=db_pwd, host=db_host,port=db_port)
curs = conn.cursor()

engine = create_engine("postgresql://{user}:{pwd}@{host}/{db}".format(user = db_user,
                                                                      pwd  = db_pwd,
                                                                      host = db_host,
                                                                      db   = db))

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
  W = ox.load_graphml('{studyregion}_pedestrian_{osm_prefix}.graphml'.format(studyregion = buffered_study_region,
                                                                             osm_prefix = osm_prefix),
                      folder = region_dir)
else:
  subtime = datetime.now()
  # # load buffered study region in EPSG4326 from postgis
  polygon =  gpd.GeoDataFrame.from_postgis("buffered_study_region_map", engine, geom_col='geom' )['geom'][0]
  print('Creating and saving all roads network... '),
  W = ox.graph_from_polygon(polygon,  network_type= 'all', retain_all = osmnx_retain_all)
  ox.save_graphml(W, 
     filename='{studyregion}_all_{osm_prefix}.graphml'.format(studyregion = buffered_study_region,
                                                                            osm_prefix = osm_prefix), 
     folder=region_dir, 
     gephi=False)
  ox.save_graph_shapefile(W, 
     filename='{studyregion}_all_{osm_prefix}'.format(studyregion = buffered_study_region,
                                                                       osm_prefix = osm_prefix),
     folder = region_dir)
  print('Done.')
  print('Creating and saving pedestrian roads network... '),
  W = ox.graph_from_polygon(polygon,  custom_filter= pedestrian, retain_all = osmnx_retain_all)
  ox.save_graphml(W, 
                 filename='{studyregion}_pedestrian_{osm_prefix}.graphml'.format(studyregion = buffered_study_region,
                                                                                 osm_prefix = osm_prefix), 
      folder=region_dir, 
      gephi=False)
  ox.save_graph_shapefile(W, 
      filename = '{studyregion}_pedestrian_{osm_prefix}'.format(studyregion = buffered_study_region,
                                                    osm_prefix = osm_prefix),
      folder = region_dir)
  print('Done.')  
  
print("Copy the network edges and nodes from shapefiles to postgis..."),
curs.execute('''SELECT 1 WHERE to_regclass('public.edges') IS NOT NULL AND to_regclass('public.nodes') IS NOT NULL;''')
res = curs.fetchone()
if res is None:
    for feature in ['edges','nodes']:
        command = (
                ' ogr2ogr -overwrite -progress -f "PostgreSQL" ' 
                ' PG:"host={host} port={port} dbname={db}'
                ' user={user} password = {pwd}" '
                ' {dir}/{studyregion}_pedestrian_{osm_prefix}/{feature}/{feature}.shp '
                ' -lco geometry_name="geom"'.format(host = db_host,
                                                    port=db_port,
                                                    db = db,
                                                    user = db_user,
                                                    pwd = db_pwd,
                                                    dir = region_dir,
                                                    studyregion = buffered_study_region,
                                                    osm_prefix = osm_prefix,
                                                    feature = feature) 
                )
        print(command)
        sp.call(command, shell=True)
    print("Done (although, if it didn't work you can use the printed command above to do it manually)")  
else:
    print("It appears that clean intersection data has already been prepared and imported for this region.")  

# Copy network to postgis
curs.execute('''SELECT 1 WHERE to_regclass('public.{}') IS NOT NULL;'''.format(intersections_table))
res = curs.fetchone()
if res is None:
    
    # Clean intersections
    print("Prepare cleaned intersections... "),
    
    G_proj = ox.project_graph(W)
    intersections = ox.clean_intersections(G_proj, tolerance=intersection_tolerance, dead_ends=False)
    intersections.crs = G_proj.graph['crs']
    intersections_latlon = intersections.to_crs(epsg=4326)
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
else:
    print("It appears that clean intersection data has already been prepared and imported for this region.")  

script_running_log(script, task, start)

# clean up
conn.close()