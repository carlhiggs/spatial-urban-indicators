"""

Compile destinations
~~~~~~~~~~~~~~~~~~~~

Script:  
    06_compile_destinations.py
Purpose: 
    Compile a schema of destination features
Authors: 
    Carl Higgs 

"""
import time
import psycopg2
from sqlalchemy import create_engine
from script_running_log import script_running_log
from _project_setup import *


def main():
    # simple timer for log file
    start = time.time()
    script = os.path.basename(sys.argv[0])
    task = 'Compile study region destinations'
    print("Commencing task: {} at {}".format(task,time.strftime("%Y%m%d-%H%M%S")))
    connection = f"postgresql://{db_user}:{db_pwd}@{db_host}/{db}"
    engine = create_engine(connection)
    # get list of datasets used for access analysis
    df = df_datasets.query("purpose=='destinations'").copy().sort_index()
    # define destination type and name from dataset index
    df.rename(columns={"type": "destination"},inplace=True)
    df['name'] = df.index
    # df[['destination','name']] =  df.apply(lambda x: x.name.split(':'),axis=1, result_type="expand")
    # create OSM data flag
    df['osm'] = (df.provider.isin(['OpenStreetMap','OSM'])| df.destination.str.startswith('osm') | df.destination.str.endswith('osm'))
    # retrieve definitions for relevant OSM destinations
    df_osm = df_osm_dest.query("destination in ['{}']".format("','".join( df[df['osm']].name.values))).copy()
    df_osm['condition'] = df_osm['condition'].replace('NULL','OR')
    df_osm_unique = df_osm[['destination','name','domain']].drop_duplicates(subset=['destination'])
    # The destination schema is used for storing destination features in the study region
    schema = 'destinations'
    sql = f'''
      CREATE SCHEMA IF NOT EXISTS {schema};
    '''
    engine.execute(sql)
    # Ensure any previously created destination tables are purged if existing
    for row in df.itertuples():
        destination = getattr(row,'destination')  
        name = getattr(row,'name')
        sql = f'''
            DROP TABLE IF EXISTS {schema}.{destination};
            DROP TABLE IF EXISTS {schema}.{name};
            '''
        engine.execute(sql)
    # Create destination type table and destination in sql database
    # The destination type table is a summary of all destinations in study region
    sql = '''
      DROP TABLE IF EXISTS destination_catalog;
      CREATE TABLE destination_catalog
      (
       destination varchar,
       name varchar,
       domain varchar NOT NULL,
       count integer,
       data varchar,
       PRIMARY KEY (destination, name, data)
      );
       '''
    engine.execute(sql)
    print("\nImporting destinations...")
    print("\n{:25} {:25} {}".format("Destination","Name","Imported"))
    for row in df.itertuples():
        destination = getattr(row,'destination')  
        sql = f'''
            CREATE TABLE IF NOT EXISTS {schema}.{destination}
            (
            name varchar,
            oid int,
            geom geometry(Point, {srid}),
            PRIMARY KEY (name, oid)
            );
        '''
        engine.execute(sql)
        data = getattr(row,'data_file')
        name = getattr(row,'name')
        domain = getattr(row,'data_name')
        osm = getattr(row,'osm')
        encoding = getattr(row,'data_encoding')
        # print(f"{destination} {data} {name} {domain} {osm}")
        if str(encoding) not in ['','nan']:
            encoding = f'--config SHAPE_ENCODING {encoding}'
        else:
            encoding = ''
        if not osm:
            epsg = int(getattr(row,'epsg'))
            # transform data if not in project spatial reference
            if epsg!=srid:
                transform =   f' -s_srs "EPSG:{epsg}" -t_srs "EPSG:{srid}" '
            else:
                transform = ''
            # get bounding box of buffered study region for clipping external data using ogr2ogr on import
            sql = f'''SELECT ST_Extent(ST_Transform(geom,{epsg})) FROM {buffered_study_region};'''
            urban_region = engine.execute(sql).fetchone()
            urban_region = [float(x) for x in urban_region[0][4:-1].replace(',',' ').split(' ')]
            bbox =  '{} {} {} {}'.format(*urban_region)
            # do stuff
            command = (
               ' ogr2ogr -overwrite -f "PostgreSQL" ' 
              f' PG:"host={db_host} port={db_port} dbname={db} user={db_user} password = {db_pwd}" '
              f' {encoding} ".{data}" -lco schema={schema} -nln {name} -clipsrc {bbox} '
               ' -lco geometry_name="geom" -lco OVERWRITE=YES '
              f' {transform}'
               )
            # print(command)
            sp.call(command, shell=True)
            # insert destinations from potentially different sources into combined table
            sql = f'''
                ALTER TABLE {schema}.{name} RENAME COLUMN ogc_fid TO oid;
                INSERT INTO {schema}.{destination} (name, oid, geom)
                SELECT '{name}',oid, d.geom
                FROM {schema}.{name} d
                ON CONFLICT (name,oid) DO NOTHING;
            '''
            engine.execute(sql)
            # catalogue destinations from this data source
            sql = f'''SELECT count(*) FROM {schema}.{name};'''
            count = engine.execute(sql).fetchone()[0]
            sql = f'''
                INSERT INTO destination_catalog (destination,name,domain,count,data)
                SELECT '{destination}',
                       '{name}',
                       '{domain}',
                        {count},
                       '{data}'
                ON CONFLICT (destination, name, data) DO NOTHING;
            '''
            engine.execute(sql)
            print(f"{destination:25} {name:25} {count:=10d}")
            sql = f'''
              CREATE INDEX IF NOT EXISTS {name}_idx ON {schema}.{name} (oid);
              CREATE INDEX IF NOT EXISTS {name}_gix ON {schema}.{name} USING GIST (geom);
              '''
            engine.execute(sql)
        if osm:          
            if str(data).startswith('query:'):
                query = data.split(':')[1]
                sql = f'''
                       DROP TABLE IF EXISTS {schema}.{name};
                       CREATE TABLE IF NOT EXISTS {schema}.{name} AS 
                       SELECT (row_number() over())::int oid,
                              'custom query' AS "data",
                              a.* 
                         FROM {query};
                       '''
                engine.execute(sql)
                dest_condition = query
            else:
                dest_condition = []
                for condition in ['AND','OR','NOT']:
                # for condition in df_osm_dest[df_osm_dest['destination']==destination]['condition'].unique():
                    # print(condition)
                    if condition == 'AND':
                        clause = ' AND '.join(df_osm[(df_osm['destination']==name)&(df_osm['condition']=='AND')].apply(lambda x: "{} IS NOT NULL".format(x.key) if x.value=='NULL' else "{} = '{}'".format(x.key,x.value),axis=1).values.tolist())
                        dest_condition.append(clause)
                    if condition == 'OR':
                        clause = ' OR '.join(df_osm[(df_osm['destination']==name)&(df_osm['condition']=='OR')].apply(lambda x: "{} IS NOT NULL".format(x.key) if x.value=='NULL' else "{} = '{}'".format(x.key,x.value),axis=1).values.tolist())
                        dest_condition.append(clause)
                    if condition != 'NOT':
                        clause = ' AND '.join(df_osm[(df_osm['destination']==name)&(df_osm['condition']=='NOT')].apply(lambda x: "{} IS NOT NULL".format(x.key) if x.value=='NULL' else "{} != '{}' OR access IS NULL".format(x.key,x.value),axis=1).values.tolist())
                        dest_condition.append(clause)
                dest_condition = [x for x in dest_condition if x!='']
                # print(len(dest_condition))
                if len(dest_condition)==1:
                    dest_condition = dest_condition[0]
                else:
                    dest_condition = '({})'.format(') AND ('.join(dest_condition))
                # print(dest_condition)
                sql = f'''
                  DROP TABLE IF EXISTS {schema}.{name};
                  CREATE TABLE {schema}.{name} AS
                  SELECT (row_number() over())::int oid,
                         osm_id,
                         "data",
                         geom
                  FROM
                  (SELECT * FROM
                    (SELECT osm_id,
                            '{osm_prefix}_point' AS data,
                            geom
                       FROM {osm_prefix}_point d WHERE {dest_condition}) point
                     UNION
                    (SELECT osm_id,
                            '{osm_prefix}_polygon' AS data,
                            ST_Centroid(d.geom)
                       FROM {osm_prefix}_polygon d WHERE {dest_condition})
                   ORDER BY data, osm_id) t
                   ;
                '''
                # print(sql)
                engine.execute(sql)
            # insert destinations from potentially different sources into combined table
            sql = f'''
                INSERT INTO {schema}.{destination} (name, oid, geom)
                SELECT '{name}',oid, d.geom
                FROM {schema}.{name} d
                ON CONFLICT (name,oid) DO NOTHING;
            '''
            engine.execute(sql)
            # catalogue destinations from this data source
            sql = f'''SELECT count(*) FROM {schema}.{name};'''
            count = engine.execute(sql).fetchone()[0]
            sql = f'''
                INSERT INTO destination_catalog (destination,name,domain,count,data)
                SELECT '{destination}' AS destination,
                       '{name}'        AS name,
                       '{domain}'      AS domain,
                        {count}        AS count,
                        data || $$:{dest_condition}$$ AS data
                FROM {schema}.{name}
                GROUP BY destination, name, data, domain
                ON CONFLICT (destination, name, data) DO NOTHING;
            '''
            engine.execute(sql)
            print(f"{destination:25} {name:25} {count:=10d}")
            sql = f'''
              CREATE INDEX IF NOT EXISTS {name}_idx ON {schema}.{name} (oid);
              CREATE INDEX IF NOT EXISTS {name}_gix ON {schema}.{name} USING GIST (geom);
              '''
            engine.execute(sql)
        sql = f'''
          CREATE INDEX IF NOT EXISTS {destination}_idx ON {schema}.{destination} (oid);
          CREATE INDEX IF NOT EXISTS {destination}_gix ON {schema}.{destination} USING GIST (geom);
          '''
        engine.execute(sql)
    engine.execute(grant_query)
    # output to completion log    
    script_running_log(script, task, start, locale)
    engine.dispose()
        
if __name__ == '__main__':
    main()
    