# Script:  _project_setup.py
# Version: 20190520
# Author:  Carl Higgs
#
# All scripts within the process folder draw on the sources, parameters and modules
# specified in the file _project_configuration.xlsx to source and output 
# resources. 
#
# If you are starting a new project, you can set up the global parameters which 
# (pending overrides) should be applied for each study region in the 
#  detailed_explanation' folder.
#
# If you are adding a new study region to an existing project, this study region
# will be entered as a column within the 'Parameters' worksheet; the corresponding
# row entries must be completed as required.

# import modules
import os
import sys
import time
import pandas
import subprocess as sp
import math 
import re
import numpy as np

# import custom utility functions
from _utils import *

# Set up locale (ie. defined at command line, or else testing)
if len(sys.argv) >= 2:
  locale = '{studyregion}'.format(studyregion = sys.argv[1])
else:
  # locale = 'bang_phlat'
  locale = 'bangkok'
if __name__ == '__main__':
  print("\nProcessing script {} for locale {}...\n".format(sys.argv[0],locale))

cwd = os.path.join(os.getcwd(),'../process')

# Load settings from _project_configuration.xlsx
xls = pandas.ExcelFile(os.path.join(cwd,'_project_configuration.xlsx'))
df_parameters = pandas.read_excel(xls, 'Parameters',index_col=0)
df_datasets = pandas.read_excel(xls, 'Datasets')
df_osm = pandas.read_excel(xls, 'osm_open_space')
df_osm_dest = pandas.read_excel(xls, 'osm_destinations')
df_context = pandas.read_excel(xls, 'Bangkok context definitions',header=[0,1],skiprows=[2])

# set up indicator context document
df_context = df_context[['Group','Indicator']][0:24].ffill()
df_context.columns = df_context.columns.droplevel()

# prepare and clean configuration entries
df_parameters[locale] = df_parameters[locale].fillna('')
for var in [x for x in  df_parameters.index.values]:
    globals()[var] = df_parameters.loc[var][locale]
# full_locale = df_parameters.loc['full_locale'][locale]

# derived study region name (no need to change!)
study_region = '{}_{}_{}'.format(locale,region,year).lower()
db = 'li_{0}_{1}{2}'.format(locale,year,suffix).lower()

# region specific output locations
locale_dir = os.path.join(folderPath,'study_region','{}'.format(study_region))
locale_maps = os.path.join('../maps/',study_region)

# Study region buffer
buffered_study_region = '{}_{}{}'.format(study_region,study_buffer,units)

regions_of_interest =  [x.strip() for x in regions_of_interest.split(',')]

# sample points
points = '{}_{}m'.format(points,point_sampling_interval)

df_datasets = compile_datasets(df_datasets,full_locale)

region_where_clause_pandas = f""" {region_where_clause_id} == '{region_where_clause_match}' """
region_where_clause_sql = f""" "{region_where_clause_id}" = '{region_where_clause_match}' """



# Region set up
area_meta = {}
area_meta_fields = ['areas_of_interest','area_datasets','area_ids','area_id_types','area_names','area_display_main','area_display_bracket']
area_meta_test_length = []
for i in area_meta_fields:
    area_meta[i] = [x.strip() for x in str(globals()[i]).split(',')]
    array_length = len(area_meta[i])
    if i not in ['area_display_main','area_display_bracket']:
      area_meta_test_length.append(array_length)
if any(x for x in area_meta_test_length if x != area_meta_test_length[1]):
  sys.exit('Please check area data in project configuration: not all required areas of interest parameters appear to have been defined...')

