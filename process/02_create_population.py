# Import population raster and convert to polygons

import rasterio
from rasterio.mask import mask
import geopandas as gpd
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
                                             index_col=areas[0]['id'],
                                             dtype={'geom': Geometry('POLYGON', srid=srid))

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
subdistricts.to_sql(areas[0]['name_s'], 
                    engine, 
                    if_exists='replace', 
                    index=True, 
                    dtype={'geom': Geometry('POLYGON', srid=srid)})
print('Estimated population for Bangkok study region in 2020'
      ' based on UN adjusted WorldPop data is {}.'.format(pop))
           
# get map data
map_layers={}

sql = '''
SELECT '10km study region buffer' AS "Description",
       ST_Transform(geom,4326) geom 
FROM {}
'''.format(buffered_study_region)
map_layers['buffer'] = gpd.GeoDataFrame.from_postgis(sql, engine, geom_col='geom' )

sql = '''
SELECT "{id}" As "Subdistrict",
         population,
         ST_Transform(geom,4326) geom 
FROM {table}
'''.format(id = 'ADM3_EN',table = areas[0]['name_s'])
map_layers[areas[0]['name_s']] = gpd.GeoDataFrame.from_postgis(sql, engine, geom_col='geom', index_col='Subdistrict')

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
                            
folium.features.GeoJsonTooltip(fields=['Subdistrict','population'],
                               labels=True, 
                               sticky=True
                              ).add_to(feature.geojson)

m.add_child(folium.raster_layers.ImageOverlay(map_layers['population'][0], 
                                 name='Poplulation per pixel (WorldPop predicted model: 2020, UN adjusted)',
                                 opacity=.7,
                                 bounds=[[bounds['miny'],bounds['minx']], 
                                         [bounds['maxy'], bounds['maxx']]],
                                 colormap=lambda x: (1, 0, x, x),#R,G,B,alpha
                                 ))

folium.LayerControl(collapsed=True).add_to(m)

# checkout https://nbviewer.jupyter.org/gist/jtbaker/57a37a14b90feeab7c67a687c398142c?flush_cache=true
# save map
map_name = '02_population.html'
m.save('../maps/{}'.format(map_name))
print("\nPlease inspect results using interactive map saved in project maps folder: {}\n".format(map_name))              
              
# pop_vector = gpd.GeoDataFrame.from_postgis('''SELECT * FROM {table}'''.format(id = 'Adm3Name',table = areas[0]['name_s']), engine, geom_col='geom' )   

# with rasterio.open(population_raster['data']) as src:
    # # set pop_vector to match crs of input raster
    # # the above works as tested (raster is epsg 4326)
    # # in theory, works if epsg is otherwise detectable in rasterio
    # pop_vector.to_crs({'init':test.crs['init']},inplace=True)
    

    
     # out_image, out_transform = mask(src, geoms, crop=True)
                                                                   
# gdf.to_crs(epsg=4326, inplace=True) 


# if src_ds is None:
    # print('Unable to open {}'.format(src_filename))
    # sys.exit(1)

# try:
    # srcband = src_ds.GetRasterBand(population_raster[1])
# except RuntimeError as e:
    # # for example, try GetRasterBand(10)
    # print('Band ( {} ) not found'.format(population_raster[1]))
    # print(e)
    # sys.exit(1)

# #
# #  create output datasource
# #
# dst_layername = population_grid
# drv = ogr.GetDriverByName("ESRI Shapefile")
# dst_ds = drv.CreateDataSource( dst_layername + ".shp" )
# dst_layer = dst_ds.CreateLayer(dst_layername, srs = None )

# gdal.Polygonize( srcband, None, dst_layer, -1, [], callback=None )


# https://postgis.net/docs/RT_ST_PixelAsPolygons.html

# # output to completion log					
script_running_log(script, task, start, locale)
engine.dispose()
