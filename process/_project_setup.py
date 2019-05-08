# Script:  config_ntnl_li_process.py
# Liveability indicator calculation template custom configuration file
# Version: 20180907
# Author:  Carl Higgs
#
# All scripts within the process folder draw on the sources, parameters and modules
# specified in the file _project_configuration.xlsx to source and output 
# resources. It is the best definition of where resources are sourced from and 
# how the methods used have been parameterised.
#
# If you are starting a new project, you can set up the global parameters which 
# (pending overrides) should be applied for each study region in the 
#  detailed_explanation' folder.
#
# If you are adding a new study region to an existing project, this study region
# will be entered as a row in the 'study_regions' worksheet; the corresponding
# column fields must be completed as required.  See the worksheet 'detailed 
# explanation' for a description of what is expected for each field.
#
# If you are running a project on a specific computer that requires some kind of 
# override of the parameters set up above, you can **in theory** use the 
# 'local_environments' worksheet to do this.  In practice this hasn't been 
# implemented yet, and the sheet is just a placeholder for the event that such 
# overrides are required.
#
# The file which draws on the project, study region, destination and local settings 
# specificied in the _project_configuration.xlsx file and implements these across 
# scripts is THIS FILE config_ntnl_li_process.py

# import modules
import os
import sys
import time
import pandas
import subprocess as sp


# Set up locale (ie. defined at command line, or else testing)
if len(sys.argv) >= 2:
  locale = '{studyregion}'.format(studyregion = sys.argv[1])
else:
  locale = 'bangkok'
if __name__ == '__main__':
  print("\nProcessing script {} for locale {}...\n".format(sys.argv[0],locale))


# Load settings from _project_configuration.xlsx
xls = pandas.ExcelFile(os.path.join(sys.path[0],'_project_configuration.xlsx'))
df_parameters = pandas.read_excel(xls, 'Parameters',index_col=0)
df_parameters[locale] = df_parameters[locale].fillna('')
full_locale = df_parameters.loc['full_locale'][locale]

df_datasets = pandas.read_excel(xls, 'Datasets')
df_datasets.name_s = df_datasets.name_s.fillna('')
df_datasets = df_datasets[(df_datasets.purpose=='indicators') & (df_datasets.target_region=='Bangkok') & (df_datasets.name_s!='')]
df_datasets.set_index('name_s',inplace=True)

# THE FOLLOWING ALL REQUIRE UPDATING TO NEW FORMAT
# df_parameters.loc = pandas.read_excel(xls, 'study_regions',index_col=1)
df_inds = pandas.read_excel(xls, 'indicator_queries')
df_destinations = pandas.read_excel(xls, 'destinations')
df_osm = pandas.read_excel(xls, 'osm_and_open_space_defs')
df_osm_dest = pandas.read_excel(xls, 'osm_dest_definitions')

responsible = df_parameters.loc['responsible'][locale]
year   = df_parameters.loc['year'][locale]

# The main directory for data
folderPath = df_parameters.loc['folderPath'][locale]

# # Set up locale (ie. defined at command line, or else testing)
# if len(sys.argv) >= 2:
  # locale = '{studyregion}'.format(studyregion = sys.argv[1])
# else:
  # locale = 'testing'
  
 
def pretty(d, indent=0):
   for key, value in d.items():
      depth = 0
      print('\t' * indent + str(key)+':'),
      if isinstance(value, dict):
        if depth == 0:
          print(" ")
          depth+=1
        pretty(value, indent+1)
      else:
        print(' ' + str(value))
  
# More study region details

region = df_parameters.loc['region'][locale]

locale_dir = os.path.join(folderPath,'study_region','{}'.format(locale.lower()))
locale_maps = os.path.join('../maps/',locale.lower())

# Study region boundary
region_shape = df_parameters.loc['region_shape'][locale]

# SQL Query to select study region
region_where_clause = df_parameters.loc['region_where_clause'][locale]

# db suffix
suffix = df_parameters.loc['suffix'][locale]

# derived study region name (no need to change!)
study_region = '{}_{}_{}'.format(locale,region,year).lower()
db = 'li_{0}_{1}{2}'.format(locale,year,suffix).lower()

# ; Project spatial reference (for ArcGIS)
SpatialRef = df_parameters.loc['SpatialRef'][locale]

