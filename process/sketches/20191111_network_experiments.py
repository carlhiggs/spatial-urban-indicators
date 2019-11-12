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
import osmnx as ox
import numpy as np
import requests
import pandas as pd
import geopandas as gpd

from sqlalchemy import create_engine
from _project_setup import *


from multiprocessing import  Pool


def create_local_nodes_dict(df,graph = G, distance = 3200):
    df[f'local_{distance}m'] = df.node.apply(lambda x: nx.multi_source_dijkstra_path_length(graph, {x}, cutoff=distance, weight='length'))
    return df


def parallelize_dataframe(df, func, n_cores=4):
    start_time = time.time()
    l = len(df)
    df_split = np.array_split(df, n_cores)
    pool = Pool(n_cores)
    df = pd.concat(pool.map(func, df_split))
    pool.close()
    pool.join()
    end_time = time.time()
    print("{} rows: {} minutes; rate per 100,000: {} minutes".format(l,(end_time-start_time)/60,(end_time-start_time)/l*100000/60))
    return df


engine = create_engine("postgresql://{user}:{pwd}@{host}/{db}".format(user = db_user,
                                                                      pwd  = db_pwd,
                                                                      host = db_host,
                                                                      db   = db))


sql_queries = {
    'Create new columns and indices for sampling point edge and node relations':'''
    ALTER TABLE sampling_points_30m ADD COLUMN IF NOT EXISTS n1 text;
    ALTER TABLE sampling_points_30m ADD COLUMN IF NOT EXISTS n1_distance int;
    ALTER TABLE sampling_points_30m ADD COLUMN IF NOT EXISTS n2 text;
    ALTER TABLE sampling_points_30m ADD COLUMN IF NOT EXISTS n2_distance int;
    CREATE INDEX IF NOT EXISTS sampling_points_30m_ogc_fid_idx ON sampling_points_30m (ogc_fid);
    UPDATE sampling_points_30m s
       SET n1 = e."from",
           n2 = e."to"
    FROM edges e
    WHERE e.ogc_fid = s.ogc_fid;
    CREATE INDEX IF NOT EXISTS sampling_points_30m_n1_idx ON sampling_points_30m (n1);
    CREATE INDEX IF NOT EXISTS sampling_points_30m_n2_idx ON sampling_points_30m (n2);
    ''',
    'Record distance from sampling points to node pairs':'''
    UPDATE sampling_points_30m s
      SET n1_distance = ST_Distance(s.geom,a.geom)::int
    FROM nodes a
    WHERE a.osmid = s.n1;
    UPDATE sampling_points_30m s
      SET n2_distance = ST_Distance(s.geom,b.geom)::int
    FROM nodes b
    WHERE b.osmid = s.n2;
    ''',
    'Record closest node and distance for destination points'
    '''
    ALTER TABLE osm_destinations ADD COLUMN IF NOT EXISTS ogc_fid text;
    UPDATE osm_destinations o
       SET ogc_fid = u.ogc_fid,
           match_point_geom = u.match_point_geom,
           match_point_distance = ST_Distance(o.geom,u.match_point_geom),
           n1 = u.n1,
           n2 = u.n2
    FROM
    (SELECT dest_oid,
            e.ogc_fid,
            ST_ClosestPoint(d.geom,e.geom) AS match_point_geom, 
            "from" n1,
            "to" n2
    FROM osm_destinations d
    CROSS JOIN edges e
    ORDER BY d.geom <#> e.geom
    LIMIT 1) u
    WHERE u.dest_oid = o.dest_oid;  
    '''
    }

for q in sql_queries:
    print(f'\n{q}... '),
    start_time = time.time()
    engine.execute(q)
    end_time = time.time()
    print("Completed in {} minutes.".format((end_time-start_time)/60)

# Set up network for analysis with NetworkX
print("Set up network for analysis with NetworkX")
start_time = time.time()
# variable for location of existing graphml xml network file, generated by OSMnx
graphml = '../data/study_region/bangkok_thailand_2018/bangkok_thailand_2018_10000m_pedestrian_osm_20190430.graphml'
# read in network
G = nx.read_graphml(graphml, node_type=str)
# ensure it is interpreted as undirected; we want our pedestrians to walk in either direction
G = nx.Graph(G)
# # length is a string (why?!), but must be an float
for u,v,d in G.edges(data=True):
   d['length'] = float(d['length'])

end_time = time.time()
print("Network x graph set up in  {:.02f} minutes".format((end_time-start_time)/60))
# For Bangkok: Network x graph set up in  1.02 minutes

# Set up output dataframe
df = pd.DataFrame(list(G.nodes),columns=['node'])

# Calculate node relations
df = parallelize_dataframe(df,create_local_nodes_dict)

# each node will be associated with a dictionary of nodes it has access to within 3200m: e.g.
# {5862588417: 0, 5862588435: 30.08, 5862588428: 43.661, 5862588436: 64.52, 5862588433: 69.287,
# ...
# 3706489893: 3195.013, 5668591342: 3195.336999999999, 5668591359: 3197.7199999999993, 1688538955: 3197.8099999999986}
# 
# with data structure looking like:
#           node                                        local_3200m
# 0   5862588417  {5862588417: 0, 5862588435: 30.08, 5862588428:...
# 1   5862588419  {5862588419: 0, 5862588424: 36.77, 5862588421:...
# 2   5862588420  {5862588420: 0, 5862588419: 140.418, 586258842...
# 3   5862588421  {5862588421: 0, 5862588419: 38.107, 5862588424...
# 4   5862588422  {5862588422: 0, 5862588424: 3.999, 5862588426:...
# ..         ...                                                ...
# 95  5898240371  {5898240371: 0, 5898240372: 29.795, 5898240382...
# 96  5898240372  {5898240372: 0, 5898240371: 29.795, 5898240382...
# 97  1199571317  {1199571317: 0, 1199571300: 112.81, 1112995534...
# 98  5935989109  {5935989109: 0, 5935989119: 52.557, 5942232342...
# 99  5898240373  {5898240373: 0, 5898240382: 28.829, 5898240372...

So the idea could be to process this in chunks outputting to SQL to ensure redundancy - e.g.:
 - check if table 'node_local_3200m' exists; if so record existing ID records
 - get ids for all nodes, less those already processed, if any
 - for chunks of 10,000, process the dataframe subset in parallel, convert  and send to sql with append (noting 