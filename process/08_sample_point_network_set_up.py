"""

Set up sample points for network analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

import networkx as nx
import time 
import numpy as np
from sqlalchemy import create_engine

from _project_setup import *

from script_running_log import script_running_log

connection = f"postgresql://{db_user}:{db_pwd}@{db_host}/{db}"

def main():
    # simple timer for log file
    start = time.time()
    script = os.path.basename(sys.argv[0])
    task = 'Set up sample points for network analysis'
    engine = create_engine(connection)
    conn = engine.connect()
    
    print('Delete any sampling points which were created within the bounds of areas of open space...')
    sql = f'''
    DELETE FROM {points} p
    USING open_space_areas o
    WHERE ST_Intersects(o.geom,p.geom);
    '''
    engine.execute(sql)
    print('Create new columns and indices for sampling point edge and node relations...')
    required_field = 'edge_ogc_fid'
    sql = f'''
    SELECT column_name 
    FROM information_schema.columns 
    WHERE table_name='{points}' and column_name='{required_field}';
    '''
    result = conn.execute(sql)
    if len([r for r in result])==0:
        now = time.strftime('%Y%m%d_%H%M')
        sql = f'''
        -- This full query took just over 30 seconds for Bangkok (1472479 sampling points)
        DROP TABLE IF EXISTS sampling_temp;
        CREATE TABLE sampling_temp AS
        SELECT point_id,         
               edge_ogc_fid,   
               metres,
               n1,               
               n2,               
               ST_Length(ST_LineSubstring(t.edge_geom, LEAST(t.llp1,t.llpm),GREATEST(t.llp1,t.llpm)))::int n1_distance,
               ST_Length(ST_LineSubstring(t.edge_geom, LEAST(t.llp2,t.llpm),GREATEST(t.llp2,t.llpm)))::int n2_distance,
               t.geom             
        FROM (
            SELECT  s.point_id,         
                    s.ogc_fid edge_ogc_fid,   
                    s.metres,
                    "from" n1,               
                    "to" n2,     
                    e.geom AS edge_geom,
                    ST_LineLocatePoint(e.geom, n1.geom) llp1,
                    ST_LineLocatePoint(e.geom, s.geom) llpm,
                    ST_LineLocatePoint(e.geom, n2.geom) llp2,
                    s.geom
            FROM {points} s
            LEFT JOIN edges e  ON s.ogc_fid = e.ogc_fid
            LEFT JOIN nodes n1 ON e."from" = n1.osmid
            LEFT JOIN nodes n2 ON e."to" = n2.osmid
            ) t;
        DROP TABLE {points};
        ALTER TABLE sampling_temp RENAME TO {points};
        CREATE UNIQUE INDEX IF NOT EXISTS {points}_ix ON {points} (point_id);
        CREATE INDEX IF NOT EXISTS {points}_edge_ogc_fid_idx ON {points} (edge_ogc_fid);
        CREATE INDEX IF NOT EXISTS {points}_n1_idx ON {points} (n1);
        CREATE INDEX IF NOT EXISTS {points}_n2_idx ON {points} (n2);
        CREATE INDEX IF NOT EXISTS {points}_gix ON {points} USING GIST (geom);
        COMMENT ON TABLE origins IS 'Sampling points created every {point_sampling_interval}m along network, where not located within areas of open space.';
        COMMENT ON COLUMN origins.s_node_distance    IS 'Distance (m) from sample point to network node with shortest distance to destination';
        COMMENT ON COLUMN origins.point_id     IS 'Unique identifier';
        COMMENT ON COLUMN origins.edge_ogc_fid IS 'Unique identifier for OSM network edge segment associated with this sample point';
        COMMENT ON COLUMN origins.metres       IS 'Distance from start of line at which the point was created';
        COMMENT ON COLUMN origins.n1           IS 'OSM ID for origin node of network edge';
        COMMENT ON COLUMN origins.n2           IS 'OSM ID for terminal node of network edge';
        COMMENT ON COLUMN origins.n1_distance  IS 'Distance (m) of sample point from network edge origin node';
        COMMENT ON COLUMN origins.n2_distance  IS 'Distance (m) of sample point from network edge terminal node';
        COMMENT ON COLUMN origins.geom         IS 'Point geometry in SRID {srid}';
        '''
        engine.execute(sql)
        
    print('Create simplified views of origins pooling the nodes and distances into single column...')
    now = time.strftime('%Y%m%d_%H%M')
    sql = f'''
    CREATE TABLE IF NOT EXISTS origins AS
    SELECT DISTINCT ON (point_id, s_node)
           s.point_id, 
           edge_ogc_fid,
           v.s_node, 
           v.s_node_distance
    from {points} s
      cross join lateral (
          values 
            (n1, n1_distance), 
            (n2, n2_distance)
      ) as v(s_node, s_node_distance)
    ORDER BY point_id, s_node, s_node_distance ASC;
    CREATE INDEX IF NOT EXISTS origins_ix ON origins (point_id);
    CREATE INDEX IF NOT EXISTS origins_edge_ix ON origins (edge_ogc_fid);
    CREATE INDEX IF NOT EXISTS origins_node_idx ON origins (s_node);
    COMMENT ON TABLE origins IS 'Created {now}: Long-form table of sample points associated with two closest nodes and their respective distances (any particular sample point would be expected to be associated with two nearest nodes, hence will be included on two rows).';
    '''
    engine.execute(sql)
    # output to completion log    
    script_running_log(script, task, start, locale)
    engine.dispose()
        
if __name__ == '__main__':
    main()