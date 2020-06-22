"""

Render documentation
~~~~~~~~~~~~~~~~~~~~

Script:  
    _create_documentation.py
Purpose: 
    Render the project documentation, based on the project configuration file and outputs.

"""

import os
import sys
import pandas as pd
import time

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

def generate_metadata_rst(ind_metadata,df_context):
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
     ['Population per km²','{locale}_02_population_{level}_population_per_sqkm'],
     ['Households per km²','{locale}_02_population_{level}_households_per_sqkm'],
     ['Communities per km²','{locale}_02_population_{level}_communities_per_sqkm'],
     ['Population in communities per km²','{locale}_02_population_{level}_population_in_communities_per_sqkm','11']
    ]
    # defined page heading as first line
    rst = 'Indicators\r\n==========\r\n'
    dimensions = ind_metadata.dimension.unique()
    dimensions.sort()
    for dimension in dimensions:
        dimension_text = dimension[3:]
        # create heading for dimension 
        rst = '{}\r\n\r\n{}\r\n{}\r\n'.format(rst,dimension_text,'~'*len(dimension_text))
        print(f'{dimension}:')
        for category in ind_metadata.loc[ind_metadata.dimension==dimension,'indicator_category'].unique():
          # create heading for indicator
          if str(category) not in ('','nan'):
            print(f'\t{category}')
            category_thai = df_context.loc[df_context['English']==category,'Thai'].values[0]
            category_definition = df_context.loc[df_context['English']==category,'Draft definition for Bangkok context'].values[0]
            rst = '{}\r\n\r\n{}\r\n{}\r\n'.format(rst,category,'|'*len(category))
            # add Thai name
            rst = '{}\r\n{}\r\n'.format(rst,category_thai)
            # add description for indicator
            rst = '{}\r\n{}\r\n'.format(rst,category_definition)
          for d in ind_metadata.loc[(ind_metadata.dimension==dimension)&(ind_metadata.indicator_category==category),'data_name'].unique():
            print(f'\t - {d}')
            # create heading for dataset
            if d != dimension_text:
                rst = '{}\r\n\r\n{}\r\n{}\r\n'.format(rst,d,'-'*len(d))
            ds = ind_metadata.query(f'dimension == "{dimension}" & indicator_category=="{category}" & data_name == "{d}"').copy()
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
                                             map = '{}_01_study_region'.format(locale).lower(),
                                     study_region = study_region)
                rst = '{}\r\n\r\n{}\r\n'.format(rst,map_code)
            if ds.iloc[0].purpose=='population':
                # add description for further usage by indicators
                rst = '{}\r\n{}\r\n'.format(rst,ds.iloc[0].method_description_ind)
                # rst = '{}\r\n\r\nIndicators\r\n^^^^^^^^^^\r\n'.format(rst)
                for popi in population_items:
                    rst = '{}\r\n\r\n{}\r\n{}\r\n'.format(rst,popi[0],'-'*len(popi[0]))
                    for level in ['district','subdistrict']:
                        pop_map = popi[1].format(locale=locale,level=level)
                        if len(popi)==2:
                            sdg = ''
                            rst = '{}\r\n\r\n'.format(rst)
                        else:
                            sdg = popi[2]
                            rst = '{}\r\n\r\nAligns with Sustainable Development Goals: {}.\r\n\r\n'.format(rst,sdg)
                        # todo: implement SDG code
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
                                             map = pop_map.lower(),
                                             study_region = study_region)
                        rst = '{}\r\n\r\n{}\r\n'.format(rst,map_code)
            if ds.iloc[0].purpose=='indicators':
                for ind in ds.method_description_ind.unique():
                    df_ind = ds.query(f'method_description_ind == "{ind}"').copy()
                    # create heading for specific indicator
                    a = df_ind.iloc[0].alias
                    a = a[:1].upper() + a[1:]
                    rst = '{}\r\n\r\n{}\r\n{}\r\n'.format(rst,a,'>'*len(a))
                    # add indicator method description
                    method = df_ind.iloc[0].method_description_ind
                    sdg = df_ind.iloc[0].sdg
                    # to do - parse SDG numbers and add in hyperlink
                    if str(sdg) not in ['','nan']:
                        rst = '{}\r\n{}\r\n\r\nAligns with Sustainable Development Goals: {}.\r\n\r\n'.format(rst,method,sdg)
                    else:
                        rst = '{}\r\n{}\r\n\r\n'.format(rst,method)
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
                                             map = ind_map.lower(),
                                             study_region = study_region)
                        rst = '{}\r\n\r\n{}\r\n'.format(rst,map_code)
                        plots = df_ind[df_ind['plot'].astype('str')!='nan'].copy()
                        plots = plots[plots.linkage_layer=='district']
                        n_plots = len(plots)
                        if n_plots > 0 and level=='district': 
                            for x in range(0,n_plots):
                                y     =  plots['table_out_name'].values[x]
                                ylab  =  plots['map_field'].values[x]
                                title =  plots['map_heading'].values[x].title()
                                x1   = 'population'     
                                x2   = 'population per sqkm'
                                plot1 = f'{y}_{x1}'.replace(' ','_')
                                plot2 = f'{y}_{x2}'.replace(' ','_')
                                plot3 = f'{y}'.replace(' ','_')
                                if os.path.exists(f'../maps/{study_region}/svg/plots/{plot3}.svg'):
                                    desc1 = f'{ylab} by {x1}'
                                    desc2 = f'{ylab} by {x2}'
                                    desc3 = f'{ylab}, ranked in ascending order'
                                    description = f'Figures for {title} with regard to {ylab} by {level}, clockwise from top: by {x1}; by {x2}; {level}s ranked in ascending order.'
                                    description_latex = f'{level}s ranked in ascending order by {ylab} with regard to {title}.'.capitalize()
                                    rst = '{}\r\n\r\n'.format(rst)
                                    plot_code = (
                                                '\r\n'
                                                '.. only:: html\r\n\r\n'
                                                '    .. raw:: html\r\n\r\n'
                                                '        <div id="plot-div">\r\n'
                                                '            <div id="div1" class="plot-box">\r\n'
                                               f'        	     <img alt={desc1} src="./../svg/plots/{plot1}.svg" class="plot-img">\r\n'
                                                '            </div>\r\n'
                                                '            <div id="div2" class="plot-box">\r\n'
                                               f'        	     <img alt={desc2} src="./../svg/plots/{plot2}.svg" class="plot-img">\r\n'
                                                '            </div><br>\r\n'
                                                '       </div><br>\r\n'
                                                '       <div>\r\n'
                                                '            <div id="div3" class="plot-box-large">\r\n'
                                               f'        	     <img alt={desc3} src="./../svg/plots/{plot3}.svg">\r\n'
                                                '            </div>\r\n'
                                               f'       <figcaption>{description}.</figcaption>\r\n\r\n'
                                                '       </div><br>\r\n\r\n'
                                                '.. only:: latex\r\n\r\n'
                                               f'   .. figure:: ../maps/{study_region}/pdf/plots/{plot1}.pdf\r\n'
                                                '      :width: 48%\r\n'
                                                '      :align: center\r\n\r\n'
                                               f'      Scatterplot of {ylab} by population for districts.\r\n\r\n'
                                               f'   .. figure:: ../maps/{study_region}/pdf/plots/{plot2}.pdf\r\n'
                                                '      :width: 48%\r\n'
                                                '      :align: center\r\n\r\n'
                                               f'      Scatterplot of {ylab} by population density for districts.\r\n\r\n'
                                               f'   .. figure:: ../maps/{study_region}/pdf/plots/{plot3}.pdf\r\n'
                                                '      :width: 100%\r\n'
                                                '      :align: center\r\n\r\n'
                                               f'      {description_latex}\r\n\r\n'
                                                )
                                    rst = '{}\r\n\r\n{}\r\n'.format(rst,plot_code)
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
    date_yyyy_mm_dd =  time.strftime("%Y-%m-%d")
    project_pdf_in = f'{full_locale} Liveability'.lower().replace(' ','')
    project_pdf_out = f'{full_locale} Liveability {year} report {date_yyyy_mm_dd}' 
    # make = (
            # "make clean" 
            # "  && make html"
           # f"  && cp -rT _build/html ../maps/{study_region}/docs"
            # )
    make = (
            "make clean" 
            "  && make html"
           f"  && cp -rT _build/html ../maps/{study_region}/docs"
            "  && make latexpdf"
           f"  && cp _build/latex/{project_pdf_in}.pdf '../maps/{study_region}/{project_pdf_out}.pdf'"
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
        metadata = generate_metadata_rst(get_ind_metadata(),df_context)
        print(f"{metadata}", file=text_file)
        
    line_prepender('../docs/conf_template.py','../docs/conf.py',get_sphinx_conf_header())
    
    make_locale_documentation(study_region)

if __name__ == '__main__':
    main()