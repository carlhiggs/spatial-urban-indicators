"""

OpenStreetMap network setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    Script:  04_create_network_resources.py
    Purpose: Create pedestrian street networks for specified city (2019)
    Authors: Carl Higgs 

"""

import time
import os
import sys
import subprocess as sp
from datetime import datetime
import psycopg2 
import networkx as nx
import osmnx as ox
from shapely.geometry import shape, MultiPolygon, Polygon
import geopandas as gpd
from sqlalchemy import create_engine
from geoalchemy2 import Geometry, WKTElement

# import folium
# from folium.plugins import MarkerCluster
# from folium.plugins import FastMarkerCluster

from bokeh.models import ColumnDataSource

from script_running_log import script_running_log
# Import custom variables for National Liveability indicator process
from _project_setup import *

def main():
    # simple timer for log file
    start = time.time()
    script = os.path.basename(sys.argv[0])
    task = 'create destination indicator tables'
    
    conn = psycopg2.connect(database=db, user=db_user, password=db_pwd, host=db_host,port=db_port)
    curs = conn.cursor()
    
    engine = create_engine("postgresql://{user}:{pwd}@{host}/{db}".format(user = db_user,
                                                                          pwd  = db_pwd,
                                                                          host = db_host,
                                                                          db   = db)) 
    
    # Copy clean intersections to postgis
    print("Prepare and copy clean intersections to postgis... ")
    curs.execute('''SELECT 1 WHERE to_regclass('public.{}') IS NOT NULL AND to_regclass('public.edges') IS NOT NULL AND to_regclass('public.nodes') IS NOT NULL;'''.format(intersections_table))
    res = curs.fetchone()
    if res is None:
        print("Get networks and save as graphs.")
        ox.config(use_cache=True, log_console=True)
        if osmnx_retain_all == 'False':
            retain_all = False
            print('''
            Note: "retain_all = False" ie. only main network segment is retained.
                Please ensure this is appropriate for your study region 
                (ie. networks on real islands may be excluded).
            ''') 
        else:
            retain_all = True
            print('''
            Note: "retain_all = True" ie. all network segments will be retained.
                Please ensure this is appropriate for your study region 
                (ie. networks on real islands will be included, however network 
                artifacts resulting in isolated network segments, or network islands,
                may also exist.  These could be problematic if sample points are 
                snapped to erroneous, mal-connected segments.  Check results.).
            ''') 
        if os.path.isfile(os.path.join(locale_dir,
              '{studyregion}_pedestrian_{osm_prefix}.graphml'.format(studyregion = buffered_study_region,
                                                                    osm_prefix = osm_prefix))):
          print('Pedestrian road network for {} has already been processed; loading this up.'.format(buffered_study_region))
          W = ox.load_graphml('{studyregion}_pedestrian_{osm_prefix}.graphml'.format(studyregion = buffered_study_region,
                                                                                     osm_prefix = osm_prefix),
                              folder = locale_dir)
        else:
          subtime = datetime.now()
          # # load buffered study region in EPSG4326 from postgis
          sql = '''SELECT geom_4326 AS geom FROM {}'''.format(buffered_study_region)
          polygon =  gpd.GeoDataFrame.from_postgis(sql, engine, geom_col='geom' )['geom'][0]
          print('Creating and saving all roads network... '),
          W = ox.graph_from_polygon(polygon,  network_type= 'all', retain_all = retain_all)
          ox.save_graphml(W, 
             filename='{studyregion}_all_{osm_prefix}.graphml'.format(studyregion = buffered_study_region,
                                                                                    osm_prefix = osm_prefix), 
             folder=locale_dir, 
             gephi=False)
          ox.save_graph_shapefile(W, 
             filename='{studyregion}_all_{osm_prefix}'.format(studyregion = buffered_study_region,
                                                                               osm_prefix = osm_prefix),
             folder = locale_dir)
          print('Done.')
          print('Creating and saving pedestrian roads network... '),
          W = ox.graph_from_polygon(polygon,  custom_filter= pedestrian, retain_all = retain_all)
          ox.save_graphml(W, 
                         filename='{studyregion}_pedestrian_{osm_prefix}.graphml'.format(studyregion = buffered_study_region,
                                                                                         osm_prefix = osm_prefix), 
              folder=locale_dir, 
              gephi=False)
          ox.save_graph_shapefile(W, 
              filename = '{studyregion}_pedestrian_{osm_prefix}'.format(studyregion = buffered_study_region,
                                                            osm_prefix = osm_prefix),
              folder = locale_dir)
          print('Done.')  
          
        print("Copy the network edges and nodes from shapefiles to Postgis..."),
        curs.execute('''SELECT 1 WHERE to_regclass('public.edges') IS NOT NULL AND to_regclass('public.nodes') IS NOT NULL;''')
        res = curs.fetchone()
        if res is None:
            for feature in ['edges','nodes']:
                command = (
                        ' ogr2ogr -overwrite -progress -f "PostgreSQL" ' 
                        ' PG:"host={host} port={port} dbname={db}'
                        ' user={user} password={pwd}" '
                        ' {dir}/{studyregion}_pedestrian_{osm_prefix}/{feature}/{feature}.shp '
                        ' -t_srs EPSG:{srid} '
                        ' -lco geometry_name="geom"'.format(host = db_host,
                                                            port=db_port,
                                                            db = db,
                                                            user = db_user,
                                                            pwd = db_pwd,
                                                            dir = locale_dir,
                                                            srid = srid,
                                                            studyregion = buffered_study_region,
                                                            osm_prefix = osm_prefix,
                                                            feature = feature) 
                        )
                print(command)
                sp.call(command, shell=True)
            print("Done (although, if it didn't work you can use the printed command above to do it manually)")  
        else:
            print("  - It appears that pedestrian network edges and nodes have already been exported to Postgis.")  
        
        # Copy clean intersections to postgis
        print("Prepare and copy clean intersections to postgis... ")
        curs.execute('''SELECT 1 WHERE to_regclass('public.{}') IS NOT NULL;'''.format(intersections_table))
        res = curs.fetchone()
        if res is None:
            # Clean intersections
            G_proj = ox.project_graph(W)
            intersections = ox.clean_intersections(G_proj, tolerance=intersection_tolerance, dead_ends=False)
            intersections.crs = G_proj.graph['crs']
            intersections_latlon = intersections.to_crs(epsg=4326)
            sql = '''
            DROP TABLE IF EXISTS {table};
            CREATE TABLE {table} (point_4326 geometry);
            INSERT INTO {table} (point_4326) VALUES {points};
            ALTER TABLE {table} ADD COLUMN geom geometry;
            UPDATE {table} SET geom = ST_Transform(point_4326,{srid});
            ALTER TABLE {table} DROP COLUMN point_4326;
            '''.format(table = intersections_table,
                    points = ', '.join(["(ST_GeometryFromText('{}',4326))".format(x.wkt) for x in intersections_latlon]),
                    srid = srid)  
            engine.execute(sql)      
            print("  - Done.")
        else:
            print("  - It appears that clean intersection data has already been prepared and imported for this region.")
    else:
        print("  - It appears that pedestrian network and clean intersections have already been exported to Postgis.") 

    curs.execute('''SELECT 1 WHERE to_regclass('public.edges_target_idx') IS NOT NULL;''')
    res = curs.fetchone()
    if res is None:
        print("Create network topology...")
        sql = '''
        ALTER TABLE edges ADD COLUMN IF NOT EXISTS "source" INTEGER;
        ALTER TABLE edges ADD COLUMN IF NOT EXISTS "target" INTEGER;
        --SELECT pgr_createTopology('edges',0.0001,'geom','ogc_fid');
        '''
        engine.execute(sql)      
        curs.execute("SELECT MIN(ogc_fid), MAX(ogc_fid) FROM edges;")
        min_id, max_id = curs.fetchone()
        print(f"there are {max_id - min_id + 1} edges to be processed")
        curs.close()

        interval = 10000
        for x in range(min_id, max_id+1, interval):
            curs = conn.cursor()
            curs.execute(
            f"select pgr_createTopology('edges', 1, 'geom', 'ogc_fid', rows_where:='ogc_fid>={x} and ogc_fid<{x+interval}');"
            )
            conn.commit()
            x_max = x + interval - 1
            if x_max > max_id:
                x_max = max_id
            print(f"edges {x} - {x_max} processed")
            
        sql = '''
        CREATE INDEX IF NOT EXISTS edges_source_idx ON edges("source");
        CREATE INDEX IF NOT EXISTS edges_target_idx ON edges("target");
        '''
        engine.execute(sql)
    else:
        print("  - It appears that the routable pedestrian network has already been set up for use by pgRouting.") 
    
    # ensure user is granted access to the newly created tables
    engine.execute(grant_query)      

    script_running_log(script, task, start)
    
    # clean up
    conn.close()

if __name__ == '__main__':
    main()