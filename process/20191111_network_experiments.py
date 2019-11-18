'''
Sketch of example for python based network analysis using an OSMnx derived graphml file

Assumptions
    - sample points (origins) 
        - are located along network
        - not necessarily coincident with nodes
        - associated with an OSM edge id (which is actually ogc_fid, created when importing to sql database)
        - TO DO: 
            - ensure each sample point is associated with edge 'from' and 'to' and their respective (Euclidean) distances from sample point
    - destination points are arbitrarily located, not necessarily along the network nor coincident with nodes
        - TO DO: 
            - ensure each destination is associated with closest edge, and in turn the 'from' and 'to' nodes and their respective (Euclidean) distances from destination point
    - edges (road network segments)
        - have ogc_fid as primary key
        - have the fields 'from' and 'to' which identify the respective terminal nodes for each edge segment
        
        


Idea: 
 -- calculate and store the distances to the two nearest nodes (node pairs) on edges for all sample point origins
 -- calculate and store the nearest node (D-nodes) and euclidean distance to this for each destination
 -- compute distances to all nodes within 3200m from all associated D-nodes
 -- for all origin-destination combinations
        - evaluate: do the O and D share an edge?  
            - If so: take Euclidean distance between these (they are close, and a straight line representation is most likely adequate; alternative is to do a spatial operation)
            - else:
                - are any of the O-node-pairs in the list of D-node-pairs?
                    - if so: take D-node-pair - O-node-pair match with minimum distance, accounting for specific D offset
                    
Other thoughts:
-- Could perhaps use nodes and edges from OSMnx after all,
As per
    http://docs.pgrouting.org/latest/en/pgr_createVerticesTable.html#pgr-create-vert-table
Could use pgr_createVerticesTable() function supplying 'from' and 'to' as the pre-specified source and target -- would these be sufficient?

SELECT pgr_createVerticesTable(edge_table, the_geom, source, target, rows_where)
SELECT pgr_createVerticesTable(edges, geom, "from", "to")

If doing the above, even better may be just to formally rename "from" and "to" to source and target
so these no longer require the inverted commas!
'''

import networkx as nx
import time 
import numpy as np
import requests
import pandas as pd
import geopandas as gpd
import psycopg2
from sqlalchemy import create_engine
from multiprocessing import  Pool
from functools import partial

from _project_setup import *

connection = f"postgresql://{db_user}:{db_pwd}@{db_host}/{db}"

def load_networkx_graph(graphml):
    # Set up network for analysis with NetworkX
    print("Setting up network for analysis with NetworkX...")
    start_time = time.time()
    # read in network
    G = nx.read_graphml(graphml, node_type=str)
    # ensure it is interpreted as undirected; we want our pedestrians to walk in either direction
    G = nx.Graph(G)
    # # length is a string (why?!), required to be float
    for u,v,d in G.edges(data=True):
       d['length'] = float(d['length'])
    end_time = time.time()
    print("Network x graph set up in  {:.02f} minutes".format((end_time-start_time)/60))
    # For Bangkok: Network x graph set up in  .84 minutes
    return(G)

def create_local_nodes_dict(node,graph,table = 'local_node_distances', distance = 3200):
    # Calculate node relations, for subset of nodes leading to destinations
    local_node_distances = nx.single_source_dijkstra_path_length(graph, node, cutoff=distance, weight='length')
    df = pd.DataFrame([[node,d,int(local_node_distances[d])] for d in local_node_distances],columns = ['node','inode','distance']).set_index('node')
    return(df)

def parallelize_dataframe(id_list, func, n_cores=4,connection=connection):
    engine = create_engine(connection)
    divvy_load = math.ceil(len(id_list)/n_cores)
    pool = Pool(processes=n_cores)
    df = pd.concat(pool.map(func,id_list,divvy_load))
    pool.close()
    pool.join()
    df.to_sql('local_node_distances',engine,if_exists='append',index=True)
    
