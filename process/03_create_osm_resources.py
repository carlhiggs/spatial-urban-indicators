"""

Collate OSM resources
~~~~~~~~~~~~~~~~~~~~~

Script:  
    03_create_osm_resources.py
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
from script_running_log import script_running_log
# Import custom variables for liveability indicator process
from _project_setup import *

def main():
    # simple timer for log file
    start = time.time()
    script = os.path.basename(sys.argv[0])
    task = 'Collate OSM resources'
    
    conn = psycopg2.connect(database=db, user=db_user, password=db_pwd, host=db_host,port=db_port)
    curs = conn.cursor()
    
    # create polygon boundary .poly file for extracting OSM             
    print("Create poly file, using command: "),
    locale_poly = 'poly_{}.poly'.format(study_region)
    feature = (
     'PG:"dbname={db} host={host} port={port} user={user} password={pwd}" {layer}'
     ).format(db  = db, 
              host= db_host, 
              port= db_port,
              user= db_user, 
              pwd = db_pwd, 
              layer = buffered_study_region)
    command = 'python ogr2poly.py {feature} -f region'.format(feature = feature)
    print(command)
    sp.call(command, shell=True)
    command = 'mv {poly} {dir}/{poly}'.format(dir = locale_dir,poly = locale_poly)
    print('\t{}'.format(command))
    sp.call(command, shell=True)
    print("Done.")
    
    # Extract OSM
    print("Extract OSM for studyregion"),
    if os.path.isfile('{}/{}'.format(locale_dir,osm_region)):
      print('...\r\n.osm file "{}/{}" already exists'.format(locale_dir,osm_region))
    else:
      print(" using command:")
      command = (
                 '../../osmosis/bin/osmosis --read-pbf file="{osm_data}"' 
                         ' --bounding-polygon file="{dir}/{poly}"' 
                         ' --write-xml file="{dir}/{osm_region}"'
                ).format(osm_data = osm_data,
                         dir = locale_dir,
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
                ' {dir}/{osm} --hstore --prefix {prefix}'
                ).format(user   = db_user, 
                        db     = db,
                        host   = db_host, 
                        port   = db_port,
                        dir    = locale_dir,
                        osm    = osm_region,
                        prefix = osm_prefix) 
        print(command)
        sp.call(command, shell=True)                           
        print("Done.")
        
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
    else:
        print("It appears that OSM data has already been imported for this region.")
        
    script_running_log(script, task, start)
    
    # clean up
    conn.close()

if __name__ == '__main__':
    main()