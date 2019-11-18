"""

Create linkage indicators
~~~~~~~~~~~~~~~~~~~~~~~~~

Script:  
    _create_linkage_indicators.py
Purpose: 
    Create indicators based on linkage with boundary data from specification in datasets section of configuration file

"""

import time
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import seaborn as sns
from textwrap import wrap

# import custom utility functions
from _utils import *
from sqlalchemy import create_engine

#from __future__ import unicode_literals
import matplotlib
matplotlib.rc('font', family='Garuda')
from script_running_log import script_running_log

# Import custom variables for National Liveability indicator process
from _project_setup import *

def label_point(x, y, val, ax,x_offset=0):
    a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
    for i, point in a.iterrows():
        ax.text(point['x']+x_offset, point['y'], str(point['val']))

def main():
    # simple timer for log file
    start = time.time()
    script = os.path.basename(sys.argv[0])
    task = 'Render plots'
    print(task)
    engine = create_engine(f"postgresql://{db_user}:{db_pwd}@{db_host}/{db}")
                      
    # retrieve subset of datasets which are files to be joined based on linkage
    df = df_datasets[df_datasets.index.str.startswith('linkage:') | df_datasets.index.str.startswith('raster:')]
    df = expand_indicators(df)
    df = df[df['plot'].astype('str') != 'nan']    
    for row in df.index:
        data_type = valid_type(df.loc[row,'data_type'])
        description = df.loc[row,'alias']
        # heading = '{}'.format(df.loc[row,'map_heading'])
        heading = '{}'.format(df.loc[row,'map_heading'])
        print(f"\n - {heading}")
        # heading = '\n'.join(wrap(heading, 80))
        plot_data_y = df.loc[row,'table_out_name'].replace(' ','_',).replace('-','_')
        area_layer = df.loc[row,'linkage_layer']
        area_linkage_id = df.loc[row,'linkage_id']
        aggregation = df.loc[row,'aggregation']
        linkage_id = df.loc[row,'linkage_id']
        point_overlay_xy = df.loc[row,'point_overlay_xy']
        display_id = area_layer
        map_field = df.loc[row,'map_field']
        rate = df.loc[row,'rate']
        rate_units = df.loc[row,'rate_units']
        rate_scale = df.loc[row,'rate_scale']
        if aggregation not in ['','nan']:
            potential_column_width = len(map_field) 
        else:
            potential_column_width = len(map_field) + len(aggregation) + 1
        if potential_column_width < pd.get_option("display.max_colwidth"):
            pd.set_option("display.max_colwidth", potential_column_width)
        map_name = f'{locale}_ind_{plot_data_y}'
        # Prepare plot
        y    = plot_data_y
        ylab = heading
        title = map_field.title()
        x1   = 'population'     
        x2   = 'population per sqkm'
        sql = f'''
        SELECT a.district_id,
               a.district_en,
               a.district_th,
               a."{x1}",
               a."{x2}",
               d.{y}
        FROM {area_layer} a
        LEFT JOIN {y} d USING ({linkage_id});
        '''
        data = pd.read_sql(sql,engine)
        data['regions_of_interest'] = 'Other regions'
        data.loc[~(data.district_en.isin(regions_of_interest)),'regions_of_interest'] = 'Case studies'
        data['label'] = data['district_th'] + ' ' + data['district_en']
        data['full_label'] = data['label'] 
        data.loc[~(data.district_en.isin(regions_of_interest)),'label'] = ''

        #colours = ['#d01c8b','#f1b6da','#f7f7f7','#b8e186','#4dac26']
        #colour_binary = [colours[0], colours[-1]]

        # scatterplots

        ax1 = sns.lmplot(x1, y, data=data, hue='regions_of_interest', fit_reg=False)
        ax1._legend.remove()
        ax1.set(xlabel=x1.title(), ylabel=ylab,title = title)
        label_point(data[x1], data[y], data['label'], plt.gca())
        # plt.show()   
        location = f'../maps/{study_region}/png/plots/{y}_{x1}'.replace(' ','_')
        ax1.savefig(location, dpi=300)   
        print(f"\t{location}")
                
        
        ax2 = sns.lmplot(x2, y, data=data, hue='regions_of_interest', fit_reg=False)
        ax2._legend.remove()
        ax2.set(xlabel=x2.title(), ylabel=ylab,title = title)
        label_point(data[x2], data[y], data['label'], plt.gca())
        # plt.show()
        location = f'../maps/{study_region}/png/plots/{y}_{x2}'.replace(' ','_')
        ax2.savefig(location, dpi=300)   
        print(f"\t{location}")

        # Horizontal bar plot
        pd_data = data.sort_values(y)
        plt.figure(figsize=(14,10))
        ax3 = sns.barplot(pd_data[y], pd_data['full_label'])
        ax3.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
        ax3.set(xlabel=ylab, ylabel=area_layer.title(),title = title)
        ax3.set_yticklabels(pd_data['full_label'])
        plt.tight_layout()
        # plt.show()
        location = f'../maps/{study_region}/png/plots/{y}'.replace(' ','_')
        ax3.figure.savefig(location, dpi=300)   
        print(f"\t{location}")
        
    # output to completion log                  
    script_running_log(script, task, start, locale)
    engine.dispose()

if __name__ == '__main__':
    main()