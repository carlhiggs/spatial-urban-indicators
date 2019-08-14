# Import population raster and calculate values for polygons

import rasterio
from rasterio.mask import mask
import geopandas as gpd
from geoalchemy2 import Geometry, WKTElement
import folium
from folium import plugins
import branca
from sqlalchemy import create_engine
import psycopg2
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

if population_linkage != {}:
    heading = "Population statistics, {}".format(population_linkage[analysis_scale]['year_target'])
    population = pandas.read_csv(population_linkage[analysis_scale]['data'],index_col=population_linkage[analysis_scale]['linkage']) 
    population_numeric = [c for c in population.columns if np.issubdtype(population[c].dtype, np.number)]
    pop_data_fields = population_map_fields.split(',')
    pop_data_fields_full = ['area_sqkm']
    pop_data_fields_to_map = []
    for f in pop_data_fields:
        pop_data_fields_full.append(f)
        if f in population_numeric:
            pop_data_fields_full.append('{} per sqkm'.format(f))
            pop_data_fields_to_map.append('{} per sqkm'.format(f))
    column_names = {}
    for f in pop_data_fields_full:
        column_names[f] = f.replace('sqkm','km\u00B2')
    map_attribution = '{} | {} | {}'.format(map_attribution,areas[area]['attribution'],population_linkage[analysis_scale]['attribution'])
    map_data={}
    tables    = [buffered_study_region,study_region]
    fields    = ["Study region buffer","Study region"]
    names     =  [buffered_study_region_name,'Study region']
    opacity   =  [0,0.4]
    highlight =  [False,False]
    for i in range(0,len(tables)):
        table = tables[i]
        field = fields[i]
        sql = '''SELECT "{}",geom_4326 geom FROM {}'''.format(field,table)
        map_data[table] = gpd.GeoDataFrame.from_postgis(sql, engine, geom_col='geom' )
    
    for area in areas:
        sql = '''
        SELECT {area},
               {data_fields}
               ST_Transform(geom, 4326) AS geom 
        FROM {area} a
        '''.format(area = area,
                   data_fields = '"{}",'.format('","'.join(pop_data_fields_full)))
        map_data[area] = gpd.GeoDataFrame.from_postgis(sql, engine, geom_col='geom')
        map_data[area].rename(columns = column_names, inplace=True)
        map_data[area].rename(columns = {'area_km\u00B2':'area (km\u00B2)'}, inplace=True)
    data_fields =[f.replace('sqkm','km\u00B2').replace('area_km\u00B2','area (km\u00B2)') for f in pop_data_fields_full]
    map_fields =[f.replace('sqkm','km\u00B2').replace('area_km\u00B2','area (km\u00B2)') for f in pop_data_fields_to_map]
    xy = [float(map_data[buffered_study_region].centroid.y),float(map_data[buffered_study_region].centroid.x)]  
    bounds = map_data[buffered_study_region].bounds.transpose().to_dict()[0]
    
    # Population map
    for field in map_fields:
        for area in areas:
          # this kind of map does not make sense for an overall summary
          if len(map_data[area].index.values) > 1:
            map_name = '{}_02_population_{}_{}'.format(locale,area,field.replace('km\u00B2','sqkm').replace(' ','_'))
            print("{}...".format(map_name))           
            m = folium.Map(location=xy, zoom_start=11,tiles=None, control_scale=True, prefer_canvas=True)
            # folium.CustomPane(name="basemaps", z_index=625, pointer_events=False).add_to(m)
            # folium.CustomPane(name="data", z_index=625, pointer_events=True).add_to(m)
            folium.TileLayer(tiles='Stamen Toner',
                            name='simple map', 
                            active=True,
                            # opacity = 0.5,
                            control=False,
                            overlay=True,
                            attr=((
                                " {} | "
                                "Map tiles: <a href=\"http://stamen.com/\">Stamen Design</a>, " 
                                "under <a href=\"http://creativecommons.org/licenses/by/3.0\">CC BY 3.0</a>, featuring " 
                                "data by <a href=\"https://wiki.osmfoundation.org/wiki/Licence/\">OpenStreetMap</a>, "
                                "under ODbL.").format(map_attribution))
                            ).add_to(m)
            # folium.TileLayer(tiles='OpenStreetMap',
                            # name='OpenStreetMap', 
                            # attr=((
                                # " {} | "
                                # "Map tiles: <a href=\"http://openstreetmap.org/\">© OpenStreetMap contributors</a>, " 
                                # "under <a href=\"http://creativecommons.org/licenses/by/3.0\">CC BY 3.0</a>, featuring " 
                                # "data by <a href=\"https://wiki.osmfoundation.org/wiki/Licence/\">OpenStreetMap</a>, "
                                # "under ODbL.").format(map_attribution))
                                    # ).add_to(m)
            map_layers={}                   
            map_layers[area] = folium.Choropleth(data = map_data[area],
                                                 geo_data =map_data[area].to_json(),
                                                 name = '{} ({})'.format(field,area),
                                                 columns =[area,field],
                                                 key_on="feature.properties.{}".format(area),
                                                 fill_color='YlGn',
                                                 fill_opacity=0.7,
                                                 line_opacity=0.2,
                                                 legend_name='{}, by {}'.format(field,area),
                                                 reset=True,
                                                 overlay = False
                               ).add_to(m)
            folium.features.GeoJsonTooltip(fields=[area]+data_fields,
                                        localize=True,
                                        labels=True, 
                                        sticky=True
                                        ).add_to(map_layers[area].geojson)    
            # folium.LayerControl(collapsed=True).add_to(m)
            m.fit_bounds(m.get_bounds())
            m.get_root().html.add_child(folium.Element(map_style))
            # Modify map heading (above legend)
            html = m.get_root().render()
            color_map =  re.search(r"color_map_[a-zA-Z0-9_]*\b|$",html).group()
            old = '{}.svg = d3.select(".legend.leaflet-control").append("svg")'.format(color_map)
            new = '''
            {color_map}.title = d3.select(".legend.leaflet-control").append("div")
                    .attr("style",'vertical-align: text-top;font-weight: bold;')
                    .text("{heading}");
            {color_map}.svg = d3.select(".legend.leaflet-control").append("svg")
            '''.format(color_map=color_map,heading=heading)
            html = html.replace(old,new)
            # save map
            m.save('{}/html/{}.html'.format(locale_maps,map_name))
            folium_to_image(input_dir  = os.path.join(locale_maps,'html'),
                            output_dir = os.path.join(locale_maps,'png'),
                            map_name = map_name,
                            strip_elements=["leaflet-control-zoom"])
        print("\n")

