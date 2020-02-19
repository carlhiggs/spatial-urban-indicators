"""

Compile destinations
~~~~~~~~~~~~~~~~~~~~

::

    Script:  06_compile_destinations.py
    Purpose: Compile a schema of destination features
    Authors: Carl Higgs 

"""
import time
import psycopg2
from sqlalchemy import create_engine
from script_running_log import script_running_log
from _project_setup import *

connection = f"postgresql://{db_user}:{db_pwd}@{db_host}/{db}"

def main():
    # simple timer for log file
    start = time.time()
    script = os.path.basename(sys.argv[0])
    task = 'Compile study region destinations'
    print("Commencing task: {} at {}".format(task,time.strftime("%Y%m%d-%H%M%S")))
    engine = create_engine(connection)
    # get list of datasets used for access analysis
    # Later, this could be broadened for other destination types
    df = df_datasets[df_datasets.index.str.startswith('access:')]
    df['destination'] = df.index.copy()
    # strip the indicator tags to leave just destination id
    df['destination'] = df.destination.apply(lambda x: '_'.join(x.split('_')[1:]))
    # list destinations which have OpenStreetMap specified as their data source
    df_osm_dest_unique = df_osm_dest[['destination','dest_full_name','domain']].drop_duplicates(subset=['destination'])
    df_osm_dest['pre-condition'] = df_osm_dest['pre-condition'].replace('NULL','OR')
    # dest_osm_list = [x.encode('utf') for x in df_osm_dest_unique['destination']]
    # Create destination type table in sql database
    # connect to the PostgreSQL server
    conn = psycopg2.connect(dbname=db, user=db_user, password=db_pwd)
    curs = conn.cursor()

    # Create empty combined destination table
    sql = '''
      DROP TABLE IF EXISTS dest_type;
      CREATE TABLE dest_type
      (
       destination varchar PRIMARY KEY,
       destination_name varchar,
       domain varchar NOT NULL,
       count integer
      );
       '''
    engine.execute(sql)
    
    create_osm_destinations_table = '''
      CREATE SCHEMA IF NOT EXISTS destinations;
      --DROP TABLE IF EXISTS osm_destinations;
      --CREATE TABLE osm_destinations
      --(
      -- dest_oid SERIAL PRIMARY KEY,
      -- osm_id varchar,
      -- destination varchar NOT NULL,
      -- destination_name varchar NOT NULL,
      -- geom geometry(POINT)
      --);
    '''
    curs.execute(create_osm_destinations_table)
    conn.commit()

    print("\nImporting destinations...")
    print("\n{dest:50} {dest_count}".format(dest = "Destination",dest_count = "Import count"))
    # for dest in dest_osm_list:
    for row in df_osm_dest_unique.itertuples():
        dest = getattr(row,'destination')  
        destination_name = getattr(row,'dest_full_name')
        domain = getattr(row,'domain')
        dest_condition = []
        for condition in ['AND','OR','NOT']:
        # for condition in df_osm_dest[df_osm_dest['destination']==dest]['pre-condition'].unique():
            # print(condition)
            if condition == 'AND':
                clause = ' AND '.join(df_osm_dest[(df_osm_dest['destination']==dest)&(df_osm_dest['pre-condition']=='AND')].apply(lambda x: "{} IS NOT NULL".format(x.key) if x.value=='NULL' else "{} = '{}'".format(x.key,x.value),axis=1).values.tolist())
                dest_condition.append(clause)
            if condition == 'OR':
                clause = ' OR '.join(df_osm_dest[(df_osm_dest['destination']==dest)&(df_osm_dest['pre-condition']=='OR')].apply(lambda x: "{} IS NOT NULL".format(x.key) if x.value=='NULL' else "{} = '{}'".format(x.key,x.value),axis=1).values.tolist())
                dest_condition.append(clause)
            if condition != 'NOT':
                clause = ' AND '.join(df_osm_dest[(df_osm_dest['destination']==dest)&(df_osm_dest['pre-condition']=='NOT')].apply(lambda x: "{} IS NOT NULL".format(x.key) if x.value=='NULL' else "{} != '{}' OR access IS NULL".format(x.key,x.value),axis=1).values.tolist())
                dest_condition.append(clause)
        dest_condition = [x for x in dest_condition if x!='']
        # print(len(dest_condition))
        if len(dest_condition)==1:
            dest_condition = dest_condition[0]
        else:
            dest_condition = '({})'.format(') AND ('.join(dest_condition))
        print(dest_condition)
        combine__point_destinations = f'''
          INSERT INTO osm_destinations (osm_id, destination,destination_name,geom)
          SELECT osm_id, '{dest}','{destination_name}', d.geom 
            FROM {osm_prefix}_point d
           WHERE {dest_condition};
        '''
        curs.execute(combine__point_destinations)
        conn.commit()        
        
        # get point dest count in order to set correct auto-increment start value for polygon dest OIDs
        curs.execute(f'''SELECT count(*) FROM osm_destinations WHERE destination = '{dest}';''')
        dest_count = int(list(curs)[0][0])       
        
        combine_poly_destinations = f'''
          INSERT INTO osm_destinations (osm_id, destination,destination_name,geom)
          SELECT osm_id, '{dest}','{destination_name}', ST_Centroid(d.geom)
            FROM {osm_prefix}_polygon d
           WHERE {dest_condition};
        '''
        curs.execute(combine_poly_destinations)
        conn.commit()      
        
        curs.execute(f'''SELECT count(*) FROM osm_destinations WHERE destination = '{dest}';''')
        dest_count = int(list(curs)[0][0])  
        
        if dest_count > 0:
          summarise_dest_type = f'''
          INSERT INTO dest_type (destination,destination_name,domain,count)
          SELECT '{dest}',
                 '{destination_name}',
                 '{domain}',
                 {dest_count}
          '''
          curs.execute(summarise_dest_type)
          conn.commit()
          # print destination name and tally which have been imported
          print(f"\n{dest:50} {dest_count:=10d}")
          print(f"({dest_condition})")

    create_osm_destinations_indices = '''
      CREATE INDEX osm_destinations_destination_idx ON osm_destinations (destination);
      CREATE INDEX osm_destinations_geom_geom_idx ON osm_destinations USING GIST (geom);
    '''
    curs.execute(create_osm_destinations_indices)
    conn.commit()
    curs.execute(grant_query)

    # output to completion log    
    script_running_log(script, task, start, locale)
    conn.close()

        
if __name__ == '__main__':
    main()
    