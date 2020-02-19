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
    df = df_datasets.query("purpose=='destinations'").copy()
    # define destination type and name from dataset index
    df[['destination','name']] =  df.apply(lambda x: x.name.split(':'),axis=1, result_type="expand")
    # create OSM data flag
    df['osm'] = (df.provider.isin(['OpenStreetMap','OSM'])| df.destination.str.startswith('osm') | df.destination.str.endswith('osm'))
    # retrieve definitions for relevant OSM destinations
    df_osm = df_osm_dest.query('destination in {}'.format(df[df['osm']].name.values)).copy()
    df_osm['pre-condition'] = df_osm['pre-condition'].replace('NULL','OR')
    df_osm_unique = df_osm[['destination','name','domain']].drop_duplicates(subset=['destination'])
    # Create destination type table and destination in sql database
    # The destination type table is a summary of all destinations in study region
    sql = '''
      DROP TABLE IF EXISTS dest_type;
      CREATE TABLE dest_type
      (
       destination varchar PRIMARY KEY,
       name varchar,
       data varchar,
       domain varchar NOT NULL,
       count integer
      );
       '''
    engine.execute(sql)
    # The destination schema is used for storing destination features in the study region
    schema = 'destinations'
    create_destination_schema = f'''
      CREATE SCHEMA IF NOT EXISTS {schema};
      --DROP TABLE IF EXISTS osm_destinations;
      --CREATE TABLE osm_destinations
      --(
      -- dest_oid SERIAL PRIMARY KEY,
      -- osm_id varchar,
      -- destination varchar NOT NULL,
      -- name varchar NOT NULL,
      -- geom geometry(POINT)
      --);
    '''
    engine.execute(create_destination_schema)
    print("\nImporting destinations...")
    print("\n{dest:50} {dest_count}".format(dest = "Destination",dest_count = "Import count"))
    # get bounding box of buffered study region for clipping using ogr2ogr on import
    for row in df.itertuples():
        destination = getattr(row,'destination')  
        data = getattr(row,'data_dir')
        name = getattr(row,'name')
        domain = getattr(row,'data_name')
        osm = getattr(row,'osm')
        encoding = getattr(row,'data_encoding')
        epsg = getattr(row,'epsg')
        sql = f'''SELECT ST_Extent(ST_Transform(geom,{epsg})) FROM {buffered_study_region};'''
        urban_region = engine.execute(sql).fetchone()
        urban_region = [float(x) for x in urban_region[0][4:-1].replace(',',' ').split(' ')]
        bbox =  '{} {} {} {}'.format(*urban_region)
        if str(encoding) not in ['','nan']:
            encoding = f'--config SHAPE_ENCODING {encoding}'
        else:
            encoding = ''
        # print(f"{destination} {data} {name} {domain} {osm}")
        if not osm:
            # do stuff
            print("\nCopy all pre-processed destinations to postgis..."),
            command = (
               ' ogr2ogr -overwrite -progress -f "PostgreSQL" ' 
              f' PG:"host={db_host} port={db_port} dbname={db} user={db_user} password = {db_pwd}" '
              f' {encoding} ".{data}" -lco schema={schema} -nln {name} -clipsrc {bbox} '
               ' -lco geometry_name="geom" -lco OVERWRITE=YES '
               ' -s_srs ESPG:{epsg} -t_srs EPSG:{srid} '
               )
            print(command)
            sp.call(command, shell=True)
            print("Done (although, if it didn't work you can use the printed command above to do it manually)")

        if osm:
            create_osm_destinations_table = '''
              DROP TABLE IF EXISTS {};
              CREATE TABLE {}
              (
               dest_oid SERIAL PRIMARY KEY,
               osm_id varchar,
               destination varchar NOT NULL,
               name varchar NOT NULL,
               geom geometry(POINT)
              );
            '''.format(destination)
            engine.execute(create_osm_destinations_table)
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
              INSERT INTO osm_destinations (osm_id, destination,name,geom)
              SELECT osm_id, '{dest}','{name}', d.geom 
                FROM {osm_prefix}_point d
               WHERE {dest_condition};
            '''
            curs.execute(combine__point_destinations)
            conn.commit()        
        
        # get point dest count in order to set correct auto-increment start value for polygon dest OIDs
        curs.execute(f'''SELECT count(*) FROM osm_destinations WHERE destination = '{dest}';''')
        dest_count = int(list(curs)[0][0])       
        
        combine_poly_destinations = f'''
          INSERT INTO osm_destinations (osm_id, destination,name,geom)
          SELECT osm_id, '{dest}','{name}', ST_Centroid(d.geom)
            FROM {osm_prefix}_polygon d
           WHERE {dest_condition};
        '''
        curs.execute(combine_poly_destinations)
        conn.commit()      
        
        curs.execute(f'''SELECT count(*) FROM osm_destinations WHERE destination = '{dest}';''')
        dest_count = int(list(curs)[0][0])  
        
        if dest_count > 0:
          summarise_dest_type = f'''
          INSERT INTO dest_type (destination,name,domain,count)
          SELECT '{dest}',
                 '{name}',
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
    