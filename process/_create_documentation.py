"""

Render documentation
~~~~~~~~~~~~~~~~~~~~

Script:  
    _create_documentation.py
Purpose: 
    Render the project documentation, based on the project configuration file and outputs.
Authors: 
    Carl Higgs
    
Inds not currently including:







"""

import os
import sys
import pandas as pd

# # Import variables from the Sphinx set up script
# sys.path.insert(0, os.path.abspath('../docs'))
# from conf import *

# Import custom variables for National Liveability indicator process
from _project_setup import *

def get_ind_metadata():
    # find and return records for all indicator data sources with a defined indicator method description
    df = df_datasets.loc[df_datasets['method_description_ind'].fillna('')!='',].copy()
    df['map'] = df.loc[:,'table_out_name'].apply(lambda x: f'{locale}_ind_{x}')
    df['description'] = df.apply(lambda x: '{}: {}'.format(x["map_heading"],x["map_field"]),axis=1)
    return df

# def get_ind_metadata(prefix='linkage:'):
    # df = df_datasets[df_datasets.index.str.startswith(prefix)].copy()
    # df['map'] = df.loc[:,'table_out_name'].apply(lambda x: f'{locale}_ind_{x}')
    # df['description'] = df.apply(lambda x: '{}: {}'.format(x["map_heading"],x["map_field"]),axis=1)
    # return df[['map','description']]
    
def create_html_select(ind_metadata):
    map_descriptions = ind_metadata.loc[ind_metadata['purpose']=='indicators',['map','description']].copy()
    text = '\r\n'.join(map_descriptions.apply(lambda x: '        <option value="{}">{}</option>'.format(x[0],x[1]),axis=1).to_list())
    return(text)

def generate_interactive_maps_rst(html_select):
    header = f'''Interactive maps
================

.. only:: html

    .. raw:: html

        <form name="change">
        <SELECT NAME="options" ONCHANGE="document.getElementById('maps_interactive').src = './../html/'+this.options[this.selectedIndex].value+'.html'">
        <option value="{default_interactive_map}">Please select a map to explore...</option>
'''
    footer = f'''
        </SELECT>
        
        <iframe name="iframe" id="maps_interactive" src="./../html/{default_interactive_map}.html" height="500px" width="100%"></iframe>
        
.. only:: latex

    Interactive maps for indicators were created and are browsable using the html documentation.
        
'''
    return(f'{header}{html_select}{footer}')