sql_queries = {
    'Create new columns and indices for sampling point edge and node relations':'''
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
        FROM sampling_points_30m s
        LEFT JOIN edges e  ON s.ogc_fid = e.ogc_fid
        LEFT JOIN nodes n1 ON e."from" = n1.osmid
        LEFT JOIN nodes n2 ON e."to" = n2.osmid
        ) t;
    DROP TABLE sampling_points_30m;
    ALTER TABLE sampling_temp RENAME TO sampling_points_30m;
    CREATE UNIQUE INDEX IF NOT EXISTS sampling_points_30m_ix ON sampling_points_30m (point_id);
    CREATE INDEX IF NOT EXISTS sampling_points_30m_edge_ogc_fid_idx ON sampling_points_30m (edge_ogc_fid);
    CREATE INDEX IF NOT EXISTS sampling_points_30m_n1_idx ON sampling_points_30m (n1);
    CREATE INDEX IF NOT EXISTS sampling_points_30m_n2_idx ON sampling_points_30m (n2);
    CREATE INDEX IF NOT EXISTS sampling_points_30m_gix ON sampling_points_30m USING GIST (geom);
    ''',
    'Record closest node and distance for destination points':'''
    -- took 2 seconds to run for Bangkok (10,047 destinations)
    CREATE MATERIALIZED VIEW IF NOT EXISTS destinations AS
    SELECT  o.dest_oid,
            o.osm_id,
            o.dest_name,
            o.dest_name_full,
            o.edge_ogc_fid,
            o.n1,
            o.n2,
            -- to determine length along a line, the origin must be located the lower proportion along the line,
            -- hence the least and greatest queries
            ST_Length(ST_LineSubstring(o.edge_geom, LEAST(llp1,llpm),GREATEST(llp1,llpm)))::int n1_distance,
            ST_Length(ST_LineSubstring(o.edge_geom, LEAST(llp2,llpm),GREATEST(llp2,llpm)))::int n2_distance,
                ST_Distance(geom,match_point_geom)::int match_point_distance,
            o.match_point_geom, 
            o.geom
    FROM
    (SELECT t.dest_oid,
            t.osm_id,
            t.dest_name,
            t.dest_name_full,
            t.geom,
            t.edge_ogc_fid,
            t.match_point_geom, 
            t.n1,
            t.n2,
            t.edge_geom,
            ST_LineLocatePoint(t.edge_geom, n1.geom) llp1,
            ST_LineLocatePoint(t.edge_geom, t.match_point_geom) llpm,
            ST_LineLocatePoint(t.edge_geom, n2.geom) llp2
    FROM 
    (SELECT d.dest_oid,
            d.osm_id,
            d.dest_name,
            d.dest_name_full,
            d.geom,
            e.geom edge_geom,
            e.edge_ogc_fid,
            ST_ClosestPoint(e.geom,d.geom) AS match_point_geom, 
            e.n1,
            e.n2    
    FROM osm_destinations d
    CROSS JOIN LATERAL (
        SELECT e.ogc_fid edge_ogc_fid, 
               e."from" n1, 
               e."to" n2,
               e.geom
        FROM edges e
        ORDER BY e.geom <-> d.geom 
        LIMIT 1
    ) e 
    ) t
    LEFT JOIN nodes n1 ON t.n1 = n1.osmid
    LEFT JOIN nodes n2 ON t.n2 = n2.osmid
    ) o;
    CREATE UNIQUE INDEX IF NOT EXISTS destinations_ix ON destinations (dest_oid);
    CREATE INDEX IF NOT EXISTS destinations_edge_ogc_fid_idx ON destinations (edge_ogc_fid);
    CREATE INDEX IF NOT EXISTS destinations_n1_idx ON destinations (n1);
    CREATE INDEX IF NOT EXISTS destinations_n2_idx ON destinations (n2);
    CREATE INDEX IF NOT EXISTS destinations_gix ON destinations USING GIST (geom);
    '''
    }

def main():
    # conn = psycopg2.connect(database=db, user=db_user, password=db_pwd)
    # curs = conn.cursor()
    engine = create_engine(connection)
    # for q in sql_queries:
        # print(f'\n{q}... ')
        # start_time = time.time()
        # curs.execute(sql_queries[q])
        # conn.commit()
        # end_time = time.time()
        # print("Completed in {} minutes.".format((end_time-start_time)/60))
        
    # conn.close()
    # load network graph
    graphml = os.path.join(locale_dir,f'{buffered_study_region}_pedestrian_{osm_prefix}.graphml')
    G = load_networkx_graph(graphml)
    for u,v,d in G.edges(data=True):
        d['length'] = int(d['length'])
        
    # nodes = list(G.nodes)
    # retrieve the distinct nodes used to access destinations
    # for Bangkok these are 11,716/353,206, or 3.32% of all nodes we need to consider
    # access within 3200 metres.
    table = 'local_node_distances'
    if engine.has_table(table):
        sql = f'''
            SELECT DISTINCT c_node node 
            FROM
              destinations CROSS JOIN LATERAL
                (VALUES(n1),(n2)) AS T(c_node)
            WHERE
              c_node IS NOT NULL
            AND NOT EXISTS
                (
                SELECT  NULL
                FROM    {table} r
                WHERE   r.node = c_node
                );
            '''
        distinct_destination_nodes = pd.read_sql(sql, engine)
    else:
        sql = '''
            SELECT DISTINCT node 
            FROM
              destinations CROSS JOIN LATERAL
                (VALUES(n1),(n2)) AS T(node)
            WHERE
              node IS NOT NULL;
            '''
        distinct_destination_nodes = pd.read_sql(sql, engine)
    
    nodes = distinct_destination_nodes.node.values.tolist()
    nrows = len(nodes)
    chunk_size = 100
    start_time = time.time()
    for x in range(0,nrows,chunk_size):
        x_end = x+chunk_size-1
        if x_end > nrows:
            x_end = nrows
        print(f"{x}:{x_end}")
        parallelize_dataframe(nodes[x:x_end],partial(create_local_nodes_dict,graph = G))
            
    end_time = time.time()
    mins = (end_time-start_time)/60
    rate = mins/nrows*100000
    print(f"Completed in {mins} minutes.")