areas = {}
for area in area_meta['areas_of_interest']:
  idx = area_meta['areas_of_interest'].index(area)
  # print('{} {}'.format(area,idx))
  if area_meta['area_datasets'] != '':
    areas[area] = {}
    areas[area]['data'] = df_datasets[df_datasets.index== area_meta['area_datasets'][idx]].data_file.values[0]
    areas[area]['name'] = area_meta['area_names'][idx]
    areas[area]['table'] = re.sub('[^\s\w]+', '', areas[area]['name']).lower().strip().replace(' ','_')
    areas[area]['id'] = area_meta['area_ids'][idx]
    areas[area]['id_type'] = area_meta['area_id_types'][idx]
    areas[area]['display_main'] = areas[area]['id']
    areas[area]['display'] = areas[area]['id']
    if len(area_meta['area_display_main']) > 1:
        areas[area]['display_main'] = area_meta['area_display_main'][idx]
        # areas[area]['display'] = areas[area]['display_main']
        if len(area_meta['area_display_bracket']) > 1:
            areas[area]['display_bracket'] = area_meta['area_display_bracket'][idx]
        else:
            areas[area]['display_bracket'] = ''
            # if areas[area]['display_bracket']!='':
                # areas[area]['display'] = (
                # '''"{}"||' ('||"{}"||')'''
                # ).format(areas[area]['display_main'],
                         # areas[area]['display_bracket'])
    else: 
        areas[area]['display'] = areas[area]['display_main']
    licence = str(df_datasets.loc[area_meta['area_datasets'][idx]]['licence'])
    if licence not in ['none specified','nan','']:
        licence_attrib = (
                          ' under <a href=\"{licence_url}/\">{licence}</a>'
                          ).format(licence_url = df_datasets.loc[area_meta['area_datasets'][idx]]['licence_url'],
                                   licence     = df_datasets.loc[area_meta['area_datasets'][idx]]['licence'])
    else:
        licence_attrib = ''
    areas[area]['attribution'] = (
                                  'Boundary data: <a href=\"{source_url}/\">{provider}</a>{licence_attrib}'
                                  ).format(source_url  = df_datasets.loc[area_meta['area_datasets'][idx]]['source_url'],
                                           provider    = df_datasets.loc[area_meta['area_datasets'][idx]]['provider'],
                                           licence_attrib = licence_attrib)

area_analysis  = areas[analysis_scale]['id']
analysis_field = areas[analysis_scale]['name']
area_ids = ([areas[area]['id'] for area in areas] + 
           [areas[area]['display_main'] for area in areas] +
           [areas[area]['display_bracket'] for area in areas])

area_id_types = [[areas[area]['id'],areas[area]['id_type']] for area in areas]

# Population
population_field = 'Population ({} estimate)'.format(population_target)

population_linkage = {}
for pop_data in list(df_datasets[['population:' in x for x in df_datasets.index]].index):
    data_type = pop_data.split(':')[1]
    population_linkage[data_type] = {}
    population_linkage[data_type]['data'] = '.{}'.format(df_datasets.loc[pop_data].data_file)
    population_linkage[data_type]['year_target'] = df_datasets.loc[pop_data].year_target
    # population_linkage[data_type]['linkage'] = '{}'.format(df_datasets.loc[pop_data].index_if_tabular)
    population_linkage[data_type]['linkage'] =  areas['subdistrict']['id']
    licence = str(df_datasets.loc[pop_data]['licence'])
    if licence not in ['none specified','nan','']:
        licence_attrib = (
                          ' under <a href=\"{licence_url}/\">{licence}</a>'
                          ).format(licence_url = df_datasets.loc[pop_data]['licence_url'],
                                   licence     = df_datasets.loc[pop_data]['licence'])
    else:
        licence_attrib = ''
    population_linkage[data_type]['attribution'] = (
                                  'Population data: <a href=\"{source_url}/\">{provider}</a>{licence_attrib}'
                                  ).format(source_url  = df_datasets.loc[pop_data]['source_url'],
                                           provider    = df_datasets.loc[pop_data]['provider'],
                                           licence_attrib = licence_attrib)

if population_grid != '':
    population_raster ={}
    population_raster['data'] = '.{}'.format(df_datasets.loc[population_data]['data_file'])
    population_raster['band'] = int(df_datasets.loc[population_data]['band_if_raster'])
    population_raster['epsg'] = int(df_datasets.loc[population_data]['epsg'])
    population_raster['attribution'] = (
                                        'Population data: <a href=\"{source_url}/\">{provider}</a> '
                                        'under <a href=\"{licence_url}/\">{licence}</a>'
                                        ).format(
                                        source_url = df_datasets.loc[population_data]['source_url'],
                                        provider = df_datasets.loc[population_data]['provider'],
                                        licence_url = df_datasets.loc[population_data]['licence_url'],
                                        licence = df_datasets.loc[population_data]['licence'])
    population_raster_clipped =  '{}_clipped_{}.tif'.format(os.path.join(folderPath,'study_region',study_region,os.path.basename(population_raster['data'])[:-4]),population_raster['epsg'])
    population_raster_projected =  '{}_clipped_{}.tif'.format(os.path.join(folderPath,'study_region',study_region,os.path.basename(population_raster['data'])[:-4]),srid)

