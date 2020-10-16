"""

Population mapping
~~~~~~~~~~~~~~~~~~

Script:  
    02_create_population.py
Purpose: 
    1) Import population raster and calculate values for polygons; 
    2) Map population
Authors: 
    Carl Higgs 

"""

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

# Import custom variables for liveability indicator process
from _project_setup import *

def main():
    # simple timer for log file
    start  = time.time()
    script = os.path.basename(sys.argv[0])
    task = 'Import population raster and associate with administrative areas'
    
    engine = create_engine("postgresql://{user}:{pwd}@{host}/{db}".format(user = db_user,
                                                                          pwd  = db_pwd,
                                                                          host = db_host,
                                                                          db   = db))  
    
    if population_linkage != {}:
        # define heading for map
        heading = "{}: Population statistics, {}".format(full_locale,population_linkage[analysis_scale]['year_target'])
        # get key fields from the specified population dataset
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
        # format to display superscript 2 for square kilometres
        for f in pop_data_fields_full:
            column_names[f] = f.replace('sqkm','km\u00B2')
        
        data_fields = '"{}",'.format('","'.join(pop_data_fields_full)).replace('"",','')
        # get study region map data for setting up map location
        map_data={}
        sql = '''SELECT ST_Transform(ST_Buffer(geom,3),4326) geom FROM {}'''.format(study_region)
        map_data['map_buffer'] = gpd.GeoDataFrame.from_postgis(sql, engine, geom_col='geom' )
        # get analytical layer data
        for area in areas:
            linkage_id = areas[area]['id']
            sql = f'''
            SELECT {linkage_id},
                   {area},
                   {data_fields}
                   ST_Transform(geom, 4326) AS geom 
            FROM {area} a
            '''
            map_data[area] = gpd.GeoDataFrame.from_postgis(sql, engine, geom_col='geom')
            map_data[area].rename(columns = column_names, inplace=True)
            map_data[area].rename(columns = {'area_km\u00B2':'area (km\u00B2)'}, inplace=True)
        data_fields =[f.replace('sqkm','km\u00B2').replace('area_km\u00B2','area (km\u00B2)') for f in pop_data_fields_full]
        map_fields =[f.replace('sqkm','km\u00B2').replace('area_km\u00B2','area (km\u00B2)') for f in pop_data_fields_to_map]
        # set up initial map location and bounds
        xy = [float(map_data['map_buffer'].centroid.y),float(map_data['map_buffer'].centroid.x)]  
        bounds = map_data['map_buffer'].bounds.transpose().to_dict()[0]
        # Population map
        for field in map_fields:
            for area in areas:
              # this kind of map does not make sense for an overall summary
              if len(map_data[area].index.values) > 1:
                linkage_id = areas[area]['id']
                map_name = '{}_02_population_{}_{}'.format(locale,area,field.replace('km\u00B2','sqkm').replace(' ','_'))
                print("{}...".format(map_name))           
                # initialise map
                # compile map attribution text
                attribution = '{} | {} | {}'.format(map_attribution,areas[area]['attribution'],population_linkage[analysis_scale]['attribution'])
                m = folium.Map(location=xy, zoom_start=11, tiles=None,control_scale=True, prefer_canvas=True,attr='{}'.format(attribution))
                # Add in location names
                folium.TileLayer(tiles='http://tile.stamen.com/toner-labels/{z}/{x}/{y}.png',
                                name='Location labels', 
                                show =False,
                                overlay=True,
                                attr=((
                                    " {} | "
                                    "Map tiles: <a href=\"http://stamen.com/\">Stamen Design</a>, " 
                                    "under <a href=\"http://creativecommons.org/licenses/by/3.0\">CC BY 3.0</a>, featuring " 
                                    "data by <a href=\"https://wiki.osmfoundation.org/wiki/Licence/\">OpenStreetMap</a>, "
                                    "under ODbL.").format(attribution))
                                        ).add_to(m)
                # Add in the actual basemap to be shown
                folium.TileLayer(tiles='http://tile.stamen.com/toner-background/{z}/{x}/{y}.png',
                                name='Basemap: Simple', 
                                show =True,
                                overlay=False,
                                attr=((
                                    " {} | "
                                    "Map tiles: <a href=\"http://stamen.com/\">Stamen Design</a>, " 
                                    "under <a href=\"http://creativecommons.org/licenses/by/3.0\">CC BY 3.0</a>, featuring " 
                                    "data by <a href=\"https://wiki.osmfoundation.org/wiki/Licence/\">OpenStreetMap</a>, "
                                    "under ODbL.").format(attribution))
                                        ).add_to(m)
                # Add in alternate basemap
                folium.TileLayer(tiles='OpenStreetMap',
                                name='Basemap: OpenStreetMap', 
                                show =False,
                                overlay=False,
                                attr=((
                                    " {} | "
                                    "Map tiles: <a href=\"http://openstreetmap.org/\">© OpenStreetMap contributors</a>, " 
                                    "under <a href=\"http://creativecommons.org/licenses/by/3.0\">CC BY 3.0</a>, featuring " 
                                    "data by <a href=\"https://wiki.osmfoundation.org/wiki/Licence/\">OpenStreetMap</a>, "
                                    "under ODbL.").format(attribution))
                                        ).add_to(m)
                # We add empty tile set in order to force display of data attribution; Basemaps are not overlay layers, so they are easily switchable
                folium.TileLayer(tiles='Null tiles',
                                name='Basemap: off', 
                                show =False,
                                overlay=False,
                                attr=((
                                    " {}"
                                   ).format(attribution))
                                        ).add_to(m)
                # Create choropleth map layer
                map_layers={}     
                legend_name = f'{field}, by {area}'
                map_layers[area] = folium.Choropleth(data = map_data[area],
                                                     geo_data =map_data[area].to_json(),
                                                     name = '{} ({})'.format(field,area),
                                                     columns =[linkage_id,field],
                                                     key_on="feature.properties.{}".format(linkage_id),
                                                     fill_color='YlGn',
                                                     fill_opacity=0.7,
                                                     nan_fill_opacity=0.2,
                                                     line_opacity=0.2,
                                                     legend_name=legend_name,
                                                     reset=True,
                                                     overlay = True
                                   ).add_to(m)
                # define tooltip on hover content, formatting and behaviour
                folium.features.GeoJsonTooltip(fields=[area]+data_fields,
                                               localize=True,
                                               labels=True, 
                                               sticky=True
                                               ).add_to(map_layers[area].geojson)    
                # Add layer control
                folium.LayerControl(collapsed=False).add_to(m)
                m.fit_bounds(m.get_bounds())
                m.get_root().html.add_child(folium.Element(map_style))
                html = m.get_root().render()
                ## Wrap legend text if too long 
                ## (65 chars seems to work well, conservatively)
                if len(legend_name) > 65:
                    import textwrap
                    legend_lines = textwrap.wrap(legend_name, 65)
                    legend_length = len(legend_name)
                    n_lines = len(legend_lines)
                    legend_height = 25 + 15 * n_lines
                    old = f'''.attr("class", "caption")
        .attr("y", 21)
        .text("{legend_name}");'''
                    new = ".append('tspan')".join(['''.attr('class','caption')
        .attr("x", 0)
        .attr("y", {pos})
        .text("{x}")'''.format(x=x,pos=21+15*legend_lines.index(x)) for x in legend_lines])
                    html = html.replace(old,new)
                    html = html.replace('.attr("height", 40);',f'.attr("height", {legend_height});')
                # move legend to lower right corner
                html = html.replace('''legend = L.control({position: \'topright''','''legend = L.control({position: \'bottomright''')
                # save map
                fid = open('{}/html/{}.html'.format(output_dir,map_name), 'wb')
                fid.write(html.encode('utf8'))
                fid.close()
                # output map to image (eg png)
                folium_to_image(input_dir  = os.path.join(output_dir,'html'),
                                output_dir = os.path.join(output_dir,'png'),
                                map_name = map_name)
            print("\n")
    
    print("Copying area population tables excerpt to geopackage..."),
    command = (
                'ogr2ogr -overwrite -f GPKG {path}/{output_name}.gpkg '
                'PG:"host={host} user={user} dbname={db} password={pwd}" '
                '  {tables}'
                ).format(output_name = '{}'.format(study_region),
                         path = os.path.join(output_dir,'gpkg'),
                         host = db_host,
                         user = db_user,
                         pwd = db_pwd,
                         db = db,
                         tables =  ' '.join(['"{}"'.format(a) for a in areas])) 
    print(" Done.")
    sp.call(command, shell=True)     
    
    print("Copying area population tables excerpt to geojson (matching IISD template specification)..."),
    for area in areas:
        geojson = f'{output_dir}/geojson/{study_region}_{area}.geojson'
        if os.path.exists(geojson):
            os.remove(geojson)
        command = (
                   f'''ogr2ogr -overwrite -f "GeoJSON" {geojson} '''
                   f'''PG:"host={db_host} user={db_user} dbname={db} password={db_pwd}" '''
                   f''' -sql 'SELECT {area}_id, {area}_en, {area}_th AS "name_th_TH", ST_Transform(geom,4326) geom FROM {area}' ''' 
                   f''' -nln "{area}(geom)" '''
                   )
        sp.call(command, shell=True)     
    print(" Done.")
    
    # # output to completion log					
    script_running_log(script, task, start, locale)
    engine.dispose()
    
if __name__ == '__main__':
    main()