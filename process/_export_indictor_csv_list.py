import os
import sys
import pandas as pd
import time

# # Import variables from the Sphinx set up script
# sys.path.insert(0, os.path.abspath('../docs'))
# from conf import *

# Import custom variables for liveability indicator process
from _project_setup import *

region_name = study_region.title()
date_yyyy_mm_dd =  time.strftime("%Y-%m-%d")
file_name = f'{region_name}_indicators_{date_yyyy_mm_dd}'

def get_ind_metadata():
     # find and return records for all indicator data sources with a defined indicator method description
     df = df_datasets.loc[df_datasets['method_description_ind'].fillna('')!='',].copy()
     df['map'] = df.loc[:,'table_out_name'].apply(lambda x: f'{locale}_ind_{x}')
     # df['description'] = df.apply(lambda x: '{}: {}'.format(x["map_heading"],x["map_field"]),axis=1)
     df['description'] = df['resource']
     return df

df = get_ind_metadata()

df[df.role=='indicators'][['description','dimension','category','table_out_name','rate_scale','units','rate_units','linkage_layer','data_name','year_published','year_target','provider','method_description_data','method_description_ind','sdg','data_file','excel_sheet','date_acquired','licence','licence_url','resolution','map_field']].sort_values(by=['dimension','category'],axis=0).to_csv(f'{file_name}.csv',encoding='utf-8-sig')