def generate_metadata_rst(ind_metadata):
    # a list of metadata items to report on
    data_items = [['provider'      ,'Data source'                             ],
                  ['source_url'    ,'URL'                                     ],
                  ['year_published','Publication year'                        ],
                  ['year_target'   ,'Target year'                             ],
                  ['date_acquired' ,'Acquisition date (yyyymmdd)'             ],
                  ['licence'       ,'Licence'                                 ],
                  ['licence_url'   ,'Licence URL'                             ],
                  ['epsg'          ,'Spatial reference (EPSG code)'           ],
                  ['data_type'     ,'Date type'                               ],
                  ['resolution'    ,'Scale / Resolution'                      ],
                  ['citations'     ,'Citation'                                ],
                  ['notes'         ,'Notes'                                   ],
                  ['data_dir'      ,'Data location relative to project folder']]
    # unformatted population items
    population_items = [
     ['Population per sqkm','{locale}_02_population_{level}_population_per_sqkm'],
     ['Households per sqkm','{locale}_02_population_{level}_households_per_sqkm'],
     ['Communities per sqkm','{locale}_02_population_{level}_communities_per_sqkm'],
     ['Population in communities per sqkm','{locale}_02_population_{level}_population_in_communities_per_sqkm'],
     ['Population not in communities per sqkm','{locale}_02_population_{level}_population_not_in_communities_per_sqkm']
    ]
    # defined page heading as first line
    rst = 'Indicators\r\n==========\r\n'
    for d in ind_metadata.data_name.unique():
        # create heading for dataset
        rst = '{}\r\n\r\n{}\r\n{}\r\n'.format(rst,d,'~'*len(d))
        ds = ind_metadata.query(f'data_name == "{d}"').copy()
        # add description for dataset
        rst = '{}\r\n{}\r\n'.format(rst,ds.iloc[0].method_description_data)
        for i in data_items:
            if '{}'.format(ds.iloc[0][i[0]]) not in ['','nan']:
                rst = '{}\r\n**{}**: {}\r\n'.format(rst,i[1],ds.iloc[0][i[0]])
        if ds.iloc[0].purpose=='boundaries':
            # add description for further usage by indicators
            rst = '{}\r\n{}\r\n'.format(rst,ds.iloc[0].method_description_ind)
            map_code = (
                        '\r\n'
                        '.. only:: html\r\n\r\n'
                        '    .. raw:: html\r\n\r\n'
                        '        <figure>\r\n'
                        '        <img alt="{description}" src="./../png/{map}.png">\r\n'
                        '        <figcaption>{description}. '
                        '        <a href="./../html/{map}.html" target="_blank">Open interactive map in new tab</a><br></figcaption>\r\n'
                        '        </figure><br>\r\n\r\n'
                        '.. only:: latex\r\n\r\n'
                        '    .. figure:: ../maps/{study_region}/png/{map}.png\r\n'
                        '       :width: 70%\r\n'
                        '       :align: center\r\n\r\n'
                        '       {description}\r\n\r\n'
                        ).format(description = f'{full_locale} study region',
                                         map = '{}_01_study_region'.format(locale),
                                 study_region = study_region)
            rst = '{}\r\n\r\n{}\r\n'.format(rst,map_code)
        if ds.iloc[0].purpose=='population':
            # add description for further usage by indicators
            rst = '{}\r\n{}\r\n'.format(rst,ds.iloc[0].method_description_ind)
            rst = '{}\r\n\r\nIndicators\r\n^^^^^^^^^^\r\n'.format(rst)
            for popi in population_items:
                rst = '{}\r\n\r\n{}\r\n{}\r\n'.format(rst,popi[0],'-'*len(popi[0]))
                for level in ['district','subdistrict']:
                    pop_map = popi[1].format(locale=locale,level=level)
                    rst = '{}\r\n\r\n'.format(rst)
                    map_code = (
                                '\r\n'
                                '.. only:: html\r\n\r\n'
                                '    .. raw:: html\r\n\r\n'
                                '        <figure>\r\n'
                                '        <img alt="{description}" src="./../png/{map}.png">\r\n'
                                '        <figcaption>{description}. '
                                '        <a href="./../html/{map}.html" target="_blank">Click to open interactive map in new tab.</a><br></figcaption>\r\n'
                                '        </figure><br>\r\n\r\n'
                                '.. only:: latex\r\n\r\n'
                                '    .. figure:: ../maps/{study_region}/png/{map}.png\r\n'
                                '       :width: 70%\r\n'
                                '       :align: center\r\n\r\n'
                                '       {description}\r\n\r\n'
                                ).format(description = '{}, by {}'.format(popi[0],level).capitalize(),
                                         map = pop_map.capitalize(),
                                         study_region = study_region)
                    rst = '{}\r\n\r\n{}\r\n'.format(rst,map_code)
        if ds.iloc[0].purpose=='indicators':
            # create heading for indicators
            rst = '{}\r\n\r\nIndicators\r\n^^^^^^^^^^\r\n'.format(rst)
            for ind in ds.method_description_ind.unique():
                df_ind = ds.query(f'method_description_ind == "{ind}"').copy()
                # create heading for specific indicator
                a = df_ind.iloc[0].alias.capitalize()
                rst = '{}\r\n\r\n{}\r\n{}\r\n'.format(rst,a,'-'*len(a))
                # add indicator method description
                rst = '{}\r\n{}\r\n'.format(rst,df_ind.iloc[0].method_description_ind)
                levels = df_ind.linkage_layer.unique()
                # map_scale_text = f'View maps for {full_locale} at available scales:'
                for level in df_ind.linkage_layer.unique(): 
                    ind_map = 'bangkok_ind_{}'.format(df_ind.loc[df_ind.linkage_layer==level].table_out_name.to_list()[0])
                    rst = '{}\r\n\r\n'.format(rst)
                    map_code = (
                                '\r\n'
                                '.. only:: html\r\n\r\n'
                                '    .. raw:: html\r\n\r\n'
                                '        <figure>\r\n'
                                '        <img alt="{description}" src="./../png/{map}.png">\r\n'
                                '        <figcaption>{description}. '
                                '        <a href="./../html/{map}.html" target="_blank">Open interactive map in new tab</a><br></figcaption>\r\n'
                                '        </figure><br>\r\n\r\n'
                                '.. only:: latex\r\n\r\n'
                                '    .. figure:: ../maps/{study_region}/png/{map}.png\r\n'
                                '       :width: 70%\r\n'
                                '       :align: center\r\n\r\n'
                                '       {description}\r\n\r\n'
                                ).format(description = f'{a}, by {level}',
                                         map = ind_map.capitalize(),
                                         study_region = study_region)
                    rst = '{}\r\n\r\n{}\r\n'.format(rst,map_code)
    return(rst)

def get_sphinx_conf_header():
    import time
    
    current_year = time.strftime("%Y")
    header=(
            "# Configuration file for the Sphinx documentation builder.\r\n"
            "# -- Project information -----------------------------------------------------\r\n"
           f"\r\nproject = '{full_locale} Liveability'"
           f"\r\ncopyright = '{current_year}, {authors}'"
           f"\r\nauthor = '{authors}'"
            "\r\n\r\n# The full version, including alpha/beta/rc tags"
           f"\r\nrelease = '{version}'\r\n"
            )
    
    return(header)

def make_locale_documentation(study_region):
    """

    Render documentation
    ~~~~~~~~~~~~~~~~~~~~

    Script:  
        _create_documentation.py
    Purpose: 
        Render the project documentation, based on the project configuration file and outputs.
    Authors: 
        Carl Higgs

    """
    print("Render the project documentation, based on the project configuration file and outputs...."),
    make = (
            "make clean" 
            "  && make html"
           f"  && cp -rT _build/html ../maps/{study_region}/docs"
            "  && make latexpdf"
           f"  && cp _build/latex/*.pdf ../maps/{study_region}"
            )
    sp.call(make, cwd ='../docs', shell=True)  
    print(" Done.")
    
def line_prepender(infile, outfile, line):
    with open(infile, 'r') as i:
        lines = ''.join([line]+i.readlines())
        with open(outfile, "w") as o:
            print(lines, file=o)
        
def main():
    with open("../docs/maps_interactive.rst", "w") as text_file:
        maps_interactive = generate_interactive_maps_rst(create_html_select(get_ind_metadata()))
        print(f"{maps_interactive}", file=text_file)

    with open("../docs/indicators.rst", "w") as text_file:
        metadata = generate_metadata_rst(get_ind_metadata())
        print(f"{metadata}", file=text_file)
        
    line_prepender('../docs/conf_template.py','../docs/conf.py',get_sphinx_conf_header())
    
    make_locale_documentation(study_region)

if __name__ == '__main__':
    main()