# Import population raster and convert to polygons

import rasterio
from rasterio.mask import mask
import geopandas as gpd
from geoalchemy2 import Geometry, WKTElement
import folium
from folium import plugins
from sqlalchemy import create_engine
import numpy as np
import json
from script_running_log import script_running_log
# Import custom variables for National Liveability indicator process
from _project_setup import *

# simple timer for log file
start  = time.time()
script = os.path.basename(sys.argv[0])
task = 'Import population raster and associate with administrative areas'

engine = create_engine("postgresql://{user}:{pwd}@{host}/{db}".format(user = db_user,
                                                                      pwd  = db_pwd,
                                                                      host = db_host,
                                                                      db   = db))                                                            

clipping_boundary = gpd.GeoDataFrame.from_postgis('''SELECT geom FROM {table}'''.format(table = buffered_study_region), engine, geom_col='geom' )   

# clip and save raster
with rasterio.open(population_raster['data']) as full_raster:
    # set pop_vector to match crs of input raster
    # the above works as tested (raster is epsg 4326)
    # in theory, works if epsg is otherwise detectable in rasterio
    clipping_boundary.to_crs({'init':full_raster.crs['init']},inplace=True)
    coords = [json.loads(clipping_boundary.to_json())['features'][0]['geometry']]
    out_img, out_transform = mask(full_raster, coords, crop=True)
    out_meta = full_raster.meta.copy()
    out_meta.update({
                    "driver": "GTiff",
                    "height": out_img.shape[1],
                    "width":  out_img.shape[2],
                    "transform": out_transform
                    }) 
                    
with rasterio.open(population_raster_clipped, "w", **out_meta) as dest:
    dest.write(out_img)    

# reproject and save the re-projected clipped raster
# (see config file for reprojection function)
reproject_raster(inpath = population_raster_clipped, 
              outpath = population_raster_projected, 
              new_crs = 'EPSG:{}'.format(srid))   


# Now, we aggregate population in each subdistrict from population grid

# Load up the clipped and projected raster population
raster_pop = rasterio.open(population_raster_projected)    
nodata = raster_pop.nodata
# ... and the subdistricts 
subdistricts = gpd.GeoDataFrame.from_postgis(areas[0]['name_s'],
                                             engine, 
                                             geom_col='geom', 
                                             index_col=areas[0]['id'])

area_json = [json.loads(subdistricts.to_json())['features']][0]

# create null field for population values
subdistricts['population'] = np.nan    
subdistricts['population'].astype('Int64', inplace=True)
# associate subdistricts with aggregate population estimates
pop = 0
for area in area_json:
    area_name = area['id']
    subraster, bounds = mask(dataset = raster_pop, 
                             shapes  = [area['geometry']],
                             nodata = nodata)
    area_pop = int(np.sum(subraster[subraster>nodata]))
    # print('{}: {}'.format(area_name,area_pop))
    pop += area_pop
    subdistricts.loc[area_name,'population'] = area_pop
# Replace subdistricts table in project Postgis database
# Create WKT geometry (postgis won't read shapely geometry)
subdistricts['geom'] = subdistricts['geom'].apply(lambda x: WKTElement(x.wkt, srid=srid))
subdistricts.to_sql(areas[0]['name_s'], 
                    engine, 
                    if_exists='replace', 
                    index=True,
                    dtype={'geom': Geometry('POLYGON', srid=srid)})
print('Estimated population for {} study region in {}'
      ' based on UN adjusted WorldPop data is {:,}.'.format(full_locale,population_target,pop))
           
# get map data
map_layers={}

sql = '''
SELECT '10km study region buffer' AS "Description",
       ST_Transform(geom,4326) geom 
FROM {}
'''.format(buffered_study_region)
map_layers['buffer'] = gpd.GeoDataFrame.from_postgis(sql, engine, geom_col='geom' )

population_field = 'Population (2020 estimate)'
sql = '''
SELECT "ADM3_TH"||' ('||"{id}"||')' As "Subdistrict",
       TO_CHAR(population, '999,999') "{population_field}",
       ST_Transform(geom,4326) geom 
FROM {table}
'''.format(id = 'ADM3_EN',table = areas[0]['name_s'], population_field=population_field)
map_layers[areas[0]['name_s']] = gpd.GeoDataFrame.from_postgis(sql, engine, geom_col='geom')

# load up the reprojected raster
with rasterio.open(population_raster_clipped) as src:
    boundary = src.bounds
    map_layers['population'] = src.read()
    nodata = src.nodata
    
xy = [float(map_layers['buffer'].centroid.y),float(map_layers['buffer'].centroid.x)]  
bounds = map_layers['buffer'].bounds.transpose().to_dict()[0]

# initialise map
m = folium.Map(location=xy, zoom_start=11,tiles=None, control_scale=True, prefer_canvas=True)
m.add_tile_layer(tiles='Stamen Toner',name='simple map', overlay=True,active=True)
# add layers (not true choropleth - for this it is just a convenient way to colour polygons)
buffer = folium.Choropleth(map_layers['buffer'].to_json(),
                           name='10km study region buffer',
                           fill_color=colours['qualitative'][1],
                           fill_opacity=0,
                           line_color=colours['qualitative'][1], 
                           highlight=False).add_to(m)

feature = folium.Choropleth(map_layers[areas[0]['name_s']].to_json(),
                            name=str.title(areas[0]['name_f']),
                            fill_opacity=0,
                            line_color=colours['qualitative'][0], 
                            highlight=False).add_to(m)
                            
folium.features.GeoJsonTooltip(fields=['Subdistrict',population_field],
                               labels=True, 
                               sticky=True
                              ).add_to(feature.geojson)

m.add_child(folium.raster_layers.ImageOverlay(map_layers['population'][0], 
                                 name='Poplulation per pixel (WorldPop predicted model: {}, UN adjusted)'.format(population_target),
                                 opacity=.7,
                                 bounds=[[bounds['miny'],bounds['minx']], 
                                         [bounds['maxy'], bounds['maxx']]],
                                 colormap=lambda x: (1, 0, x, x),#R,G,B,alpha
                                 ))

folium.LayerControl(collapsed=True).add_to(m)

# checkout https://nbviewer.jupyter.org/gist/jtbaker/57a37a14b90feeab7c67a687c398142c?flush_cache=true
# save map
map_name = '{}_02_population.html'.format(locale)
m.save('../maps/{}'.format(map_name))
print("\nPlease inspect results using interactive map saved in project maps folder: {}\n".format(map_name))              
 
# # output to completion log					
script_running_log(script, task, start, locale)
engine.dispose()