# Set up output dataframe
# df = pd.DataFrame(list(G.nodes),columns=['node'])


sql = '''
-- Create simplified views of origins and destinations,
-- pooling the nodes and distances into single column.
-- This will make evaluation of full minimum distances
-- more straightforward.

DROP MATERIALIZED VIEW IF EXISTS origins;
CREATE MATERIALIZED VIEW origins AS
SELECT DISTINCT ON (point_id, s_node)
       s.point_id, 
       v.s_node, 
       v.s_node_distance
from sampling_points_30m s
  cross join lateral (
      values 
        (n1, n1_distance), 
        (n2, n2_distance)
  ) as v(s_node, s_node_distance)
ORDER BY point_id, s_node, s_node_distance ASC;
CREATE INDEX IF NOT EXISTS origins_ix ON origins (point_id);
CREATE INDEX IF NOT EXISTS origins_node_idx ON origins (s_node);

CREATE MATERIALIZED VIEW dests AS
SELECT DISTINCT ON (dest_oid, d_node)
       d.dest_oid,
       d.dest_name_full,
       v.d_node, 
       v.d_node_distance,
       d.match_point_distance,
       d_node_distance + match_point_distance AS d_full_distance
from destinations d
  cross join lateral (
      values 
        (n1, n1_distance), 
        (n2, n2_distance)
  ) as v(d_node, d_node_distance);
CREATE INDEX IF NOT EXISTS dests_ix ON dests (dest_oid);
CREATE INDEX IF NOT EXISTS dests_node_idx ON dests (d_node);

CREATE MATERIALIZED VIEW node_lookup AS
SELECT DISTINCT ON (node_osmid,pgr_node)
       v.node_osmid,
       v.pgr_node
from edges e
  cross join lateral (
      values 
        ("from", source), 
        ("to", target)
  ) as v(node_osmid, pgr_node);
CREATE INDEX IF NOT EXISTS edge_lookup_ix ON edge_lookup (node_osmid);
CREATE INDEX IF NOT EXISTS edge_lookup_node_idx ON edge_lookup (pgr_node);

-- ensure the destination match node is also indexed
CREATE INDEX IF NOT EXISTS local_node_distances_inode_idx ON local_node_distances (inode);

-- An example of distance to destination query, using the networkx derived network
DROP MATERIALIZED VIEW IF EXISTS test_local_od;
EXPLAIN ANALYZE
CREATE MATERIALIZED VIEW test_local_od AS
SELECT DISTINCT ON (point_id)
       s.point_id, 
       s.s_node, 
       s.s_node_distance, 
       d.dest_oid, 
       d.dest_name_full, 
       d.d_node, 
       d.d_full_distance, 
       l.node,
       l.inode, 
       l.distance AS node_distance,
       s_node_distance + d_full_distance + l.distance AS final_distance
FROM origins s
LEFT JOIN local_node_distances l 
       ON s.s_node = l.node
LEFT JOIN dests d 
       ON d.d_node = l.inode
WHERE dest_name_full = 'Supermarket' 
ORDER BY point_id,final_distance ASC 
LIMIT 10;
SELECT * FROM test_local_od;

DROP MATERIALIZED VIEW IF EXISTS local_node_distances_pgr;
EXPLAIN ANALYZE
CREATE MATERIALIZED VIEW local_node_distances_pgr AS
SELECT s.node_osmid AS s_node_osmid,
       t.node_osmid AS t_node_osmid,
       l.*
FROM local_network_3200m l
LEFT JOIN edge_lookup s ON s.pgr_node = l.from_v
LEFT JOIN edge_lookup t ON t.pgr_node = l.node
WHERE EXISTS 
    (SELECT 1
       FROM 
      dests d 
      WHERE d.d_node = t.node_osmid);
CREATE INDEX IF NOT EXISTS local_node_distances_pgr_source_ix ON local_node_distances_pgr (node);
CREATE INDEX IF NOT EXISTS local_node_distances_pgr_target_ix ON local_node_distances_pgr (node);
CREATE INDEX IF NOT EXISTS local_node_distances_pgr_node_ix ON local_node_distances_pgr (node);


DROP MATERIALIZED VIEW IF EXISTS test_local_od_pgr;
EXPLAIN ANALYZE
CREATE MATERIALIZED VIEW test_local_od_pgr AS
SELECT DISTINCT ON (point_id)
       s.point_id, 
       s.s_node, 
       s.s_node_distance, 
       d.dest_oid, 
       d.dest_name_full, 
       d.d_node, 
       d.d_full_distance, 
       l.s_node node,
       l.t_node inode, 
       l.agg_cost AS node_distance,
       s_node_distance + d_full_distance + l.agg_cost AS final_distance
FROM origins s
LEFT JOIN local_node_distances_pgr l 
       ON s.s_node = l.s_node_osmid
RIGHT JOIN dests d 
       ON d.d_node = l.t_node_osmid
WHERE dest_name_full = 'Supermarket' 
  AND d_node IS NOT NULL
ORDER BY point_id,final_distance ASC 
LIMIT 10;
SELECT * FROM test_local_od_pgr;


'''

    
# Sausage buffer
# sb = nx.ego_graph(G, node, radius=1600, center=True, undirected=True, distance='length')
# Turns out, ego graph is just basic Dijkstra implementation; we could do better
# https://github.com/networkx/networkx/blob/aeeeef92f2229b0cc8ebbbbfcfc87128f546d55f/networkx/generators/ego.py
# Eg multi source, 1600m threshold, not directed