# Project spatial reference EPSG code (for Postgis)
srid       = df_parameters.loc['srid'][locale]
units      = df_parameters.loc['units'][locale]
units_full = df_parameters.loc['units_full'][locale]

# Study region buffer
study_buffer = df_parameters.loc['study_buffer'][locale]
buffered_study_region = '{}_{}{}'.format(study_region,study_buffer,units)
buffered_study_region_name = df_parameters.loc['buffered_study_region_name'][locale]

# Population
population_grid   = df_parameters.loc['pop_grid'][locale]
population_target   = df_parameters.loc['pop_target'][locale]
population_field = 'Population ({} estimate)'.format(population_target)
population_raster ={}
population_raster['data'] = '.{}'.format(df_datasets.loc[population_grid]['data_dir'])
population_raster['band'] = int(df_datasets.loc[population_grid]['band_if_raster'])
population_raster['epsg'] = int(df_datasets.loc[population_grid]['epsg'])
population_raster_clipped =  '{}_clipped_{}.tif'.format(os.path.join(folderPath,'study_region',locale,os.path.basename(population_raster['data'])[:-4]),population_raster['epsg'])
population_raster_projected =  '{}_clipped_{}.tif'.format(os.path.join(folderPath,'study_region',locale,os.path.basename(population_raster['data'])[:-4]),srid)
pop_alt_data = {}
for pop_data in list(df_datasets[['population:' in x for x in df_datasets.index]].index):
    data_type = pop_data.split(':')[1]
    pop_alt_data[data_type] = '.{}'.format(df_datasets.loc['population:district'].data_dir)
    
def reproject_raster(inpath, outpath, new_crs):
    import rasterio
    from rasterio.warp import calculate_default_transform, reproject, Resampling
    dst_crs = new_crs # CRS for web meractor 
    with rasterio.open(inpath) as src:
        transform, width, height = calculate_default_transform(
            src.crs, dst_crs, src.width, src.height, *src.bounds)
        kwargs = src.meta.copy()
        kwargs.update({
            'crs': dst_crs,
            'transform': transform,
            'width': width,
            'height': height
        })
        with rasterio.open(outpath, 'w', **kwargs) as dst:
            for i in range(1, src.count + 1):
                reproject(
                    source=rasterio.band(src, i),
                    destination=rasterio.band(dst, i),
                    src_transform=src.transform,
                    src_crs=src.crs,
                    dst_transform=transform,
                    dst_crs=dst_crs,
                    resampling=Resampling.nearest)
    
# Number of processors to use in when multiprocessing
nWorkers = df_parameters.loc['multiprocessing'][locale]

# hexagon diagonal length and buffer distance (metres)
#   -- hexagon sides will be half the length of this value
#   -- hexagon area is 3/2 * sqrt(3) * (hex_diag/2)^2
#  so with diag of 3000 m, area is 5845671.476 sq.m.
hex_diag   = df_parameters.loc['hex_diag'][locale]
hex_buffer = df_parameters.loc['hex_buffer'][locale]

# Derived hex settings - no need to change
hex_grid = '{0}_hex_{1}{2}_diag'.format(study_region,hex_diag,units)
hex_grid_buffer =  '{0}_hex_{1}{2}_diag_{3}{2}_buffer'.format(study_region,hex_diag,units,hex_buffer)
hex_side = float(hex_diag)*0.5

# SQL Settings
db_host   = df_parameters.loc['db_host'][locale]
db_port   = '{}'.format(df_parameters.loc['db_port'][locale])
db_user   = df_parameters.loc['db_user'][locale]
db_pwd    = df_parameters.loc['db_pwd'][locale]
admin_db  = df_parameters.loc['db_main'][locale]
admin_user_name = admin_db
admin_pwd = db_pwd

# Database names -- derived from above parameters; (no need to change!)
gdb       = '{}.gdb'.format(db)
db_sde    = '{}.sde'.format(db)
gdb_path    = os.path.join(locale_dir,gdb)
db_sde_path = os.path.join(locale_dir,db_sde)
dbComment = 'Liveability indicator data for {0} {1}.'.format(locale,year)


