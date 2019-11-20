# Script:  15_od_distances_3200m.py
# Purpose: This script records the distances to all destinations within 3200m
# Authors: Carl Higgs
# Date: 20190208

import os
import time
import multiprocessing
import sys
import psycopg2 
import numpy as np
from progressor import progressor

from script_running_log import script_running_log

# Import custom variables for National Liveability indicator process
from _project_setup import *

# simple timer for log file
start = time.time()
script = os.path.basename(sys.argv[0])

# SQL Settings
## Note - this used to be 'dist_cl_od_parcel_dest' --- simplified to 'result_table'
result_table = "local_network_3200m"
progress_table = "{table}_progress".format(table = result_table)
 
conn = psycopg2.connect(database=db, user=db_user, password=db_pwd)
curs = conn.cursor() 

# tally expected parcel-destination class result set  
curs.execute("SELECT count(*) FROM edges_vertices_pgr;")
goal = list(curs)[0][0]
curs.execute('''
  SELECT DISTINCT(from_v) 
  FROM local_network_3200m
  ORDER BY from_v ASC;
  ''')

processed_id_list = [x[0] for x in list(curs)]
processed = len(processed_id_list)
if processed==0:
  processed_id_list = [0]
    

conn.close()

# Worker/Child PROCESS
def process_local_network(from_id): 
    # Connect to SQL database 
    try:
        conn = psycopg2.connect(database=db, user=db_user, password=db_pwd)
        curs = conn.cursor()
    except:
        print("SQL connection error")
        print(sys.exc_info()[1])
        return 100
    try:   
        to_id = from_id+1000
        id_list_to_process = [x for x in range(from_id,to_id) if x not in processed_id_list]
        if len(id_list_to_process) > 0:
            last_id = max(id_list_to_process)
            count = len(id_list_to_process)
            id_array = ','.join([str(x) for x in id_list_to_process])
            place = 'before local network query'
            sql = f'''
              INSERT INTO local_network_3200m
              SELECT from_v,node,edge,agg_cost
              FROM pgr_drivingDistance(
                  'SELECT ogc_fid AS id, source, target, length::float8 as cost FROM edges',
                  ARRAY[{id_array}],
                 3200,
                  false
                  )
              ON CONFLICT (id) DO NOTHING
              ;
             '''      
            # print(sql)
            curs.execute(sql)
            conn.commit()       
            place = "update progress (post OD matrix results, successful)"
            # update current progress
            curs.execute(f'''UPDATE {progress_table} SET processed = processed+{count}''')
            conn.commit()
        else:
            last_id = max(processed_id_list)
        place = "check progress"
        curs.execute(f'''SELECT processed from {progress_table}''')
        progress = int(list(curs)[0][0])
        place = 'final progress'
        completion_time = time.strftime("%Y%m%d-%H%M%S")
        progressor(progress,
                   goal,
                   start,
                   f'''{progress}/{goal}; last id processed: {last_id}, at {completion_time}''') 
    except:
        print('''Error: {}\nPlace: {}'''.format( sys.exc_info(),place))  
    finally:
        conn.close()
    
# MAIN PROCESS
if __name__ == '__main__':
  task = 'Record distances from origins to destinations within 3200m'
  print("Commencing task ({}): {} at {}".format(db,task,time.strftime("%Y%m%d-%H%M%S")))
  # initial postgresql connection
  conn = psycopg2.connect(database=db, user=db_user, password=db_pwd)
  curs = conn.cursor()  
  
  create_results_table = '''
  CREATE TABLE IF NOT EXISTS local_network_3200m
  (
  from_v   bigint           ,
  node     bigint           ,
  edge     bigint           ,
  agg_cost double precision 
  )
  ;
   '''
  curs.execute(create_results_table)
  conn.commit()
  
  print("Create a table for tracking progress... "), 
  create_progress_table = f'''
    DROP TABLE IF EXISTS {progress_table};
    CREATE TABLE IF NOT EXISTS {progress_table} (processed int);
    INSERT INTO {progress_table} (processed) VALUES ({processed});
    '''
  # print(create_progress_table)
  curs.execute(create_progress_table)
  conn.commit()
  print("Done.")
  evaluate_progress = f'''
   SELECT processed FROM {progress_table};
  '''
  curs.execute(evaluate_progress)
  processed = list(curs)[0][0] # assumes processing was not prematurely truncated

  if processed < goal:
    print("Commence multiprocessing..."),
    place_to_start = min(processed_id_list)
    # Parallel processing setting
    pool = multiprocessing.Pool(processes=cpu_count)
    # get list of ids over which to iterate
    # this assumes that the ids are sequential integers
    iteration_list = [i*1000 for i in range(place_to_start,int((goal+1000)/1000))]
    # # Iterate process over hexes across cpu_count
    divvy_load = math.ceil(len(iteration_list)/cpu_count)
    pool.map(process_local_network, iteration_list, chunksize=divvy_load)
    evaluate_progress = '''
     SELECT processed FROM {};
    '''.format(progress_table)
    curs.execute(evaluate_progress)
    processed = list(curs)[0][0]
    if processed < goal:
      print('''
      The script has finished running, however the number of results processed {} is still less than the goal{}.  
      There may be a bug.  
      Please investigate how this might have occurred.
      '''.format(processed,goal))
    if processed > goal:
      print('''
      The number of processed results is larger than the completion goal ({}).
      it appears something has gone wrong. 
      Please check how this might have occurred.  
      There may be a bug.
      '''.format(goal))
    else:
      print('''The completion goal of {} has been completed.'''.format(goal))
  # output to completion log    
  if processed == goal:
    # this script will only be marked as successfully complete if the number of results processed matches the completion goal.
    script_running_log(script, task, start, locale)
  print("Processing completed.\nCreating indices...",)           
  sql = '''
  CREATE INDEX IF NOT EXISTS local_network_3200m_idx   ON local_network_3200m("from_v",agg_cost);
  CREATE INDEX IF NOT EXISTS local_network_3200m_edge  ON local_network_3200m("edge");
  '''
  curs.execute(sql)
  conn.commit()
  print("Done.")
  conn.close()