# # The following relates to previous code where raster grid was used for population
# # This approach is not used in revised approach for this project; and the below 
# # has not yet been confirmed to work  - so, disabled using following variable:
# raster_code_verified = False
# if population_grid != '':
  # if not raster_code_verified:
    # print("Population grid variable has been defined, however more work needs to be done to verify that the code implementing this works; once this has been done please update script for creating population to remove the check which prints this message."
  # else:
    # clipping_boundary = gpd.GeoDataFrame.from_postgis('''SELECT geom FROM {table}'''.format(table = buffered_study_region), engine, geom_col='geom' )   

    # # clip and save raster
    # with rasterio.open(population_raster['data']) as full_raster:
        # # set pop_vector to match crs of input raster
        # # the above works as tested (raster is epsg 4326)
        # # in theory, works if epsg is otherwise detectable in rasterio
        # clipping_boundary.to_crs({'init':full_raster.crs['init']},inplace=True)
        # coords = [json.loads(clipping_boundary.to_json())['features'][0]['geometry']]
        # out_img, out_transform = mask(full_raster, coords, crop=True)
        # out_meta = full_raster.meta.copy()
        # out_meta.update({
                        # "driver": "GTiff",
                        # "height": out_img.shape[1],
                        # "width":  out_img.shape[2],
                        # "transform": out_transform
                        # }) 
                        
    # with rasterio.open(population_raster_clipped, "w", **out_meta) as dest:
        # dest.write(out_img)    

    # # reproject and save the re-projected clipped raster
    # # (see config file for reprojection function)
    # reproject_raster(inpath = population_raster_clipped, 
                  # outpath = population_raster_projected, 
                  # new_crs = 'EPSG:{}'.format(srid))   


    # # Now, we aggregate population in each subdistrict from population grid

    # # Load up the clipped and projected raster population
    # raster_pop = rasterio.open(population_raster_projected)    
    # nodata = raster_pop.nodata

    # # ... and the areas in this region
    # for admin_area in areas: 
        # analysis_area = gpd.GeoDataFrame.from_postgis('''SELECT "{}",geom FROM {}'''.format(areas[admin_area]['id'],
                                                                                          # areas[admin_area]['name_s']),
                                                    # engine, 
                                                    # geom_col='geom', 
                                                    # index_col=areas[admin_area]['id'])
        
        # area_json = [json.loads(analysis_area.to_json())['features']][0]
        
        # # create null field for population values
        # analysis_area['population'] = np.nan    
        # analysis_area['population'].astype('Int64', inplace=True)
        # # associate analysis_area with aggregate population estimates
        # pop = 0
        # for area in area_json:
            # area_name = area['id']
            # subraster, bounds = mask(dataset = raster_pop, 
                                    # shapes  = [area['geometry']],
                                    # nodata = nodata)
            # area_pop = int(np.sum(subraster[subraster>nodata]))
            # # print('{}: {}'.format(area_name,area_pop))
            # pop += area_pop
            # analysis_area.loc[area_name,'population'] = area_pop
        # # create temp table for re-linkage of indicator with area back in postgis
        # analysis_area['population'].to_sql('temp', 
                             # engine, 
                             # if_exists='replace', 
                             # index=True)
        
        # engine.execute('''
        # ALTER TABLE {table} ADD COLUMN IF NOT EXISTS "population" int;
        # ALTER TABLE {table} ADD COLUMN IF NOT EXISTS "{population_field}" text;
        # ALTER TABLE {table} ADD COLUMN IF NOT EXISTS "{population_field} per hectare" double precision;
        # UPDATE {table} a
            # SET 
                # population = temp.population,
                # "{population_field}" = TO_CHAR(temp.population, '999,999,999'),
                # "{population_field} per hectare" = (temp.population/area_ha)::double precision
            # FROM temp 
            # WHERE a."{id}" = temp."{id}";
        # '''.format(table = areas[admin_area]['name_s'],
                   # id = areas[admin_area]['id'],
                   # population_field = population_field))
                   
    # print('Estimated population for {} study region in {}'
          # ' based on UN adjusted WorldPop data is {:,}.'.format(full_locale,population_target,pop))

    # # Calculate "Ratio of community population to district population" 
    # # as, the ratio of area level population to larger area levels
    # for area in areas:
        # # only process those areas smaller than the largest scale
        # if area < len(areas)-1:
            # other_larger_areas = [a for a in areas if a != area and a > area]
            # for other_area in other_larger_areas:
                # engine.execute('''
                # ALTER TABLE {area} ADD COLUMN IF NOT EXISTS "pop_ratio_{area}_{other_area}" double precision;
                # UPDATE {area} a
                    # SET 
                         # "pop_ratio_{area}_{other_area}" = (a.population/(b.population::float)::double precision)
                    # FROM {other_area} b
                    # WHERE a."{other_area_id}" = b."{other_area_id}";
                # '''.format(area = areas[area]['name_s'],
                           # area_id = areas[area]['id'],
                           # other_area = areas[other_area]['name_s'],
                           # other_area_id = areas[other_area]['id']))
        
    # # Prepare maps
    # conn = psycopg2.connect(database=db, user=db_user, password=db_pwd, host=db_host,port=db_port)
    # curs = conn.cursor()
    # curs.execute('''
    # SELECT 1 
    # FROM information_schema.columns 
    # WHERE table_name='districts' and column_name='pop_ratio_districts_provinces';
    # ''')
    # res = curs.fetchone()
    # if res is None:
        # print("Automated map creation for this script is currently set up for areas for which provincial population estimates have been calculated only.")
    # else:
        # map_attribution = '{} | {} | {}'.format(map_attribution,areas[area]['attribution'],population_raster['attribution'])
        
        # # checkout https://nbviewer.jupyter.org/gist/jtbaker/57a37a14b90feeab7c67a687c398142c?flush_cache=true
        # map_layers={}
        
        
        # sql = '''SELECT "Description", geom_4326 geom FROM {}'''.format(buffered_study_region)
        # map_layers['buffer'] = gpd.GeoDataFrame.from_postgis(sql, engine, geom_col='geom' )
        
        # sql = '''
        # SELECT a."{id}",
            # a."{analysis_field}",
            # a.population,
            # a."{population_field}",
            # ROUND(a."{population_field} per hectare"::numeric,2) "{population_field} per hectare",
            # ROUND(100*a."pop_ratio_districts_provinces"::numeric,2) "Percent of Bangkok population in subdistrict",
            # a.geom_4326 geom
        # FROM {area} a
        # '''.format(id =areas[1]['id'],
                # analysis_field = areas[1]['name_f'],
                # area = areas[1]['name_s'],
                # population_field=population_field)
        # map_layers[areas[1]['name_s']] = gpd.GeoDataFrame.from_postgis(sql, engine, geom_col='geom' )
        
        # sql = '''
        # SELECT a."{id}",
            # a."{analysis_field}",
            # a.population,
            # a."{population_field}",
            # ROUND(a."{population_field} per hectare"::numeric,2) "{population_field} per hectare",
            # ROUND(100*a."pop_ratio_subdistricts_districts"::numeric,2) "Percent of district population in subdistrict",
            # ROUND(100*a."pop_ratio_subdistricts_provinces"::numeric,2) "Percent of Bangkok population in subdistrict",
            # b."{other_area_name}",
            # a.geom_4326 geom
        # FROM {area} a
        # LEFT JOIN {other_area} b ON a."{other_area_id}" = b."{other_area_id}"
        # '''.format(id =areas[0]['id'],
                # analysis_field = analysis_field,
                # area = area_analysis, 
                # population_field=population_field,
                # other_area = areas[1]['name_s'],
                # other_area_name = areas[1]['name_f'],
                # other_area_id = areas[1]['id'])
        # map_layers[areas[0]['name_s']] = gpd.GeoDataFrame.from_postgis(sql, engine, geom_col='geom')
        
        # # load up the reprojected raster
        # with rasterio.open(population_raster_clipped) as src:
            # boundary = src.bounds
            # map_layers['population'] = src.read()
            # nodata = src.nodata
            
        # xy = [float(map_layers['buffer'].centroid.y),float(map_layers['buffer'].centroid.x)]  
        # bounds = map_layers['buffer'].bounds.transpose().to_dict()[0]
        # print("\nPlease inspect results using interactive maps saved in project maps folder:")
        
        # # Population raster map (includes the raster overlay)
        # m = folium.Map(location=xy, zoom_start=11,tiles=None, control_scale=True, prefer_canvas=True)
        # m.add_tile_layer(tiles='Stamen Toner',
                        # name='simple map', 
                        # active=True,
                        # attr=((
                            # " {} | "
                            # "Map tiles: <a href=\"http://stamen.com/\">Stamen Design</a>, " 
                            # "under <a href=\"http://creativecommons.org/licenses/by/3.0\">CC BY 3.0</a>, featuring " 
                            # "data by <a href=\"https://wiki.osmfoundation.org/wiki/Licence/\">OpenStreetMap</a>, "
                            # "under ODbL.").format(map_attribution))
                                # )
                                
        # # bins = list(map_layers[areas[0]['name_s']]['population'].quantile([0, 0.25, 0.5, 0.75, 1]))  
        # population_layer = folium.Choropleth(map_layers[areas[0]['name_s']],
                        # name = areas[0]['name_f'],
                        # fill_opacity=0,
                        # line_opacity=0,
                        # highlight=True,
                        # overlay = True
                        # ).add_to(m)
                                    
        # folium.features.GeoJsonTooltip(fields=[areas[0]['name_f'],
                                            # areas[1]['name_f'],
                                            # population_field,
                                            # '{} per hectare'.format(population_field),
                                            # 'Percent of district population in subdistrict',
                                            # 'Percent of Bangkok population in subdistrict',],
                                    # labels=True, 
                                    # sticky=True
                                    # ).add_to(population_layer.geojson)                          
                                    
        # m.add_child(folium.raster_layers.ImageOverlay(map_layers['population'][0], 
                                        # name='Poplulation per pixel (WorldPop predicted model: {}, UN adjusted)'.format(population_target),
                                        # opacity=.7,
                                        # bounds=[[bounds['miny'],bounds['minx']], 
                                                # [bounds['maxy'], bounds['maxx']]],
                                        # colormap=lambda x: (1, 0, x, x),#R,G,B,alpha,
                                        # legend_name='Poplulation per pixel (WorldPop predicted model: {}, UN adjusted)'.format(population_target),
                                        # overlay=True
                                        # ))                              
                                    
        # folium.LayerControl(collapsed=True).add_to(m)
        # m.fit_bounds(m.get_bounds())
        # m.get_root().html.add_child(folium.Element(map_style))
        
        # # save map
        # map_name = '{}_02_population_raster_{}'.format(locale,population_target)
        # m.save('{}/html/{}.html'.format(locale_maps,map_name))
        # folium_to_png(os.path.join(locale_maps,'html'),os.path.join(locale_maps,'png'),map_name)
        # print("\t- {}".format(map_name)) 
        
        # # Population map
        # m = folium.Map(location=xy, zoom_start=11,tiles=None, control_scale=True, prefer_canvas=True)
        # m.add_tile_layer(tiles='Stamen Toner',
                        # name='simple map', 
                        # active=True,
                        # attr=((
                            # " {} | "
                            # "Map tiles: <a href=\"http://stamen.com/\">Stamen Design</a>, " 
                            # "under <a href=\"http://creativecommons.org/licenses/by/3.0\">CC BY 3.0</a>, featuring " 
                            # "data by <a href=\"https://wiki.osmfoundation.org/wiki/Licence/\">OpenStreetMap</a>, "
                            # "under ODbL.").format(map_attribution))
                                # )
        # districts_layer = folium.Choropleth(map_layers[areas[1]['name_s']],
                        # name=areas[1]['name_f'],
                        # fill_opacity=0,
                        # line_color=colours['qualitative'][1], 
                        # highlight=True,
                        # overlay = True
                        # ).add_to(m)
        # folium.features.GeoJsonTooltip(fields=[areas[1]['name_f'],
                                            # population_field,
                                            # '{} per hectare'.format(population_field),
                                            # 'Percent of Bangkok population in subdistrict',],
                                    # labels=True, 
                                    # sticky=True
                                    # ).add_to(districts_layer.geojson)    
        # population_layer = folium.Choropleth(data=map_layers[areas[0]['name_s']],
                        # geo_data =map_layers[areas[0]['name_s']].to_json(),
                        # name = population_field,
                        # columns =[areas[0]['id'],'population'],
                        # key_on="feature.properties.{}".format(areas[0]['id']),
                        # fill_color='YlGn',
                        # fill_opacity=0.7,
                        # line_opacity=0.2,
                        # legend_name='{}, by {}'.format(population_field,areas[0]['name_f']),
                        # # bins=bins,
                        # reset=True,
                        # overlay = True
                        # ).add_to(m)
                                    
        # folium.features.GeoJsonTooltip(fields=[areas[0]['name_f'],
                                            # areas[1]['name_f'],
                                            # population_field,
                                            # '{} per hectare'.format(population_field),
                                            # 'Percent of district population in subdistrict',
                                            # 'Percent of Bangkok population in subdistrict',],
                                    # labels=True, 
                                    # sticky=True
                                    # ).add_to(population_layer.geojson)                          
                                    
        # folium.LayerControl(collapsed=True).add_to(m)
        # m.fit_bounds(m.get_bounds())
        # m.get_root().html.add_child(folium.Element(map_style))
        
        # # save map
        # map_name = '{}_02_population_{}'.format(locale,population_target)
        # m.save('{}/html/{}.html'.format(locale_maps,map_name))
        # folium_to_png(os.path.join(locale_maps,'html'),os.path.join(locale_maps,'png'),map_name)
        # print("\t- {}".format(map_name))           
        
        # # Population density map
        # m = folium.Map(location=xy, zoom_start=11,tiles=None, control_scale=True, prefer_canvas=True)
        # m.add_tile_layer(tiles='Stamen Toner',
                        # name='simple map', 
                        # active=True,
                        # attr=((
                            # " {} | "
                            # "Map tiles: <a href=\"http://stamen.com/\">Stamen Design</a>, " 
                            # "under <a href=\"http://creativecommons.org/licenses/by/3.0\">CC BY 3.0</a>, featuring " 
                            # "data by <a href=\"https://wiki.osmfoundation.org/wiki/Licence/\">OpenStreetMap</a>, "
                            # "under ODbL.").format(map_attribution))
                                # )
        # districts_layer = folium.Choropleth(map_layers[areas[1]['name_s']],
                        # name=areas[1]['name_f'],
                        # fill_opacity=0,
                        # line_color=colours['qualitative'][1], 
                        # highlight=True,
                        # overlay = True
                        # ).add_to(m)
        # folium.features.GeoJsonTooltip(fields=[areas[1]['name_f'],
                                            # population_field,
                                            # '{} per hectare'.format(population_field),
                                            # 'Percent of Bangkok population in subdistrict',],
                                    # labels=True, 
                                    # sticky=True
                                    # ).add_to(districts_layer.geojson)    
        # density_layer = folium.Choropleth(data=map_layers[areas[0]['name_s']],
                        # geo_data =map_layers[areas[0]['name_s']].to_json(),
                        # name = '{} per hectare'.format(population_field),
                        # columns =[areas[0]['id'],'{} per hectare'.format(population_field)],
                        # key_on="feature.properties.{}".format(areas[0]['id']),
                        # fill_color='YlGn',
                        # fill_opacity=0.7,
                        # line_opacity=0.2,
                        # legend_name='{} per hectare, by {}'.format(population_field,areas[0]['name_f']),
                        # # bins=bins,
                        # reset=True,
                        # overlay = True
                        # ).add_to(m)
                                    
        # folium.features.GeoJsonTooltip(fields=[areas[0]['name_f'],
                                            # areas[1]['name_f'],
                                            # population_field,
                                            # '{} per hectare'.format(population_field),
                                            # 'Percent of district population in subdistrict',
                                            # 'Percent of Bangkok population in subdistrict',],
                                    # labels=True, 
                                    # sticky=True
                                    # ).add_to(density_layer.geojson)                              
                                    
        # folium.LayerControl(collapsed=True).add_to(m)
        # m.fit_bounds(m.get_bounds())
        # m.get_root().html.add_child(folium.Element(map_style))
        
        # # save map
        # map_name = '{}_02_population_density_{}'.format(locale,population_target)
        # m.save('{}/html/{}.html'.format(locale_maps,map_name))
        # folium_to_png(os.path.join(locale_maps,'html'),os.path.join(locale_maps,'png'),map_name)
        # print("\t- {}".format(map_name))              
        
        
        # # Percent of district population in subdistrict
        # m = folium.Map(location=xy, zoom_start=11,tiles=None, control_scale=True, prefer_canvas=True)
        # m.add_tile_layer(tiles='Stamen Toner',
                        # name='simple map', 
                        # active=True,
                        # attr=((
                            # " {} | "
                            # "Map tiles: <a href=\"http://stamen.com/\">Stamen Design</a>, " 
                            # "under <a href=\"http://creativecommons.org/licenses/by/3.0\">CC BY 3.0</a>, featuring " 
                            # "data by <a href=\"https://wiki.osmfoundation.org/wiki/Licence/\">OpenStreetMap</a>, "
                            # "under ODbL.").format(map_attribution))
                                # )
        # districts_layer = folium.Choropleth(map_layers[areas[1]['name_s']],
                        # name=areas[1]['name_f'],
                        # fill_opacity=0,
                        # line_color=colours['qualitative'][1], 
                        # highlight=True,
                        # overlay = True
                        # ).add_to(m)
        # folium.features.GeoJsonTooltip(fields=[areas[1]['name_f'],
                                            # population_field,
                                            # '{} per hectare'.format(population_field),
                                            # 'Percent of Bangkok population in subdistrict',],
                                    # labels=True, 
                                    # sticky=True
                                    # ).add_to(districts_layer.geojson)      
                                    
        # population_percent_layer = folium.Choropleth(data=map_layers[areas[0]['name_s']],
                        # geo_data =map_layers[areas[0]['name_s']].to_json(),
                        # name = 'Percent of district population in subdistrict',
                        # columns =[areas[0]['id'],'Percent of district population in subdistrict'],
                        # key_on="feature.properties.{}".format(areas[0]['id']),
                        # fill_color='YlGn',
                        # fill_opacity=0.7,
                        # line_opacity=0.2,
                        # legend_name='Percent of district population in {}'.format(areas[0]['name_f']),
                        # # bins=bins,
                        # reset=True,
                        # overlay = True
                        # ).add_to(m)
                                    
        # folium.features.GeoJsonTooltip(fields=[areas[0]['name_f'],
                                            # areas[1]['name_f'],
                                            # population_field,
                                            # '{} per hectare'.format(population_field),
                                            # 'Percent of district population in subdistrict',
                                            # 'Percent of Bangkok population in subdistrict',],
                                    # labels=True, 
                                    # sticky=True
                                    # ).add_to(population_percent_layer.geojson)                              
                                    
        # folium.LayerControl(collapsed=True).add_to(m)
        # m.fit_bounds(m.get_bounds())
        # m.get_root().html.add_child(folium.Element(map_style))
        
        # # save map
        # map_name = '{}_02_percent_of_district_population_in_subdistrict_{}'.format(locale,population_target)
        # m.save('{}/html/{}.html'.format(locale_maps,map_name))
        # folium_to_png(os.path.join(locale_maps,'html'),os.path.join(locale_maps,'png'),map_name)
        # print("\t- {}".format(map_name))   
        
        
        # # Percent of Bangkok population in subdistrict
        # m = folium.Map(location=xy, zoom_start=11,tiles=None, control_scale=True, prefer_canvas=True)
        # m.add_tile_layer(tiles='Stamen Toner',
                        # name='simple map', 
                        # active=True,
                        # attr=((
                            # " {} | "
                            # "Map tiles: <a href=\"http://stamen.com/\">Stamen Design</a>, " 
                            # "under <a href=\"http://creativecommons.org/licenses/by/3.0\">CC BY 3.0</a>, featuring " 
                            # "data by <a href=\"https://wiki.osmfoundation.org/wiki/Licence/\">OpenStreetMap</a>, "
                            # "under ODbL.").format(map_attribution))
                                # )
        # districts_layer = folium.Choropleth(map_layers[areas[1]['name_s']],
                        # name=areas[1]['name_f'],
                        # fill_opacity=0,
                        # line_color=colours['qualitative'][1], 
                        # highlight=True,
                        # overlay = True
                        # ).add_to(m)
        # folium.features.GeoJsonTooltip(fields=[areas[1]['name_f'],
                                            # population_field,
                                            # '{} per hectare'.format(population_field),
                                            # 'Percent of Bangkok population in subdistrict',],
                                    # labels=True, 
                                    # sticky=True
                                    # ).add_to(districts_layer.geojson)    
        # population_percent_layer = folium.Choropleth(data=map_layers[areas[0]['name_s']],
                        # geo_data =map_layers[areas[0]['name_s']].to_json(),
                        # name = 'Percent of Bangkok population in subdistrict',
                        # columns =[areas[0]['id'],'Percent of Bangkok population in subdistrict'],
                        # key_on="feature.properties.{}".format(areas[0]['id']),
                        # fill_color='YlGn',
                        # fill_opacity=0.7,
                        # line_opacity=0.2,
                        # legend_name='Percent of Bangkok population in  {}'.format(areas[0]['name_f']),
                        # # bins=bins,
                        # reset=True,
                        # overlay = True
                        # ).add_to(m)
                                    
        # folium.features.GeoJsonTooltip(fields=[areas[0]['name_f'],
                                            # areas[1]['name_f'],
                                            # population_field,
                                            # '{} per hectare'.format(population_field),
                                            # 'Percent of district population in subdistrict',
                                            # 'Percent of Bangkok population in subdistrict',],
                                    # labels=True, 
                                    # sticky=True
                                    # ).add_to(population_percent_layer.geojson)                                                         
                                    
        # folium.LayerControl(collapsed=True).add_to(m)
        # m.fit_bounds(m.get_bounds())
        # m.get_root().html.add_child(folium.Element(map_style))
        
        # # save map
        # map_name = '{}_02_percent_of_Bangkok_population_in_subdistrict_{}'.format(locale,population_target)
        # m.save('{}/html/{}.html'.format(locale_maps,map_name))
        # folium_to_png(os.path.join(locale_maps,'html'),os.path.join(locale_maps,'png'),map_name)
        # print("\t- {}".format(map_name))   

print("Copying area population tables excerpt to geopackage..."),
command = (
            'ogr2ogr -overwrite -f GPKG {path}/{output_name}.gpkg '
            'PG:"host={host} user={user} dbname={db} password={pwd}" '
            '  {tables}'
            ).format(output_name = '{}_population_{}'.format(study_region,population_linkage[analysis_scale]['year_target']),
                     path = os.path.join(locale_maps,'gpkg'),
                     host = db_host,
                     user = db_user,
                     pwd = db_pwd,
                     db = db,
                     tables =  ' '.join(['"{}"'.format(a) for a in areas])) 
print(" Done.")
sp.call(command, shell=True)     

# # output to completion log					
script_running_log(script, task, start, locale)
engine.dispose()
