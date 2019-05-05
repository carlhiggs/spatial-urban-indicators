# Import population raster and convert to polygons

import rasterio
from rasterio.mask import mask
import geopandas as gpd
from geoalchemy2 import Geometry, WKTElement
import folium
from folium import plugins
import branca
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

# ... and the areas in this region
for admin_area in areas: 
    analysis_area = gpd.GeoDataFrame.from_postgis('''SELECT "{}",geom FROM {}'''.format(areas[admin_area]['id'],
                                                                                      areas[admin_area]['name_s']),
                                                engine, 
                                                geom_col='geom', 
                                                index_col=areas[admin_area]['id'])
    
    area_json = [json.loads(analysis_area.to_json())['features']][0]
    
    # create null field for population values
    analysis_area['population'] = np.nan    
    analysis_area['population'].astype('Int64', inplace=True)
    # associate analysis_area with aggregate population estimates
    pop = 0
    for area in area_json:
        area_name = area['id']
        subraster, bounds = mask(dataset = raster_pop, 
                                shapes  = [area['geometry']],
                                nodata = nodata)
        area_pop = int(np.sum(subraster[subraster>nodata]))
        # print('{}: {}'.format(area_name,area_pop))
        pop += area_pop
        analysis_area.loc[area_name,'population'] = area_pop
    # create temp table for re-linkage of indicator with area back in postgis
    analysis_area['population'].to_sql('temp', 
                         engine, 
                         if_exists='replace', 
                         index=True)
    
    engine.execute('''
    ALTER TABLE {table} ADD COLUMN IF NOT EXISTS "population" int;
    ALTER TABLE {table} ADD COLUMN IF NOT EXISTS "{population_field}" text;
    ALTER TABLE {table} ADD COLUMN IF NOT EXISTS "{population_field} per hectare" double precision;
    UPDATE {table} a
        SET 
            population = temp.population,
            "{population_field}" = TO_CHAR(temp.population, '999,999'),
            "{population_field} per hectare" = (temp.population/area_ha)::double precision
        FROM temp 
        WHERE a."{id}" = temp."{id}";
    '''.format(table = areas[admin_area]['name_s'],
               id = areas[admin_area]['id'],
               population_field = population_field))
               
print('Estimated population for {} study region in {}'
      ' based on UN adjusted WorldPop data is {:,}.'.format(full_locale,population_target,pop))

# get map data
map_layers={}

sql = '''SELECT "Description", geom_4326 geom FROM {}'''.format(buffered_study_region)
map_layers['buffer'] = gpd.GeoDataFrame.from_postgis(sql, engine, geom_col='geom' )

sql = '''
SELECT "{id}",
       "{analysis_field}",
       population,
       "{population_field}",
       ROUND("{population_field} per hectare"::numeric,2) "{population_field} per hectare",
       geom_4326 geom
FROM {table}
'''.format(id =areas[0]['id'],analysis_field = analysis_field,table = area_analysis, population_field=population_field)
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
m.add_tile_layer(tiles='Stamen Toner',name='simple map', active=True)
# add layers (not true choropleth - for this it is just a convenient way to colour polygons)

buffer = folium.Choropleth(map_layers['buffer'].to_json(),
                           name='10km study region buffer',
                           fill_color=colours['qualitative'][1],
                           fill_opacity=0,
                           line_color=colours['qualitative'][1], 
                           highlight=False).add_to(m)

bins = list(map_layers[areas[0]['name_s']]['population'].quantile([0, 0.25, 0.5, 0.75, 1]))
population_layer = folium.Choropleth(data=map_layers[areas[0]['name_s']],
                  geo_data =map_layers[areas[0]['name_s']].to_json(),
                  name = population_field,
                  columns =[areas[0]['id'],'population'],
                  key_on="feature.properties.{}".format(areas[0]['id']),
                  fill_color='YlGn',
                  fill_opacity=0.7,
                  line_opacity=0.2,
                  legend_name=population_field,
                  # bins=bins,
                  reset=True,
                  overlay = True,
                  show=True
                  ).add_to(m)
                            
folium.features.GeoJsonTooltip(fields=[areas[0]['name_f'],population_field],
                               labels=True, 
                               sticky=True
                              ).add_to(population_layer.geojson)                          
                              
m.add_child(folium.raster_layers.ImageOverlay(map_layers['population'][0], 
                                 name='Poplulation per pixel (WorldPop predicted model: {}, UN adjusted)'.format(population_target),
                                 opacity=.7,
                                 bounds=[[bounds['miny'],bounds['minx']], 
                                         [bounds['maxy'], bounds['maxx']]],
                                 colormap=lambda x: (1, 0, x, x),#R,G,B,alpha,
                                 overlay=True
                                 ))                              
                              
folium.LayerControl(collapsed=True).add_to(m)

# checkout https://nbviewer.jupyter.org/gist/jtbaker/57a37a14b90feeab7c67a687c398142c?flush_cache=true
# save map
map_name = '{}_02_population_{}.html'.format(locale,population_target)
m.save('../maps/{}'.format(map_name))

# initialise map
m = folium.Map(location=xy, zoom_start=11,tiles=None, control_scale=True, prefer_canvas=True)
m.add_tile_layer(tiles='Stamen Toner',name='simple map', active=True)
# add layers (not true choropleth - for this it is just a convenient way to colour polygons)

buffer = folium.Choropleth(map_layers['buffer'].to_json(),
                           name=buffered_study_region_name,
                           fill_color=colours['qualitative'][1],
                           fill_opacity=0,
                           line_color=colours['qualitative'][1], 
                           highlight=False).add_to(m)

bins = list(map_layers[areas[0]['name_s']]['population'].quantile([0, 0.25, 0.5, 0.75, 1]))

density_layer = folium.Choropleth(data=map_layers[areas[0]['name_s']],
                  geo_data =map_layers[areas[0]['name_s']].to_json(),
                  name = '{} per hectare'.format(population_field),
                  columns =[areas[0]['id'],'{} per hectare'.format(population_field)],
                  key_on="feature.properties.{}".format(areas[0]['id']),
                  fill_color='YlGn',
                  fill_opacity=0.7,
                  line_opacity=0.2,
                  legend_name='{} per hectare'.format(population_field),
                  # bins=bins,
                  reset=True,
                  overlay = True,
                  ).add_to(m)
                            
folium.features.GeoJsonTooltip(fields=[areas[0]['name_f'],'{} per hectare'.format(population_field)],
                               labels=True, 
                               sticky=True
                              ).add_to(density_layer.geojson)                              
                              
m.add_child(folium.raster_layers.ImageOverlay(map_layers['population'][0], 
                                 name='Poplulation per pixel (WorldPop predicted model: {}, UN adjusted)'.format(population_target),
                                 opacity=.7,
                                 bounds=[[bounds['miny'],bounds['minx']], 
                                         [bounds['maxy'], bounds['maxx']]],
                                 colormap=lambda x: (1, 0, x, x),#R,G,B,alpha,
                                 overlay=True
                                 ))                              
                              
folium.LayerControl(collapsed=True).add_to(m)

# checkout https://nbviewer.jupyter.org/gist/jtbaker/57a37a14b90feeab7c67a687c398142c?flush_cache=true
# save map
map_name = '{}_02_population_density_{}.html'.format(locale,population_target)
m.save('../maps/{}'.format(map_name))
print("\nPlease inspect results using interactive map saved in project maps folder: {}\n".format(map_name))              
 
# # output to completion log					
script_running_log(script, task, start, locale)
engine.dispose()
