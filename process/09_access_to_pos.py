"""

Estimate access within threshold: Public open space
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

import networkx as nx
import time 
import numpy as np
import requests
import pandas as pd
import geopandas as gpd
import psycopg2
from sqlalchemy import create_engine
import pandana

from script_running_log import script_running_log

from _project_setup import *
now = time.strftime('%Y%m%d_%H%M')

connection = f"postgresql://{db_user}:{db_pwd}@{db_host}/{db}"

def graphml_to_pandana(graphml):
    # Set up network for analysis with NetworkX
    print("Setting up network for analysis with NetworkX...")
    start_time = time.time()    
    import osmnx as ox
    file = os.path.basename(graphml)
    folder = os.path.dirname(graphml)
    G = ox.load_graphml(file, folder)
    gdf_nodes = ox.graph_to_gdfs(G, nodes=True, edges=False)
    gdf_edges = ox.graph_to_gdfs(G, nodes=False, edges=True)
    # get network from Pandana
    network=pandana.network.Network(gdf_nodes["x"], gdf_nodes["y"], gdf_edges["u"], gdf_edges["v"],gdf_edges[["length"]])
    end_time = time.time()
    print("Graphml network loaded in  {:.02f} minutes".format((end_time-start_time)/60))
    # For Bangkok: Network x graph set up in  .84 minutes
    return(network)

def pandanas_accessability(network, destinations, cutoff):
    network.precompute(cutoff + 1)
    network.set_pois(category='all', maxdist=cutoff, maxitems=1, x_col=destinations['lon'], y_col=destinations['lat'])
    result = network.nearest_pois(distance=cutoff, category='all', num_pois=1)
    return(result)

def main():
    # simple timer for log file
    start = time.time()
    script = os.path.basename(sys.argv[0])
    task = 'Calculate access to public open space'
    engine = create_engine(connection)
    
    # load network graph
    graphml = os.path.join(locale_dir,f'{buffered_study_region}_pedestrian_{osm_prefix}.graphml')
    network = graphml_to_pandana(graphml)

    dest = {'pos_any':[400,'''LEFT JOIN aos_public_osm USING (aos_id) 
                                  WHERE aos_public_osm.aos_id IS NOT NULL 
                                    AND aos_ha_public > 0 AND water_percent < 100'''],
            'pos_large':[400,'''LEFT JOIN aos_public_osm USING (aos_id) 
                                  WHERE aos_public_osm.aos_id IS NOT NULL 
                                    AND aos_ha_public > 1.5 
                                    AND water_percent < 100''']}
    print("Estimating access within threshold for...")
    for d in dest:
        print(f' - {d}')
        destination = d
        distance = dest[d][0]
        query = dest[d][1]
        table = 'aos_nodes_30m_line'
        sql = f'''
            SELECT dest_table.*,
            ST_X(ST_Transform(dest_table.geom,4326)) lon, 
            ST_Y(ST_Transform(dest_table.geom,4326)) lat
            FROM {table} dest_table
            {query};
            '''
        destinations = gpd.GeoDataFrame.from_postgis(sql, engine, geom_col='geom')
        access = pandanas_accessability(network, destinations, distance+1)
        access.index.name = 'node_osmid'
        access.columns = ['distance_m']
        access.to_sql(f'od_node_{destination}',index='node_osmid',if_exists='replace',con=engine)
        sql = f'''
        DROP TABLE IF EXISTS ind_access_{destination};
        CREATE TABLE ind_access_{destination} AS
        SELECT DISTINCT ON (point_id) 
            point_id, 
            s_node_distance,
            distance_m,
            s_node_distance + distance_m AS full_distance_m,
            ((s_node_distance + distance_m)<={distance})::int access_{distance}m
        FROM origins o
        LEFT JOIN od_node_pos_any n ON o.s_node::bigint = n.node_osmid
        ORDER BY point_id, s_node_distance ASC;
        COMMENT ON TABLE ind_access_{destination}                     IS 'Created {now}: Estimates for access to the destination "{destination}" for each sample point.  A binary indicator of access is evaluated using a threshold of distance in metres <= {distance} m';
        COMMENT ON COLUMN ind_access_{destination}.s_node_distance    IS 'Distance (m) from sample point to network node with shortest distance to destination';
        COMMENT ON COLUMN ind_access_{destination}.distance_m         IS 'Distance (m) from node to destination (shortest route accessible for this sample point) up to 1 metre beyond threshold of {distance}';
        COMMENT ON COLUMN ind_access_{destination}.full_distance_m    IS 'Distance (m) from sample point to destination (note: threshold limited distance; results beyond {distance}m are truncated';
        COMMENT ON COLUMN ind_access_{destination}.access_{distance}m IS 'Indicator of access for sample point to destination within {distance}m inclusive (0 = no access; 1 = access)';
        '''
        engine.execute(sql)

if __name__ == '__main__':
    main()
    # output to completion log    
    script_running_log(script, task, start, locale)
    engine.dispose()