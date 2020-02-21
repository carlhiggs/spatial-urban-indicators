"""

Create sample points and hex grid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    Script:  05_create_sample_points.py
    Purpose: Create hex grid and sample points
    Authors: Carl Higgs

"""

import time
from sqlalchemy import create_engine
import psycopg2
from script_running_log import script_running_log

# Import custom variables for National Liveability indicator process
from _project_setup import *

def main():
    # simple timer for log file
    start = time.time()
    script = os.path.basename(sys.argv[0])
    task = 'Create hex grid and sample points'
    
    engine = create_engine("postgresql://{user}:{pwd}@{host}/{db}".format(user = db_user,
                                                                          pwd  = db_pwd,
                                                                          host = db_host,
                                                                          db   = db))      
     
    conn = engine.connect()
    if not engine.has_table(hex_grid):
        # Create hex grid using algorithm from Hugh Saalmans (@minus34) under Apache 2 licence
        # https://github.com/minus34/postgis-scripts/blob/master/hex-grid/create-hex-grid-function.sql
        sql = '''
        --------------------------------------------------------------------------------------------------------------------------------
        -- HEX GRID - Create function
        --------------------------------------------------------------------------------------------------------------------------------
        --
        -- Hugh Saalmans (@minus34)
        -- 2015/04/10
        --
        -- DESCRIPTION:
        -- 
        -- Function returns a grid of mathmatically correct hexagonal polygons.
        -- Useful for hexbinning (the art of mapping clusters of information unbiased by political/historical/statistical boundaries).
        --
        -- INPUT
        --
        --   areakm2     : area of each hexagon in square km.
        --                   - note: hexagon size can be off slightly due to coordinate rounding in the calcs.
        --
        --   xmin, ymin  : min coords of the grid extents.
        --
        --   xmax, ymax  : max coords of the grid extents.
        --
        --   inputsrid   : the coordinate system (SRID) of the input min/max coords.
        --
        --   workingsrid : the SRID used to process the polygons.
        --                   - SRID must be a projected coord sys (i.e. in metres) as the calcs require ints. Degrees are out.
        --                   - should be an equal area SRID such as Albers or Lambert Azimuthal (e.g. Australia = 3577, US = 2163).
        --                   - using Mercator will NOT return hexagons of equal area due to its distortions (don't try it in Greenland).
        --
        --   ouputsrid   : the SRID of the output polygons.
        --
        -- NOTES
        --
        --   Hexagon height & width are rounded up & down to the nearest metre, hence the area may be off slightly.
        --   This is due to the Postgres generate_series function which doesn't support floats.
        --
        --   Why are my areas wrong in QGIS, MapInfo, etc...?
        --      Let's assume you created WGS84 lat/long hexagons, you may have noticed the areas differ by almost half in a desktop GIS
        --      like QGIS or MapInfo Pro. This is due to the way those tools display geographic coordinate systems like WGS84 lat/long.
        --      Running the following query in PostGIS will confirm the min & max sizes of your hexagons (in km2):
        --
        --         SELECT (SELECT (MIN(ST_Area(geom::geography, FALSE)) / 1000000.0)::numeric(10,3) From my_hex_grid) AS minarea,
        --               (SELECT (MAX(ST_Area(geom::geography, FALSE)) / 1000000.0)::numeric(10,3) From my_hex_grid) AS maxarea;
        --
        --   Hey, why doesn't the grid cover the area I defined using my min/max extents?
        --      Assuming you used lat/long extents and processed the grid with an equal area projection, the projection caused your
        --      min/max coords to describe a conical shape, not a rectangular one - and the conical area didn't cover everything you
        --      wanted to include.  See au-hex-grid.png as an example of this.
        --      If you're bored - learn why projections distort maps here: http://www.icsm.gov.au/mapping/about_projections.html
        --
        --   This code is based on this PostGIS Wiki article: https://trac.osgeo.org/postgis/wiki/UsersWikiGenerateHexagonalGrid
        --
        --   Dimension calcs are based on formulae from: http://hexnet.org/content/hexagonal-geometry
        --
        -- LICENSE
        --
        -- This work is licensed under the Apache License, Version 2: https://www.apache.org/licenses/LICENSE-2.0
        --
        --------------------------------------------------------------------------------------------------------------------------------
        
        --DROP FUNCTION IF EXISTS hex_grid(areakm2 FLOAT, xmin FLOAT, ymin FLOAT, xmax FLOAT, ymax FLOAT, inputsrid INTEGER,
        --  workingsrid INTEGER, ouputsrid INTEGER);
        CREATE OR REPLACE FUNCTION hex_grid(areakm2 FLOAT, xmin FLOAT, ymin FLOAT, xmax FLOAT, ymax FLOAT, inputsrid INTEGER,
          workingsrid INTEGER, ouputsrid INTEGER)
          RETURNS SETOF geometry AS
        $BODY$
        
        DECLARE
          minpnt GEOMETRY;
          maxpnt GEOMETRY;
          x1 INTEGER;
          y1 INTEGER;
          x2 INTEGER;
          y2 INTEGER;
          aream2 FLOAT;
          qtrwidthfloat FLOAT;
          qtrwidth INTEGER;
          halfheight INTEGER;
        
        BEGIN
        
          -- Convert input coords to points in the working SRID
          minpnt = ST_Transform(ST_SetSRID(ST_MakePoint(xmin, ymin), inputsrid), workingsrid);
          maxpnt = ST_Transform(ST_SetSRID(ST_MakePoint(xmax, ymax), inputsrid), workingsrid);
        
          -- Get grid extents in working SRID coords
          x1 = ST_X(minpnt)::INTEGER;
          y1 = ST_Y(minpnt)::INTEGER;
          x2 = ST_X(maxpnt)::INTEGER;
          y2 = ST_Y(maxpnt)::INTEGER;
        
          -- Get height and width of hexagon - FLOOR and CEILING are used to get the hexagon size closer to the requested input area
          aream2 := areakm2 * 1000000.0;
          qtrwidthfloat := sqrt(aream2/(sqrt(3.0) * (3.0/2.0))) / 2.0;
          
          qtrwidth := FLOOR(qtrwidthfloat);
          halfheight := CEILING(qtrwidthfloat * sqrt(3.0));
        
          -- Return the hexagons - done in pairs, with one offset from the other
          RETURN QUERY (
            SELECT ST_Transform(ST_SetSRID(ST_Translate(geom, x_series::FLOAT, y_series::FLOAT), workingsrid), ouputsrid) AS geom
              FROM generate_series(x1, x2, (qtrwidth * 6)) AS x_series,
                   generate_series(y1, y2, (halfheight * 2)) AS y_series,
                   (
                     SELECT ST_GeomFromText(
                       format('POLYGON((0 0, %s %s, %s %s, %s %s, %s %s, %s %s, 0 0))',
                         qtrwidth, halfheight,
                         qtrwidth * 3, halfheight,
                         qtrwidth * 4, 0,
                         qtrwidth * 3, halfheight * -1,
                         qtrwidth, halfheight * -1
                       )
                     ) AS geom
                     UNION
                     SELECT ST_Translate(
                       ST_GeomFromText(
                         format('POLYGON((0 0, %s %s, %s %s, %s %s, %s %s, %s %s, 0 0))',
                           qtrwidth, halfheight,
                           qtrwidth * 3, halfheight,
                           qtrwidth * 4, 0,
                           qtrwidth * 3, halfheight * -1,
                           qtrwidth, halfheight * -1
                         )
                       )
                     , qtrwidth * 3, halfheight) as geom
                   ) AS two_hex);
        
        END$BODY$
          LANGUAGE plpgsql VOLATILE
          COST 100;
        '''
        engine.execute(sql)
        
        # create hexes with some additional offsetting to ensure complete study region coverage
        sql = '''
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
        FROM {study_region}) t
        WHERE ST_Intersects(geom,old_geom);
        CREATE UNIQUE INDEX IF NOT EXISTS {hex_grid}_idx ON {hex_grid} (hex_id);
        CREATE INDEX IF NOT EXISTS {hex_grid}_geom_idx ON {hex_grid} USING GIST (geom);
        '''.format(hex_grid = hex_grid,
                   hex_area_km2 = hex_area_km2,
                   study_region = buffered_study_region,
                   srid = srid,
                   hex_buffer = hex_buffer)       
        
        engine.execute(sql)     
    else:
        print("  - The table {} has already been processed.".format(hex_grid)) 

    if not engine.has_table(hex_grid_buffer):
        sql = '''
        CREATE TABLE IF NOT EXISTS {hex_grid_buffer} AS
        SELECT hex_id, 
               ST_Buffer(geom,{hex_buffer}) AS geom
          FROM {hex_grid};
        CREATE UNIQUE INDEX IF NOT EXISTS {hex_grid_buffer}_idx ON {hex_grid_buffer} (hex_id);
        CREATE INDEX IF NOT EXISTS {hex_grid_buffer}_geom_idx ON {hex_grid_buffer} USING GIST (geom);
        '''.format(hex_grid = hex_grid,
                   hex_grid_buffer = hex_grid_buffer,
                   hex_buffer = hex_buffer)           
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
