"""

Create sample points and hex grid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Script:  
    05_create_sample_points.py
Purpose: 
    Create hex grid and sample points
Authors: 
    Carl Higgs

"""

import time
from sqlalchemy import create_engine
import psycopg2
from script_running_log import script_running_log

# Import custom variables for liveability indicator process
from _project_setup import *

def main():
    # simple timer for log file
    start = time.time()
    script = os.path.basename(sys.argv[0])
    task = 'Create hex grid and sample points'
    
    conn = psycopg2.connect(database=db, user=db_user, password=db_pwd, host=db_host,port=db_port)
    curs = conn.cursor()
    
    engine = create_engine(f"postgresql://{db_user}:{db_pwd}@{db_host}/{db}")
    if not engine.has_table(hex_grid):
        # Create hex grid using algorithm from Hugh Saalmans (@minus34) under Apache 2 licence
        # https://github.com/minus34/postgis-scripts/blob/master/hex-grid/create-hex-grid-function.sql
        curs.execute(hex_function)
        conn.commit()
        
        # create hexes with some additional offsetting to ensure complete study region coverage
        sql = f'''
        CREATE TABLE IF NOT EXISTS {hex_grid} AS
        SELECT row_number() OVER () AS hex_id, geom
          FROM (
          SELECT hex_grid({hex_area_km2}::float, 
                          ST_XMin(geom)-{hex_buffer}, 
                          ST_YMin(geom)-{hex_buffer}, 
                          ST_XMax(geom)+{hex_buffer}, 
                          ST_YMax(geom)+{hex_buffer}, 
                          {srid}, 
                          {srid}, 
                          {srid}) geom, geom AS old_geom
        FROM {buffered_study_region}) t
        WHERE ST_Intersects(geom,old_geom);
        CREATE UNIQUE INDEX IF NOT EXISTS {hex_grid}_idx ON {hex_grid} (hex_id);
        CREATE INDEX IF NOT EXISTS {hex_grid}_geom_idx ON {hex_grid} USING GIST (geom);
        '''
        engine.execute(sql)     
    else:
        print("  - The table {} has already been processed.".format(hex_grid)) 

    if not engine.has_table(hex_grid_buffer):
        sql = f'''
        CREATE TABLE IF NOT EXISTS {hex_grid_buffer} AS
        SELECT hex_id, 
               ST_Buffer(geom,{hex_buffer}) AS geom
          FROM {hex_grid};
        CREATE UNIQUE INDEX IF NOT EXISTS {hex_grid_buffer}_idx ON {hex_grid_buffer} (hex_id);
        CREATE INDEX IF NOT EXISTS {hex_grid_buffer}_geom_idx ON {hex_grid_buffer} USING GIST (geom);
        '''         
        engine.execute(sql)
    else:
        print("  - The table {} has already been processed.".format(hex_grid_buffer)) 

    if not engine.has_table(points):  
        # Create sample points
        print("  - Create sample points at regular intervals along the network, if not already existing... "),
        linkage_table = areas[analysis_scale]['table']
        sql = f'''
        CREATE TABLE IF NOT EXISTS {points} AS
        WITH line AS 
                (SELECT
                    ogc_fid,
                    (ST_Dump(ST_Transform(geom,{srid}))).geom AS geom
                FROM edges),
            linemeasure AS
                (SELECT
                    ogc_fid,
                    ST_AddMeasure(line.geom, 0, ST_Length(line.geom)) AS linem,
                    generate_series(0, ST_Length(line.geom)::int, {point_sampling_interval}) AS metres
                FROM line),
            geometries AS (
                SELECT
                    ogc_fid,
                    metres,
                    (ST_Dump(ST_GeometryN(ST_LocateAlong(linem, metres), 1))).geom AS geom
                FROM linemeasure),
            sampling_points AS (
                SELECT
                    row_number() OVER() AS point_id,
                    {area_analysis},
                    ogc_fid,
                    metres,
                    ST_SetSRID(ST_MakePoint(ST_X(geometries.geom), ST_Y(geometries.geom)), {srid}) AS geom
                FROM geometries
                LEFT JOIN {linkage_table} ON ST_Intersects(geometries.geom,{linkage_table}.geom)
                WHERE  ST_Intersects(geometries.geom,{linkage_table}.geom)
                ),
            networked_points AS (
                SELECT  s.point_id,         
                        s.{area_analysis},
                        s.ogc_fid edge_ogc_fid,   
                        s.metres,
                        "from" n1,               
                        "to" n2,     
                        e.geom AS edge_geom,
                        ST_LineLocatePoint(e.geom, n1.geom) llp1,
                        ST_LineLocatePoint(e.geom, s.geom) llpm,
                        ST_LineLocatePoint(e.geom, n2.geom) llp2,
                        s.geom
                FROM sampling_points s
                LEFT JOIN edges e  ON s.ogc_fid = e.ogc_fid
                LEFT JOIN nodes n1 ON e."from" = n1.osmid
                LEFT JOIN nodes n2 ON e."to" = n2.osmid
                )
        SELECT t.point_id,        
               t.{area_analysis}, 
               t.edge_ogc_fid,   
               t.metres,
               t.n1,               
               t.n2,               
               ST_Length(ST_LineSubstring(t.edge_geom, LEAST(t.llp1,t.llpm),GREATEST(t.llp1,t.llpm)))::int n1_distance,
               ST_Length(ST_LineSubstring(t.edge_geom, LEAST(t.llp2,t.llpm),GREATEST(t.llp2,t.llpm)))::int n2_distance,
               t.geom             
        FROM networked_points t
        ;
        CREATE UNIQUE INDEX IF NOT EXISTS {points}_ix ON {points} (point_id);
        CREATE INDEX IF NOT EXISTS {points}_edge_ogc_fid_idx ON {points} (edge_ogc_fid);
        CREATE INDEX IF NOT EXISTS {points}_n1_idx ON {points} (n1);
        CREATE INDEX IF NOT EXISTS {points}_n2_idx ON {points} (n2);
        CREATE INDEX IF NOT EXISTS {points}_gix ON {points} USING GIST (geom);
        COMMENT ON TABLE {points} IS 'Sampling points created every {point_sampling_interval}m along network, where not located within areas of open space.';
        COMMENT ON COLUMN {points}.point_id     IS 'Unique identifier';
        COMMENT ON COLUMN {points}.edge_ogc_fid IS 'Unique identifier for OSM network edge segment associated with this sample point';
        COMMENT ON COLUMN {points}.metres       IS 'Distance from start of line at which the point was created';
        COMMENT ON COLUMN {points}.n1           IS 'OSM ID for origin node of network edge';
        COMMENT ON COLUMN {points}.n2           IS 'OSM ID for terminal node of network edge';
        COMMENT ON COLUMN {points}.n1_distance  IS 'Distance (m) of sample point from network edge origin node';
        COMMENT ON COLUMN {points}.n2_distance  IS 'Distance (m) of sample point from network edge terminal node';
        COMMENT ON COLUMN {points}.geom         IS 'Point geometry in SRID {srid}';
        ''' 
        engine.execute(sql)             
        print("Sampling points table {} created with sampling at every {} metres along the pedestrian network.".format(points,point_sampling_interval))
    else:
        print("  - The table {} has already been processed.".format(points)) 
    
    print('Delete any sampling points which were created within the bounds of areas of open space...')
    sql = f'''
    DELETE FROM {points} p
    USING open_space_areas o
    WHERE ST_Intersects(o.geom,p.geom);
    '''
    engine.execute(sql)

    print('Create simplified views of origins pooling the nodes and distances into single column...')
    if not engine.has_table('origins'):
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
    
    # grant access to the tables just created
    engine.execute(grant_query)
    # output to completion log					
    script_running_log(script, task, start, locale)
    engine.dispose() 

if __name__ == '__main__':
    main()
