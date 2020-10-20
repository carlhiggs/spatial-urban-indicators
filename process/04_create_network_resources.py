"""

OpenStreetMap network setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Script:  
    04_create_network_resources.py
Purpose: 
    Collate OSM resources for specified city (2019)
Authors: 
    Carl Higgs 

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

from script_running_log import script_running_log
# Import custom variables for liveability indicator process
from _project_setup import *

def main():
    # simple timer for log file
    start = time.time()
    script = os.path.basename(sys.argv[0])
    task = 'create destination indicator tables'
    
    conn = psycopg2.connect(database=db, user=db_user, password=db_pwd, host=db_host,port=db_port)
    curs = conn.cursor()
    
    engine = create_engine(f"postgresql://{db_user}:{db_pwd}@{db_host}/{db}") 
    
    # Copy clean intersections to postgis
    print("Prepare and copy clean intersections to postgis... ")
    curs.execute(f'''SELECT 1 WHERE to_regclass('public.{intersections_table}') IS NOT NULL AND to_regclass('public.edges') IS NOT NULL AND to_regclass('public.nodes') IS NOT NULL;''')
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
        if os.path.isfile(f'{locale_dir}/{buffered_study_region}_pedestrian_{osm_prefix}.graphml'):
          print(f'Pedestrian road network for {buffered_study_region} has already been processed; loading this up.')
          W = ox.load_graphml(f'{locale_dir}/{buffered_study_region}_pedestrian_{osm_prefix}.graphml')
        else:
          subtime = datetime.now()
          # # load buffered study region in EPSG4326 from postgis
          sql = f'''SELECT geom_4326 AS geom FROM {buffered_study_region}'''
          polygon =  gpd.GeoDataFrame.from_postgis(sql, engine, geom_col='geom' )['geom'][0]
          print('Creating and saving all roads network... '),
          W = ox.graph_from_polygon(polygon,  network_type= 'all', retain_all = retain_all)
          ox.save_graphml(W, filepath=f'{locale_dir}/{buffered_study_region}_all_{osm_prefix}.graphml',gephi=False)
          ox.save_graph_shapefile(W, filepath=f'{locale_dir}/{buffered_study_region}_all_{osm_prefix}')
          print('Done.')
          print('Creating and saving pedestrian roads network... '),
          W = ox.graph_from_polygon(polygon,  custom_filter= pedestrian, retain_all = retain_all,network_type='walk')
          ox.save_graphml(W,filepath=f'{locale_dir}/{buffered_study_region}_pedestrian_{osm_prefix}.graphml',gephi=False)
          ox.save_graph_shapefile(W, filepath=f'{locale_dir}/{buffered_study_region}_pedestrian_{osm_prefix}')
          print('Done.')  
          
        print("Copy the network edges and nodes from shapefiles to Postgis..."),
        curs.execute('''SELECT 1 WHERE to_regclass('public.edges') IS NOT NULL AND to_regclass('public.nodes') IS NOT NULL;''')
        res = curs.fetchone()
        if res is None:
            for feature in ['edges','nodes']:
                command = (
                        ' ogr2ogr -overwrite -progress -f "PostgreSQL" ' 
                       f' PG:"host={db_host} port={db_port} dbname={db}'
                       f' user={db_user} password={db_pwd}" '
                       f' {locale_dir}/{buffered_study_region}_pedestrian_{osm_prefix}/{feature}.shp '
                       f' -t_srs EPSG:{srid} '
                        ' -lco geometry_name="geom"'
                        )
                print(command)
                sp.call(command, shell=True)
            print("Done (although, if it didn't work you can use the printed command above to do it manually)")  
        else:
            print("  - It appears that pedestrian network edges and nodes have already been exported to Postgis.")  
        
        if not engine.has_table(intersections_table): 
            ## Copy clean intersections to postgis
            print("\nPrepare and copy clean intersections to postgis... ")
            # Clean intersections
            G_proj = ox.project_graph(W)
            intersections = ox.consolidate_intersections(G_proj, tolerance=intersection_tolerance, rebuild_graph=False, dead_ends=False, reconnect_edges=False)
            if rebuild:
                points = ', '.join(["(ST_GeomFromText('POINT({} {})', 4326))".format(intersections.nodes[k]['lon'],intersections.nodes[k]['lat']) for k in intersections.nodes.keys() if 'lon' in intersections.nodes[k].keys()])
            else:
                intersections.crs = G_proj.graph['crs']
                intersections_latlon = intersections.to_crs(epsg=4326)
                points = ', '.join(["(ST_GeometryFromText('{}',4326))".format(x.wkt) for x in intersections_latlon])
            
            sql = f'''
            DROP TABLE IF EXISTS {intersections_table};
            CREATE TABLE {intersections_table} (point_4326 geometry);
            INSERT INTO {intersections_table} (point_4326) VALUES {points};
            ALTER TABLE {intersections_table} ADD COLUMN geom geometry;
            UPDATE {intersections_table} SET geom = ST_Transform(point_4326,{srid});
            ALTER TABLE {intersections_table} DROP COLUMN point_4326;
            '''
            engine.execute(sql)      
            print("  - Done.")
        else:
            print("  - It appears that clean intersection data has already been prepared and imported for this region.")
    else:
        print("\nIt appears that edges, nodes and clean intersection data have already been prepared and imported for this region.")

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