# Expand indicator datasets using area information
df_datasets['linkage_id'] = df_datasets.linkage_layer.apply(lambda x: areas[x]['id'] if str(x)!='nan' else '')
df_datasets = expand_indicators(df_datasets)

# Derived hex settings
hex_grid = '{0}_hex_{1}{2}_diag'.format(study_region,hex_diag,units)
hex_grid_buffer =  '{0}_hex_{1}{2}_diag_{3}{2}_buffer'.format(study_region,hex_diag,units,hex_buffer)
hex_side = float(hex_diag)*0.5
hex_area_km2 = ((3*math.sqrt(3.0)/2)*(hex_side)**2)*10.0**-6

# Database names -- derived from above parameters; (no need to change!)
gdb       = '{}.gdb'.format(db)
db_sde    = '{}.sde'.format(db)
gdb_path    = os.path.join(locale_dir,gdb)
db_sde_path = os.path.join(locale_dir,db_sde)
dbComment = 'Liveability indicator data for {0} {1}.'.format(locale,year)

# Environment settings for SQL
os.environ['PGHOST']     = db_host
os.environ['PGPORT']     = str(db_port)
os.environ['PGUSER']     = db_user
os.environ['PGPASSWORD'] = db_pwd
os.environ['PGDATABASE'] = db

# OSM settings
osm_data = os.path.join(folderPath,osm_data)
osm_date = str(osm_date)
osm_prefix = 'osm_{}'.format(osm_date)
osm_region = '{}_{}.osm'.format(locale,osm_prefix)

osm_source = os.path.join(folderPath,'study_region',locale,'{}_{}.osm'.format(buffered_study_region,osm_prefix))

# define pedestrian network custom filter (based on OSMnx 'walk' network type, without the cycling exclusion)
pedestrian = (
             '["area"!~"yes"]' 
             '["highway"!~"motor|proposed|construction|abandoned|platform|raceway"]'
             '["foot"!~"no"]'  
             '["service"!~"private"]' 
             '["access"!~"private"]'
             )
             
grant_query = '''GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO {0};
                 GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO {0};'''.format(db_user)



# roads
# Define network data name structures
# road_data = df_parameters.loc['road_data'][locale]  # the folder where road data is kept
network_folder = 'osm_{}_epsg{}_pedestrian_{}'.format(buffered_study_region,srid,osm_prefix)
network_source = os.path.join(locale_dir,network_folder)
intersections_table = "clean_intersections_{}m".format(intersection_tolerance)

# Sausage buffer run parameters
# If you experience 'no forward edges' issues, change this value to 1
# this means that for *subsequently processed* buffers, it will use 
# an ST_SnapToGrid parameter of 0.01 instead of 0.001
## The first pass should use 0.001, however.
snap_to_grid = 0.001
if no_forward_edge_issues == 1:
  snap_to_grid = 0.01

# Destinations data directory
# destination_list = [x for x in df_destinations.destination.tolist()] # the destinations 

df_osm_dest = df_osm_dest.replace(np.nan, 'NULL', regex=True)

# Colours for presenting maps
colours = {}
# http://colorbrewer2.org/#type=qualitative&scheme=Dark2&n=8
colours['qualitative'] = ['#1b9e77','#d95f02','#7570b3','#e7298a','#66a61e','#e6ab02','#a6761d','#666666']
# http://colorbrewer2.org/#type=diverging&scheme=PuOr&n=8
colours['diverging'] = ['#8c510a','#bf812d','#dfc27d','#f6e8c3','#c7eae5','#80cdc1','#35978f','#01665e']
        
map_style = '''
<style>
.legend {
    padding: 0px 0px;
    font: 12px sans-serif;
    background: white;
    background: rgba(255,255,255,1);
    box-shadow: 0 0 15px rgba(0,0,0,0.2);
    border-radius: 5px;
    }
.leaflet-control-attribution {
	width: 60%;
	height: auto;
	}
.leaflet-container {
    background-color:rgba(255,0,0,0.0);
}
</style>
<script>L_DISABLE_3D = true;</script>
'''    

# specify that the above modules and all variables below are imported on 'from config.py import *'
__all__ = [x for x in dir() if x not in ['area','__file__','__all__', '__builtins__', '__doc__', '__name__', '__package__']]
 
