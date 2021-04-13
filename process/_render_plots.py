"""

Render plots
~~~~~~~~~~~~~~~~~~~~~~~~~

Script:  
    _render_plots.py
Purpose: 
    Create exploratory data plots

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

# Import custom variables for liveability indicator process
from _project_setup import *

def label_point(x, y, val, ax,x_offset=0):
    a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
    for i, point in a.iterrows():
        ax.text(point['x']+x_offset, point['y'], str(point['val']),rotation=45)

def main():
    # simple timer for log file
    start = time.time()
    script = os.path.basename(sys.argv[0])
    task = 'Render plots'
    print(task)
    engine = create_engine(f"postgresql://{db_user}:{db_pwd}@{db_host}/{db}")
                      
    # retrieve subset of datasets which are files to be joined based on linkage
    df = df_datasets.query('type=="linkage" | type=="raster" | type=="access"').copy()
    # df = df_datasets.query('type=="access"').copy()
    df = df[df['plot'].astype('str') != 'nan']    
    for row in df.index:
        row_type = df.loc[row,'type']
        data_type = valid_type(df.loc[row,'data_type'])
        description = df.loc[row,'resource']
        description = '\n'.join(wrap(description, 80))
        plot_data_y = df.loc[row,'table_out_name'].replace(' ','_',).replace('-','_')
        area_layer = df.loc[row,'linkage_layer']
        if df.loc[row,'plot'] == area_layer:
            print(f"\n - {description}")
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
            ylab = description
            title = description
            x1   = 'population'     
            x2   = 'population per sqkm'
            if row_type!='access':
                sql = f'''
                SELECT a.{area_layer},
                       a.{area_layer}_en,
                       a.{area_layer}_th,
                       a."{x1}",
                       a."{x2}",
                       d.{y}
                FROM {area_layer} a
                LEFT JOIN {y} d USING ({linkage_id});
                '''
            else:
                y = plot_data_y
                schema='ind_area'
                table = plot_data_y.replace('_pop_pct','')
                table_y = 'percent_access'
                sql = f'''
                SELECT a.{area_layer}_id,
                       a.{area_layer}_en,
                       a.{area_layer}_th,
                       a."{x1}",
                       a."{x2}",
                       d.{table_y} {y}
                FROM {area_layer} a
                LEFT JOIN {schema}.{table} d USING ({linkage_id});
                '''
            
            data = pd.read_sql(sql,engine)
            data['regions_of_interest'] = 'Other regions'
            data.loc[~(data[regions_of_interest_variable].isin(regions_of_interest)),'regions_of_interest'] = 'Case studies'
            data['label'] = data[f'{area_layer}_th'] + ' ' + data[f'{area_layer}_en']
            data['full_label'] = data['label'] 
            data.loc[~(data[regions_of_interest_variable].isin(regions_of_interest)),'label'] = ''
            
            #colours = ['#d01c8b','#f1b6da','#f7f7f7','#b8e186','#4dac26']
            #colour_binary = [colours[0], colours[-1]]
            
            for dir in ['pdf','svg']:
                folder_dir = (f'../output/{study_region}/{dir}/plots/')
                if not os.path.exists(folder_dir):
                    os.makedirs(folder_dir)
            
            if area_layer == regions_of_interest_scale:
                # scatterplots
                # by population
                location = f'../output/{study_region}/pdf/plots/{y}_{x1}.pdf'.replace(' ','_')
                if not os.path.exists(location):
                    font = {'family':'Garuda','size':9.0}
                    matplotlib.rc('font', **font)
                    g = sns.lmplot(x = x1,y = y, data=data, hue='regions_of_interest', fit_reg=False)
                    g._legend.remove()
                    g.set(xlabel=x1.capitalize(), ylabel=title)
                    label_point(data[x1], data[y], data['label'], plt.gca())
                    for ax in g.axes[:,0]:
                        ax.get_xaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: f"{x:,.0f}"))
                        if data_type in ['integer','Int64']:
                            ax.get_yaxis().set_major_locator(matplotlib.ticker.MaxNLocator(integer=True))
                            ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: f"{x:,.0f}"))
                        else:
                            ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: "{:,.9g}".format(round(x,3))))
                    
                    plt.tight_layout()
                    # plt.show()   
                    g.savefig(location)   
                    plt.close()
                    print(f"\t{location} saved.")
                else:
                    print(f"\t{location} already exists.")
                
                # by population per square kilometre
                location = f'../output/{study_region}/pdf/plots/{y}_{x2}.pdf'.replace(' ','_')
                if not os.path.exists(location):
                    font = {'family':'Garuda','size':9.0}
                    matplotlib.rc('font', **font)
                    g = sns.lmplot(x = x2,y = y, data=data, hue='regions_of_interest', fit_reg=False)
                    g._legend.remove()
                    g.set(xlabel=x2.replace('sqkm','km\u00B2').capitalize(), ylabel=title)
                    label_point(data[x2], data[y], data['label'], plt.gca())
                    for ax in g.axes[:,0]:
                        ax.get_xaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: f"{x:,.0f}"))
                        if data_type in ['integer','Int64']:
                            ax.get_yaxis().set_major_locator(matplotlib.ticker.MaxNLocator(integer=True))
                            ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: f"{x:,.0f}"))
                        else:
                            ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: "{:,.9g}".format(round(x,3))))
                    
                    plt.tight_layout()
                    # plt.show()
                    
                    g.savefig(location)   
                    plt.close()
                    print(f"\t{location} saved.")
                else:
                    print(f"\t{location} exists.")
                
            # Horizontal bar plot
            location = f'../output/{study_region}/pdf/plots/{y}.pdf'.replace(' ','_')
            if not os.path.exists(location):
                font = {'family':'Garuda','size':12.0}
                matplotlib.rc('font', **font)
                pd_data = data.sort_values(y)
                plt.figure(figsize=(14,10))
                ax = sns.barplot(x = pd_data[y],y = pd_data['full_label'])
                ax.set(xlabel=title, ylabel=area_layer.title())
                if data_type in ['integer','Int64']:
                    ax.xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(integer=True))
                    ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: f"{x:,.0f}"))
                else:
                    ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: f"{x:,.2g}"))
                
                ax.set_yticklabels(pd_data['full_label'])
                plt.tight_layout()
                # plt.show()
                
                ax.figure.savefig(location)  
                ax.figure.savefig(location.replace('pdf','svg'))  
                plt.close()
                print(f"\t{location} saved")
            else:
                print(f"\t{location} exists.")
        
    # output to completion log                  
    script_running_log(script, task, start, locale)
    engine.dispose()

if __name__ == '__main__':
    main()