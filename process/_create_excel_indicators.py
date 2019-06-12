# Script:  _create_excel_indicators.py
# Purpose: Create indicators based on Excel data where accompanied by a 'map_this_dir_config.xlsx' file with appropriate entries
# Author:  Carl Higgs
# Date:    20190610

import time
import os
import pandas as pd
import numpy as np
import geopandas as gpd
from geoalchemy2 import Geometry, WKTElement
from sqlalchemy import create_engine
import folium

from script_running_log import script_running_log

# Import custom variables for National Liveability indicator process
from _project_setup import *

# simple timer for log file
start = time.time()
script = os.path.basename(sys.argv[0])
task = 'create study region boundary'

engine = create_engine("postgresql://{user}:{pwd}@{host}/{db}".format(user = db_user,
                                                                      pwd  = db_pwd,
                                                                      host = db_host,
                                                                      db   = db))

# Prepare folders
if not os.path.exists(locale_maps):
    os.makedirs(locale_maps)    
for dir in ['html','png','pdf','gpkg']:
    path = os.path.join(locale_maps,dir)
    if not os.path.exists(path):
        os.makedirs(path)   

# Iterate over data directory
print("Check folders in data directory for 'map_this_dir_config.xlsx' files... "),
for root, dirs, files in os.walk('../data'):
    for file in files:
        # retrieve configuration details for Excel files in folder, if config file encountered
        if file == 'map_this_dir_config.xlsx':
            config = os.path.join(root,file)
            print('Directory: {}'.format(root))
            xls = pd.ExcelFile(config)
            df = pd.read_excel(xls, 'map_config')
            # iterate over files specificed in config file within this folder
            for row in df.index.values:
                dataset = df.loc[row,'File']
                print('  - "{}"'.format(dataset))
                sheet = df.loc[row,'Sheet']
                description = df.loc[row,'Description']
                heading = df.loc[row,'Heading']
                map_name_suffix = df.loc[row,'map_name_suffix'].replace(' ','_',).replace('-','_')
                area_layer = df.loc[row,'Area layer']
                area_linkage_id = df.loc[row,'Area linkage ID']
                area_index =  [k for k in areas.keys() if areas[k]['name_s']==area_layer][0]
                aggregation = df.loc[row,'Aggregation if duplicates']
                linkage_id = df.loc[row,'Linkage ID']
                display_id = df.loc[row,'Display ID']
                map_field = df.loc[row,'Map field']
                if np.isnan(description):
                    description = map_field
                source = df.loc[row,'Source']
                mapxls = pd.ExcelFile(os.path.join(root,dataset))
                mdf = pd.read_excel(mapxls,sheet)
                mdf = mdf.set_index(linkage_id)
                mdf.index.name = area_linkage_id
                # aggregate data by ID using specified method, if specified.
                # Note that currently only 'sum' and 'average' have been programmed as options.
                aggregation_text = ''
                if aggregation =='sum':
                    mdf = mdf.groupby(mdf.index)[map_field].sum().to_frame()
                    aggregation_text = " ({})".format(aggregation)
                elif aggregation == 'average':
                    mdf = mdf.groupby(mdf.index)[map_field].mean().to_frame()
                    aggregation_text = " ({})".format(aggregation)
                elif not '{}'.format(description)=='nan':
                    print("Specified aggregation method has not been programmed as an option for this Excel file; no aggregation will be made if duplicate IDs are encountered.  If duplicate IDs exists, results are likely inaccurate,")
                # we create an alternate description field as it may be that the map_field variable is > 63 characters 
                # in which case it would be truncated.  So we use the map_name_suffix as the field name for the data, and populate 'description'
                # with the 
                mdf['description'] = map_field
                # Send to SQL database
                mdf.columns = [map_name_suffix,'description']
                mdf.to_sql(map_name_suffix, engine, if_exists='replace', index=True)
                # Create map
                attribution = '{} | {} | {}'.format(map_attribution,areas[area_index]['attribution'],source)
                tables    = [buffered_study_region,study_region]
                fields    = ['Description','Description']
                sql = '''
                SELECT "{id}",
                    a."{data}",
                    a.description,
                    b.geom_4326 geom
                FROM {data} a 
                LEFT JOIN {area} b USING ("{id}")
                '''.format(id =area_linkage_id,
                        data = map_name_suffix, 
                        area = area_layer)
                map = gpd.GeoDataFrame.from_postgis(sql, engine, geom_col='geom')
                
                # get map centroid from study region
                xy = [float(map.centroid.y.mean()),float(map.centroid.x.mean())]    
                # initialise map
                m = folium.Map(location=xy, zoom_start=10, tiles=None,control_scale=True, prefer_canvas=True)
                m.add_tile_layer(tiles='Stamen Toner',
                                name='simple map', 
                                active=True,
                                attr=((
                                    " {} | "
                                    "Map tiles: <a href=\"http://stamen.com/\">Stamen Design</a>, " 
                                    "under <a href=\"http://creativecommons.org/licenses/by/3.0\">CC BY 3.0</a>, featuring " 
                                    "data by <a href=\"https://wiki.osmfoundation.org/wiki/Licence/\">OpenStreetMap</a>, "
                                    "under ODbL.").format(attribution))
                                        )
                # Create choropleth map
                layer = folium.Choropleth(data=map,
                                geo_data =map.to_json(),
                                name = map_field,
                                columns =[area_linkage_id,map_name_suffix],
                                key_on="feature.properties.{}".format(area_linkage_id),
                                fill_color='YlGn',
                                fill_opacity=0.7,
                                line_opacity=0.2,
                                legend_name='{}, by {}{}'.format(map_field,area_layer,aggregation_text),
                                # bins=bins,
                                reset=True,
                                overlay = True
                                ).add_to(m)
                folium.features.GeoJsonTooltip(fields=[area_linkage_id,'description',map_name_suffix],
                                            labels=True, 
                                            sticky=True
                                            ).add_to(layer.geojson)    
                # Add layer control
                folium.LayerControl(collapsed=False).add_to(m)
                m.fit_bounds(m.get_bounds())
                m.get_root().html.add_child(folium.Element(map_style))
                # Modify map heading (above legend)
                html = m.get_root().render()
                old = 'color_map_66a6a7f06f83420991f9e8431b3eae0d.svg = d3.select(".legend.leaflet-control").append("svg")'
                new = '''
                color_map_66a6a7f06f83420991f9e8431b3eae0d.title = d3.select(".legend.leaflet-control").append("div")
                        .attr("style",'vertical-align: text-top;font-weight: bold;')
                        .text("{}");
                color_map_66a6a7f06f83420991f9e8431b3eae0d.svg = d3.select(".legend.leaflet-control").append("svg")
                '''.format(heading)
                html = html.replace(old,new)
                # save map
                map_name = '{}_{}'.format(locale,map_name_suffix)
                fid = open('{}/html/{}.html'.format(locale_maps,map_name), 'wb')
                fid.write(html.encode('utf8'))
                fid.close()
                folium_to_png(os.path.join(locale_maps,'html'),os.path.join(locale_maps,'png'),map_name)
                print('\t- {}/html/{}.html'.format(locale_maps,map_name))
                print('\t- {}/png/{}.png'.format(locale_maps,map_name))
                print('')
# output to completion log					
script_running_log(script, task, start, locale)
engine.dispose()
