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
                      
    if 'reprocess' in sys.argv:
        reprocess = True
    else:
        reprocess = False
                      
    # retrieve subset of datasets which are files to be joined based on accessibility analyses (previously run)
    df = df_datasets.query("purpose=='indicators' & type=='access'").copy().sort_index()
    
    # retrieve list of additional covariate names from population data set
    population = pandas.read_csv(population_linkage[analysis_scale]['data'],index_col=population_linkage[analysis_scale]['linkage']) 
    population_fields = get_df_data_fields(population,population_map_fields)
    
    # create dictionary of additional covariate names for mapping (with superscript 2)
    column_names = {}
    # format to display superscript 2 for square kilometres
    for f in population_fields:
        column_names[f] = f.replace('sqkm','km\u00B2')
 
    schema = 'ind_area'
    for area in df.linkage_layer.unique():
        area_id = areas[area]['id']
        # note: for aggregation to areas to be successful, an area linkage layer must be defined
        print(area)
        for row in df.query(f"linkage_layer=='{area}'").itertuples():
            destination = getattr(row,'destination')  
            print(f"  - {destination}")
            distance = getattr(row,'resolution')
            measure = 'percent_access'
            
            area_layer = getattr(row,'linkage_layer')
            area_linkage_id = getattr(row,'linkage_id')
            map_name_suffix = getattr(row,'table_out_name')
            table = map_name_suffix.replace('_pop_pct','')
            # get information about this measure
            data_type = valid_type(getattr(row,'data_type'))
            description = getattr(row,'alias')
            heading = '{}: {}'.format(full_locale,getattr(row,'map_heading'))
            aggregation = getattr(row,'aggregation')
            linkage_id = getattr(row,'linkage_id')
            point_overlay_xy = getattr(row,'point_overlay_xy')
            display_id = area_layer
            map_field = getattr(row,'map_field')
            units = getattr(row,'units')
            rate = getattr(row,'rate')
            rate_units = getattr(row,'rate_units')
            rate_scale = getattr(row,'rate_scale')
            units = format_units(units,rate_units,rate_scale)
            target_year = getattr(row,'year_target')
            source = getattr(row,'provider')
            potential_column_width = len(f'{map_field}_{aggregation}')
            if potential_column_width < pd.get_option("display.max_colwidth"):
                pd.set_option("display.max_colwidth", potential_column_width)
            print('\t{}'.format(table))
            map_name = f'{locale}_ind_{map_name_suffix}'
            if os.path.isfile(f'{locale_maps}/html/{map_name}.html') and reprocess==False:
                print('\t - File appears to already have been processed (HTML output exists); skipping.')
            else:
                if 'skip_tables' not in sys.argv:
                    csv_file = f'{locale_maps}/csv/{study_region}_{map_name_suffix}.csv'
                    generate_isid_csv_template(engine, area_layer, area_linkage_id, target_year, measure, units, schema, table, csv_file)
                if 'skip_maps' not in sys.argv:
                    # Create map
                    attribution = '{} | {} | {} data: {}'.format(map_attribution,areas[area_layer]['attribution'],map_field,source)
                    coalesce_na = '{}'.format(getattr(row,'coalesce_na'))
                    data_fields = population_fields
                    generate_map(engine,map_name,map_attribution, attribution, area, heading, measure, map_field,  linkage_id, schema, table, coalesce_na, data_fields,column_names,map_style,outpath=locale_maps)
    # output to completion log                  
    script_running_log(script, task, start, locale)
    engine.dispose()

if __name__ == '__main__':
    main()