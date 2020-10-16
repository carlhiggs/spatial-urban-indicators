"""

Generate attributions
~~~~~~~~~~~~~~~~~~~~~

Script:  
    _generate_attributions.py
Purpose: 
    Save a CSV of formatted attributions for processed indicators

"""

import os
import sys
import time
# Import custom variables for liveability indicator process
from _project_setup import *
 
def main():
    # simple timer for log file
    date = time.strftime('%Y-%m-%d')
               
    # retrieve subset of datasets which are files to be joined based on accessibility analyses (previously run)
    df = df_datasets.query("purpose in ['indicators','destinations','methods','boundaries']").copy().sort_index()
    
    df['attribution'] = df.apply(lambda x: f'{ map_attribution.replace("  Grey indicates no data.","")} | data: "{x.provider}" ({x.year_published})',axis=1)
    df = df[['purpose','indicator_measure', 'attribution','dimension', 'category', 'type', 'region','data_name','method_description_data','method_description_ind','data_file','source_url','date_acquired','licence','licence_url']] \
        .drop_duplicates() \
        .sort_values(['purpose','dimension','category','indicator_measure'])
    df[['purpose','indicator_measure','attribution']].to_csv(f'{output_dir}/csv/attribution_{date}_brief.csv',index=False)
    df.to_csv(f'{output_dir}/csv/attribution_{date}_full.csv',index=False)

if __name__ == '__main__':
    main()