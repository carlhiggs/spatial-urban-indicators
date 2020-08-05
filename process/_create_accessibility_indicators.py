"""

Create accessibility indicators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Script:  
    _create_accessibility_indicators.py
Purpose: 
    Create indicators based on previously run accessibility analyses

"""

import time
import os
import pandas as pd
import numpy as np
from sqlalchemy import create_engine, NVARCHAR, event
import sqlite3

from script_running_log import script_running_log

# Import custom variables for National Liveability indicator process
from _project_setup import *
 
def main():
    # simple timer for log file
    start = time.time()
    script = os.path.basename(sys.argv[0])
    task = 'Create indicators from linkage files'
    
    engine = create_engine(f"postgresql://{db_user}:{db_pwd}@{db_host}/{db}")
    gpkg_path = os.path.join(locale_maps,'gpkg')
    engine_sqlite = create_engine(f'sqlite:///{gpkg_path}/{study_region}.gpkg',module = sqlite3)
                      
    # retrieve subset of datasets which are files to be joined based on accessibility analyses (previously run)
    df = df_datasets.query("purpose=='indicators' & type=='access'").copy().sort_index()
    
    # retrieve list of additional covariate names from population data set
    population = pandas.read_csv(population_linkage[analysis_scale]['data'],
                                 index_col=population_linkage[analysis_scale]['linkage']) 
    data_fields = get_df_data_fields(population,population_map_fields)
    
    schema = 'ind_area'
    measure = 'percent_access'
    for area in df.linkage_layer.unique():
        area_id = areas[area]['id']
        area_attribution = areas[area]['attribution']
        print(area)
        for row in df.query(f"linkage_layer=='{area}'").itertuples():
            table = row.table_out_name
            map_name = table.replace('_pop_pct','')
            print('\t{}'.format(table))
            if 'skip_tables' not in sys.argv:
                out_path=f'{locale_maps}/csv'
                generate_isid_csv_template(engine, row, out_path, prefix=study_region, schema=schema,table=map_name,measure=measure)
            if 'skip_maps' not in sys.argv:
                # Create map
                generate_map(engine,row,out_path=locale_maps,data_fields=data_fields,prefix=locale,schema=schema,map_attribution=map_attribution,area_attribution=area_attribution,map_style_html_css=map_style,table=map_name,measure=measure)
                
    # output to completion log                  
    script_running_log(script, task, start, locale)
    engine.dispose()

if __name__ == '__main__':
    main()