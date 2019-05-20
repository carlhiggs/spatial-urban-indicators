# Purpose: Create hex grid and sample points
# Author:  Carl Higgs
# Date:    20190520

import time
from sqlalchemy import create_engine
import psycopg2
from script_running_log import script_running_log

# Import custom variables for National Liveability indicator process
from _project_setup import *

# simple timer for log file
start = time.time()
script = os.path.basename(sys.argv[0])
task = 'Create hex grid and sample points'

conn = psycopg2.connect(database=db, user=db_user, password=db_pwd, host=db_host,port=db_port)
curs = conn.cursor()

engine = create_engine("postgresql://{user}:{pwd}@{host}/{db}".format(user = db_user,
                                                                      pwd  = db_pwd,
                                                                      host = db_host,
                                                                      db   = db))      

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
engine.execute(sql.replace('%','%%'))

# create hexes with some additional offsetting to ensure complete study region coverage
sql = '''
DROP TABLE IF EXISTS {hex_grid};           
CREATE TABLE {hex_grid} AS
SELECT row_number() OVER () AS hex_id, geom
  FROM (
  SELECT hex_grid({hex_area_km2}, 
                  ST_XMin(geom)-{hex_buffer}, 
                  ST_YMin(geom)-{hex_buffer}, 
                  ST_XMax(geom)+{hex_buffer}, 
                  ST_YMax(geom)+{hex_buffer}, 
                  {srid}, 
                  {srid}, 
                  {srid}) geom, geom AS old_geom
FROM bangkok_thailand_2018_10000m) t
WHERE ST_Intersects(geom,old_geom);
CREATE UNIQUE INDEX {hex_grid}_idx ON {hex_grid} (hex_id);
CREATE INDEX {hex_grid}_geom_idx ON {hex_grid} USING GIST (geom);
'''.format(hex_grid = hex_grid,
           hex_area_km2 = hex_area_km2,
           srid = srid,
           hex_buffer = hex_buffer)           
engine.execute(sql)

sql = '''
DROP TABLE IF EXISTS {hex_grid_buffer};           
CREATE TABLE {hex_grid_buffer} AS
SELECT hex_id, 
       ST_Buffer(geom,{hex_buffer}) AS geom
  FROM {hex_grid};
CREATE UNIQUE INDEX {hex_grid_buffer}_idx ON {hex_grid_buffer} (hex_id);
CREATE INDEX {hex_grid_buffer}_geom_idx ON {hex_grid_buffer} USING GIST (geom);
'''.format(hex_grid = hex_grid,
           hex_grid_buffer = hex_grid_buffer,
           hex_buffer = hex_buffer)           
engine.execute(sql)

# Create sample points
print("Create sample points at regular intervals along the network... ")
if table_exists(points) is False:
    sql = '''
    CREATE TABLE {points} AS
    WITH line AS 
            (SELECT
                ogc_fid,
                (ST_Dump(ST_Transform(geom,32647))).geom AS geom
            FROM edges),
        linemeasure AS
            (SELECT
                ogc_fid,
                ST_AddMeasure(line.geom, 0, ST_Length(line.geom)) AS linem,
                generate_series(0, ST_Length(line.geom)::int, {interval}) AS metres
            FROM line),
        geometries AS (
            SELECT
                ogc_fid,
                metres,
                (ST_Dump(ST_GeometryN(ST_LocateAlong(linem, metres), 1))).geom AS geom 
            FROM linemeasure)
    SELECT
        row_number() OVER() AS point_id,
        ogc_fid,
        metres,
        ST_SetSRID(ST_MakePoint(ST_X(geom), ST_Y(geom)), {srid}) AS geom
    FROM geometries;
    CREATE UNIQUE INDEX {points}_idx ON {points} (point_id);
    CREATE INDEX {points}_geom_idx ON {points} USING GIST (geom);
    '''.format(points = points,
               interval = point_sampling_interval,
               srid = srid)  
    engine.execute(sql)      
    engine.execute(grant_query)      
    print("  - Sampling points table {} created with sampling at every {} metres along the pedestrian network.".format(points,point_sampling_interval))
else:
    print("  - It appears that sample points table {} have already been prepared for this region.".format(points))  
    
print("Associate sample points with overlay polygons (e.g. administrative boundaries, and hexagons for processing)")

for table_id_tuple in [[hex_grid,"hex_id"],[areas[0]['name_s'],areas[0]['id']]]:
    sql = '''
        ALTER TABLE {points} ADD COLUMN IF NOT EXISTS "{id}" text;
        UPDATE {points} p
            SET "{id}" = a."{id}"
            FROM {table} a
            WHERE ST_Intersects(p.geom,a.geom);
    '''.format(points = points,
               table = table_id_tuple[0],
               id = table_id_tuple[1])
    engine.execute(sql)

# grant access to the tables just created
engine.execute(grant_query)

# output to completion log					
script_running_log(script, task, start, locale)

engine.close()