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
bangkok_01_study_region
bangkok_02_population_subdistrict_population_per_sqkm
bangkok_02_population_district_population_per_sqkm
bangkok_02_population_subdistrict_households_per_sqkm
bangkok_02_population_district_households_per_sqkm
bangkok_02_population_subdistrict_communities_per_sqkm
bangkok_02_population_district_communities_per_sqkm
bangkok_02_population_subdistrict_population_in_communities_per_sqkm
bangkok_02_population_district_population_in_communities_per_sqkm
bangkok_02_population_subdistrict_population_not_in_communities_per_sqkm
bangkok_02_population_district_population_not_in_communities_per_sqkm

"""

import os
import sys
import pandas as pd

# # Import variables from the Sphinx set up script
# sys.path.insert(0, os.path.abspath('../docs'))
# from conf import *

# Import custom variables for National Liveability indicator process
from _project_setup import *

def get_ind_list():
    df = df_datasets[df_datasets.index.str.startswith('linkage:')].copy()
    df['map'] = df.loc[:,'table_out_name'].apply(lambda x: f'{locale}_ind_{x}')
    df['description'] = df.apply(lambda x: '{}: {}'.format(x["map_heading"],x["map_field"]),axis=1)
    return df[['map','description']]
    
def create_html_select(map_descriptions):
    text = '\r\n'.join(map_descriptions.apply(lambda x: '        <option value="{}">{}</option>'.format(x[0],x[1]),axis=1).to_list())
    return(text)

def generate_interactive_maps_rst(select_text):
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
    return(f'{header}{select_text}{footer}')

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
        maps_interactive = generate_interactive_maps_rst(create_html_select(get_ind_list()))
        print(f"{maps_interactive}", file=text_file)
        
    line_prepender('../docs/conf_template.py','../docs/conf.py',get_sphinx_conf_header())
    
    make_locale_documentation(study_region)

if __name__ == '__main__':
    main()