os.environ['PGHOST']     = db_host
os.environ['PGPORT']     = db_port
os.environ['PGUSER']     = db_user
os.environ['PGPASSWORD'] = db_pwd
os.environ['PGDATABASE'] = db

osm_data = os.path.join(folderPath,df_parameters.loc['osm_data'][locale])
osm_date = '{}'.format(df_parameters.loc['osm_date'][locale])
osm_prefix = 'osm_{}'.format(osm_date)
osm_region = '{}_{}.osm'.format(locale,osm_prefix)

# osm_source = df_parameters.loc['osm_source']
# osm_source = D:/ntnl_li_2018_template/data/study_region/bangkok/bangkok_thailand_2016_10000m_20181001.osm
osm_source = os.path.join(folderPath,'study_region',locale,'{}_{}.osm'.format(buffered_study_region,osm_prefix))
osmnx_retain_all = df_parameters.loc['osmnx_retain_all'][locale]
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

# Region set up
areas_of_interest = [int(x) for x in df_parameters.loc['regions_of_interest'][locale].split(',')]
areas = {}
for area in areas_of_interest + ['urban']:
  prefix = area
  if type(area) is int:
    prefix = 'region{}'.format(area)
  if df_parameters.loc['{}_data'.format(prefix)][locale] != '':
    areas[area] = {}
    for field in ['data','name','id','display']:
      if field=='data':
        # join with data path prefix
        areas[area][field] = os.path.join(folderPath,df_parameters.loc['{}_{}'.format(prefix,field)][locale])
        areas[area]['table'] = os.path.splitext(os.path.basename(areas[area]['data']))[0].lower()
      elif field=='name': 
        # split into full (f) and short (s) lower case versions; latter is safe for database use
        areas[area]['name_f'] = df_parameters.loc['{}_name'.format(prefix)][locale].split(',')[0]
        if len(df_parameters.loc['{}_name'.format(prefix)][locale].split(',')) > 1:
          areas[area]['name_s'] = df_parameters.loc['{}_name'.format(prefix)][locale].split(',')[1].lower()
        else:
          areas[area]['name_s'] = areas[area]['name_f'].lower()
      elif field=='display':
        if len('{}'.format(df_parameters.loc['{}_display'.format(prefix)][locale])) > 1:
          areas[area]['display'] = df_parameters.loc['{}_display'.format(prefix)][locale]
        else:
          areas[area]['display'] = df_parameters.loc['{}_id'.format(prefix)][locale]
      else:
        areas[area][field] = df_parameters.loc['{}_{}'.format(prefix,field)][locale]

area_filter = df_parameters.loc['area_filter_field'][locale]
area_filter_field = df_parameters.loc['area_filter_field'][locale]
area_filter_value = df_parameters.loc['area_filter_value'][locale]
area_analysis  = areas[df_parameters.loc['analysis_scale'][locale]]['name_s']
analysis_field = areas[df_parameters.loc['analysis_scale'][locale]]['name_f']

# Point data locations used for sampling
# Note that the process assumes we have already transformed points to the project's spatial reference
# Point data locations (e.g. GNAF address point features)
points = 'sample_points'
points_id = df_parameters.loc['points_id'][locale]

# roads
# Define network data name structures
# road_data = df_parameters.loc['road_data'][locale]  # the folder where road data is kept
network_folder = 'osm_{}_epsg{}_pedestrian_{}'.format(buffered_study_region,srid,osm_prefix)
network_source = os.path.join(locale_dir,network_folder)
network_edges = df_parameters.loc['network_edges'][locale]
network_junctions = df_parameters.loc['network_junctions'][locale]

# network
# sausage buffer network size  -- in units specified above
distance = df_parameters.loc['distance'][locale]

# intersection tolerance
intersection_tolerance = df_parameters.loc['intersection_tolerance'][locale]
intersections_table = "clean_intersections_{}m".format(intersection_tolerance)

# search tolderance (in units specified above; features outside tolerance not located when adding locations)
# NOTE: may need to increase if no locations are found
tolerance = df_parameters.loc['tolerance'][locale]
 
# buffer distance for network lines as sausage buffer  
line_buffer = df_parameters.loc['line_buffer'][locale]

# Threshold paramaters
soft_threshold_slope = df_parameters.loc['soft_threshold_slope'][locale]

