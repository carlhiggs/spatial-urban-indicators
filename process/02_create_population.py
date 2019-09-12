"""

Population mapping
~~~~~~~~~~~~~~~~~~

::

    Script:  02_create_population.py
    Purpose: 1) Import population raster and calculate values for polygons; 
             2) Map population
    Authors: Carl Higgs
    Note:    The raster population method of this script has been commented 
             out for Bangkok purposes, due to preference for agreed upon area 
             level statistics for population.  As such, this script functions 
             to map the population data and statistics processed in the study 
             region creation script.

"""

# 

from script_running_log import script_running_log
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
# Import custom variables for National Liveability indicator process
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
        # compile map attribution text
        attribution = '{} | {} | {}'.format(map_attribution,areas[area]['attribution'],population_linkage[analysis_scale]['attribution'])
        # get study region map data for setting up map location
        map_data={}
        sql = '''SELECT ST_Transform(ST_Buffer(geom,3),4326) geom FROM {}'''.format(study_region)
        map_data['map_buffer'] = gpd.GeoDataFrame.from_postgis(sql, engine, geom_col='geom' )
        # get analytical layer data
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
        # set up initial map location and bounds
        xy = [float(map_data['map_buffer'].centroid.y),float(map_data['map_buffer'].centroid.x)]  
        bounds = map_data['map_buffer'].bounds.transpose().to_dict()[0]
        # Population map
        for field in map_fields:
            for area in areas:
              # this kind of map does not make sense for an overall summary
              if len(map_data[area].index.values) > 1:
                map_name = '{}_02_population_{}_{}'.format(locale,area,field.replace('km\u00B2','sqkm').replace(' ','_'))
                print("{}...".format(map_name))           
                # initialise map
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
                map_layers[area] = folium.Choropleth(data = map_data[area],
                                                     geo_data =map_data[area].to_json(),
                                                     name = '{} ({})'.format(field,area),
                                                     columns =[area,field],
                                                     key_on="feature.properties.{}".format(area),
                                                     fill_color='YlGn',
                                                     fill_opacity=0.7,
                                                     nan_fill_opacity=0.2,
                                                     line_opacity=0.2,
                                                     legend_name='{}, by {}'.format(field,area),
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
                # move legend to lower right corner
                html = html.replace('''legend = L.control({position: \'topright''','''legend = L.control({position: \'bottomright''')
                # save map
                fid = open('{}/html/{}.html'.format(locale_maps,map_name), 'wb')
                fid.write(html.encode('utf8'))
                fid.close()
                # output map to image (eg png)
                folium_to_image(input_dir  = os.path.join(locale_maps,'html'),
                                output_dir = os.path.join(locale_maps,'png'),
                                map_name = map_name)
            print("\n")
    
    print("Copying area population tables excerpt to geopackage..."),
    command = (
                'ogr2ogr -overwrite -f GPKG {path}/{output_name}.gpkg '
                'PG:"host={host} user={user} dbname={db} password={pwd}" '
                '  {tables}'
                ).format(output_name = '{}'.format(study_region),
                         path = os.path.join(locale_maps,'gpkg'),
                         host = db_host,
                         user = db_user,
                         pwd = db_pwd,
                         db = db,
                         tables =  ' '.join(['"{}"'.format(a) for a in areas])) 
    print(" Done.")
    sp.call(command, shell=True)     
    
    print("Copying area population tables excerpt to geojson..."),
    for area in areas:
        command = (
                    'ogr2ogr -overwrite -f "GeoJSON" {path}/{output_name}.geojson '
                    'PG:"host={host} user={user} dbname={db} password={pwd}" '
                    '  "{tables}(geom)" '
                    ).format(output_name = '{}_{}'.format(study_region,area),
                             path = os.path.join(locale_maps,'geojson'),
                             host = db_host,
                             user = db_user,
                             pwd = db_pwd,
                             db = db,
                             tables = area)
        sp.call(command, shell=True)     
    print(" Done.")
    
    # # output to completion log					
    script_running_log(script, task, start, locale)
    engine.dispose()
    
if __name__ == '__main__':
    main()