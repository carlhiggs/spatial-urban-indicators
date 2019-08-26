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
df_datasets = pandas.read_excel(xls, 'Datasets')
df_inds = pandas.read_excel(xls, 'indicator_queries')
df_destinations = pandas.read_excel(xls, 'destinations')
df_osm = pandas.read_excel(xls, 'osm_and_open_space_defs')
df_osm_dest = pandas.read_excel(xls, 'osm_dest_definitions')

# prepare and clean configuration entries
df_parameters[locale] = df_parameters[locale].fillna('')
for var in [x for x in  df_parameters.index.values]:
    globals()[var] = df_parameters.loc[var][locale]
# full_locale = df_parameters.loc['full_locale'][locale]
df_datasets.name_s = df_datasets.name_s.fillna('')
df_datasets = df_datasets[(df_datasets.purpose=='indicators') & (df_datasets.target_region==full_locale) & (df_datasets.name_s!='')]
df_datasets.set_index('name_s',inplace=True)

# derived study region name (no need to change!)
study_region = '{}_{}_{}'.format(locale,region,year).lower()
db = 'li_{0}_{1}{2}'.format(locale,year,suffix).lower()

# region specific output locations
locale_dir = os.path.join(folderPath,'study_region','{}'.format(study_region))
locale_maps = os.path.join('../maps/',study_region)

# Study region buffer
buffered_study_region = '{}_{}{}'.format(study_region,study_buffer,units)

# sample points
points = '{}_{}m'.format(points,point_sampling_interval)

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
    areas[area]['data'] = df_datasets[df_datasets.index== area_meta['area_datasets'][idx]].data_dir.values[0]
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

# An SQL query to define the field's display format for mapping
# 

# Population
population_field = 'Population ({} estimate)'.format(population_target)

population_linkage = {}
for pop_data in list(df_datasets[['population:' in x for x in df_datasets.index]].index):
    data_type = pop_data.split(':')[1]
    population_linkage[data_type] = {}
    population_linkage[data_type]['data'] = '.{}'.format(df_datasets.loc[pop_data].data_dir)
    population_linkage[data_type]['year_target'] = df_datasets.loc[pop_data].year_target
    population_linkage[data_type]['linkage'] = '{}'.format(df_datasets.loc[pop_data].index_if_tabular)
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
    population_raster['data'] = '.{}'.format(df_datasets.loc[population_data]['data_dir'])
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
dest_dir = os.path.join(folderPath,dest_dir)
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

## need to modify this to also allow to pdf -- perhaps using pdfkit
# https://stackoverflow.com/questions/54390417/how-to-download-a-web-page-as-a-pdf-using-python
# I think in future should use puppeteer with headless chrome
# (or pyppeteer)
def folium_to_image(input_dir='',output_dir='',map_name='',formats=['png'],width=1000,height=800,pause=3,strip_elements=["leaflet-control-zoom","leaflet-control-layers"]):
    import selenium.webdriver
    try:
        if (input_dir=='' or map_name==''):
            raise Exception(('This function requires specification of an input directory.\n'
                   'Please specify the function in the following form:\n'
                   'folium_to_png(input_dir,output_dir,map_name,[["format","format"]],[width],[height],[pause])'
                   ))
            return
        if output_dir=='':
            output_dir = input_dir
        options=selenium.webdriver.firefox.options.Options()
        options.add_argument('--headless')
        driver = selenium.webdriver.Firefox(options=options)
        driver.set_window_size(width, height)  # choose a resolution
        driver.get('file:///{}/{}/{}.html'.format(os.getcwd(),input_dir,map_name))
        # You may need to add time.sleep(seconds) here
        time.sleep(pause)
        # Remove zoom controls from snapshot
        for leaflet_class in strip_elements:
            element = driver.find_element_by_class_name(leaflet_class)
            driver.execute_script("""
            var element = arguments[0];
            element.parentNode.removeChild(element);
            """, element)
        if 'png' in formats:
            driver.save_screenshot('{}/{}.png'.format(output_dir,map_name))
        # if 'pdf' in formats:
            # import pdfkit
            # with open("{}/__folium_temp.html".format(output_dir), "w") as f:
                # f.write(driver.page_source)
            # pdfkit.from_file("{}/__folium_temp.html".format(output_dir), 
                             # '{}/{}.pdf'.format(output_dir,map_name))
            # os.remove("{}/__folium_temp.html".format(output_dir))
        driver.close()
    except Exception as error:
        print("Export of {} failed.".format('{}/{}.png: {}'.format(output_dir,map_name,error)))
        
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
    
# function for printing dictionaries in 'pretty' format to screen 
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

def table_exists(name):
    ret = engine.dialect.has_table(engine, name)
    print('Table "{}" exists: {}'.format(name, ret))
    return ret

# function for returning a pandas type given a string value representing that type
def valid_type(str_of_type):
    if str_of_type in ['int','integer']:
        return('Int64')
    elif str_of_type in ['float','double precision']:
        return('float64')
    elif str_of_type in ['str','string','text','object']:
        return('object')
    else:
        return('object')

# specify that the above modules and all variables below are imported on 'from config.py import *'
__all__ = [x for x in dir() if x not in ['__file__','__all__', '__builtins__', '__doc__', '__name__', '__package__']]
 