# Island exceptions are defined using ABS constructs in the project configuration file.
# They identify contexts where null indicator values are expected to be legitimate due to true network isolation, 
# not connectivity errors. 
# For example, for Rottnest Island in Western Australia: sa1_maincode IN ('50702116525')
island_exception = df_parameters.loc['island_exception'][locale]

# Sausage buffer run parameters
# If you experience 'no forward edges' issues, change this value to 1
# this means that for *subsequently processed* buffers, it will use 
# an ST_SnapToGrid parameter of 0.01 instead of 0.001
## The first pass should use 0.001, however.
no_foward_edge_issues = df_parameters.loc['no_forward_edge_issues'][locale]
snap_to_grid = 0.001
if no_foward_edge_issues == 1:
  snap_to_grid = 0.01

# Areas of Open Space
aos_threshold = df_parameters.loc['aos_threshold'][locale]
    
# Destinations - locate destinations.gdb within dest_dir (ie. 'D:\ntnl_li_2018\data\destinations\' or whereever your ntnl_li_2018 folder is located)
# Destinations data directory
dest_dir = os.path.join(folderPath,df_parameters.loc['dest_dir'][locale])
destination_id = df_parameters.loc['destination_id'][locale]

study_destinations = 'study_destinations'

# array / list of destinations 
# IMPORTANT -- These are specified in the 'destinations' worksheet of the _project_configuration.xlsx file
#               - specify: destination, domain, cutoff and count distances as required
#
#           -- If new destinations are added, they should be appended to end of list 
#              to ensure this order is respected across time.
#
# The table 'dest_type' will be created in Postgresql to keep track of destinations

df_destinations = df_destinations.replace(pandas.np.nan, 'NULL', regex=True)
destination_list = [x for x in df_destinations.destination.tolist()] # the destinations 

df_osm_dest = df_osm_dest.replace(pandas.np.nan, 'NULL', regex=True)

# Colours for presenting maps
colours = {}
# http://colorbrewer2.org/#type=qualitative&scheme=Dark2&n=8
colours['qualitative'] = ['#1b9e77','#d95f02','#7570b3','#e7298a','#66a61e','#e6ab02','#a6761d','#666666']
# http://colorbrewer2.org/#type=diverging&scheme=PuOr&n=8
colours['diverging'] = ['#8c510a','#bf812d','#dfc27d','#f6e8c3','#c7eae5','#80cdc1','#35978f','#01665e']

def style_dict_fcn(type = 'qualitative',colour=0):
    if type not in ['qualitative','diverging']:
        print("Specified type unknown; assuming 'qualitative'.")
        type = 'qualitative'
    return {
        'fillOpacity': 0.5,
        'line_opacity': 0.2,
        'fillColor': colours[type][colour],
        'lineColor': colours[type][colour]
    }

def folium_to_png(locale_maps,map_name,width=1000,height=800,pause=3):
    import selenium.webdriver
    try:
        options=selenium.webdriver.firefox.options.Options()
        options.add_argument('--headless')
        driver = selenium.webdriver.Firefox(options=options)
        driver.set_window_size(width, height)  # choose a resolution
        driver.get('file:///{}/{}/{}.html'.format(os.getcwd(),locale_maps,map_name))
        # You may need to add time.sleep(seconds) here
        time.sleep(pause)
        # Remove zoom controls from snapshot
        for leaflet_class in ["leaflet-control-zoom","leaflet-control-layers"]:
            element = driver.find_element_by_class_name(leaflet_class)
            driver.execute_script("""
            var element = arguments[0];
            element.parentNode.removeChild(element);
            """, element)
        driver.save_screenshot('{}/{}.png'.format(locale_maps,map_name))
        driver.close()
    except:
        print("Export of {} failed.".format('{}/{}.png'.format(locale_maps,map_name)))
        
legend_style = '''
<style>
.legend {
    padding: 0px 0px;
    font: 10px sans-serif;
    background: white;
    background: rgba(255,255,255,1);
    box-shadow: 0 0 15px rgba(0,0,0,0.2);
    border-radius: 5px;
    }
</style>
'''        

# specify that the above modules and all variables below are imported on 'from config.py import *'
__all__ = [x for x in dir() if x not in ['__file__','__all__', '__builtins__', '__doc__', '__name__', '__package__']]
 