# further idea for checking edges in subgraph based on nodes, using sql results of local_nodes_distances:
# SELECT ogc_fid FROM edges WHERE '5862588417' IN ("from","to")
# CREATE TABLE test_sb AS 
#    SELECT node, 
#           ST_UNION(geom) geom 
#      FROM local_nodes_distances l, 
#           edges e 
#     WHERE l.distance <=1600 AND l.inode IN (e."from",e."to") 
#     GROUP BY node;
#
# Or more practically using hexes

if __name__ == '__main__':
    main()

# # each node will be associated with a dictionary of nodes it has access to within 3200m: e.g.
# # {5862588417: 0, 5862588435: 30.08, 5862588428: 43.661, 5862588436: 64.52, 5862588433: 69.287,
# # ...
# # 3706489893: 3195.013, 5668591342: 3195.336999999999, 5668591359: 3197.7199999999993, 1688538955: 3197.8099999999986}
# # 
# # with data structure looking like:
# #           node                                        local_3200m
# # 0   5862588417  {5862588417: 0, 5862588435: 30.08, 5862588428:...
# # 1   5862588419  {5862588419: 0, 5862588424: 36.77, 5862588421:...
# # 2   5862588420  {5862588420: 0, 5862588419: 140.418, 586258842...
# # 3   5862588421  {5862588421: 0, 5862588419: 38.107, 5862588424...
# # 4   5862588422  {5862588422: 0, 5862588424: 3.999, 5862588426:...
# # ..         ...                                                ...
# # 95  5898240371  {5898240371: 0, 5898240372: 29.795, 5898240382...
# # 96  5898240372  {5898240372: 0, 5898240371: 29.795, 5898240382...
# # 97  1199571317  {1199571317: 0, 1199571300: 112.81, 1112995534...
# # 98  5935989109  {5935989109: 0, 5935989119: 52.557, 5942232342...
# # 99  5898240373  {5898240373: 0, 5898240382: 28.829, 5898240372...
# 
# test_n = [5862588417,5862588419,5862588420,5862588421,5862588422]
# test_l = [{5862588417: 0, 5862588435: 30.08, 5862588428:380},
#         {5862588419: 0, 5862588424: 36.77, 5862588421:498},
#         {5862588420: 0, 5862588419: 140.418, 586258842:46499},
#         {5862588421: 0, 5862588419: 38.107, 5862588424:121},
#         {5862588422: 0, 5862588424: 3.999, 5862588426:51}]
# df = pd.DataFrame(list(zip(test_n, test_l)), 
#                columns =['node', 'local_3200m']) 
# df 
# 
# 
# # keys, values = zip(*((k, v) for d in dicts for k, v in d.items()))
# # new_data = {'id': ids, 'metric': metrics, 'keys': keys, 'values': values}
# # new_df = pd.DataFrame.from_dict(new_data)
# 
# final_df = pd.DataFrame()
# 
# for row in df.iterrows():
#     i = row[1][0]           # get the id value
#     for key, value in row[1][1].items():
#         tmp_df = pd.DataFrame({
#             'node':i,
#             'inode': key,
#             'distance': value
#         }, index=[0])
#         final_df = final_df.append(tmp_df) # append the tmp_df to our final df
# 
# final_df.reset_index(drop=True) 
# 
# 
# So the idea could be to process this in chunks outputting to SQL to ensure redundancy - e.g.:
#  - check if table 'node_local_3200m' exists; if so record existing ID records
#  - get ids for all nodes, less those already processed, if any
#  - for chunks of 10,000, process the dataframe subset in parallel, convert  and send to sql with append (noting 