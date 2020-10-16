"""

Create linkage indicators
~~~~~~~~~~~~~~~~~~~~~~~~~

Script:  
    _create_linkage_indicators.py
Purpose: 
    Create indicators based on linkage with boundary data from specification in datasets section of configuration file

"""

import time
import os
import pandas as pd
import numpy as np
import geopandas as gpd
from geoalchemy2 import Geometry, WKTElement
from sqlalchemy import create_engine, NVARCHAR, event
import folium
import re
import sqlite3
import io

from script_running_log import script_running_log

# Import custom variables for liveability indicator process
from _project_setup import *

def set_columns_width(map_field,aggregation):
    """
    Define units value, based on whether rate and scaling values

    Parameters
    ----------
    units: string
        the generic defined units for this measure
    rate_units: string
        if this is a rate, the units of this rate
    rate_scale: string
        if this is a rate, the scale of the rate; if equal to 1, it is ignored.

    Returns
    -------
    units string
    """
    
    if aggregation not in ['','nan']:
        potential_column_width = len(map_field) 
    else:
        potential_column_width = len(map_field) + len(aggregation) + 1
    if potential_column_width < pd.get_option("display.max_colwidth"):
        pd.set_option("display.max_colwidth", potential_column_width)

def format_units(units,rate_units,rate_scale):
    """
    Return formatted units value, based on whether rate and scaling values

    Parameters
    ----------
    units: string
        the generic defined units for this measure
    rate_units: string
        if this is a rate, the units of this rate
    rate_scale: string
        if this is a rate, the scale of the rate; if equal to 1, it is ignored.

    Returns
    -------
    units string
    """
    if rate_units!='':
        if rate_scale == 1:
            units = f'per {rate_units}'
        else:
            units = f'per {rate_scale} {rate_units}'
    return(units)

def main():
    # simple timer for log file
    start = time.time()
    script = os.path.basename(sys.argv[0])
    task = 'Create indicators from linkage files'
    
    engine = create_engine(f"postgresql://{db_user}:{db_pwd}@{db_host}/{db}")
    gpkg_path = os.path.join(output_dir,'gpkg')
    engine_sqlite = create_engine(f'sqlite:///{gpkg_path}/{study_region}.gpkg',module = sqlite3)
                      
    if 'reprocess' in sys.argv:
        reprocess = True
    else:
        reprocess = False
                      
    # retrieve subset of datasets which are files to be joined based on linkage
    df = df_datasets.query(f"type=='linkage'").copy()
    # get key fields from the specified population dataset
    population = pandas.read_csv(population_linkage[analysis_scale]['data'],index_col=population_linkage[analysis_scale]['linkage']) 
    population_numeric = [c for c in population.columns if np.issubdtype(population[c].dtype, np.number)]
    pop_data_fields = population_map_fields.split(',')
    pop_data_fields_full = ['area_sqkm']
    pop_data_fields_to_map = []
    for f in pop_data_fields:
        pop_data_fields_full.append(f)
        if f in population_numeric:
            pop_data_fields_full.append(f'{f} per sqkm')
            pop_data_fields_to_map.append(f'{f} per sqkm')
    
    pop_data_fields_full = [x for x in pop_data_fields_full if x!= ""]
    pop_data_fields_to_map = [x for x in pop_data_fields_to_map if x!= ""]
    
    column_names = {}
    # format to display superscript 2 for square kilometres
    for f in pop_data_fields_full:
        column_names[f] = f.replace('sqkm','km\u00B2')
    
    for row in df.index:
        dataset = df.loc[row,'data_file']
        print('  - "{}"'.format(dataset))
        # get information about this measure
        sheet = df.loc[row,'excel_sheet']
        data_type = valid_type(df.loc[row,'data_type'])
        description = df.loc[row,'indicator_measure']
        map_name_suffix = df.loc[row,'table_out_name'].replace(' ','_',).replace('-','_')
        area_layer = df.loc[row,'linkage_layer']
        area_linkage_id = df.loc[row,'linkage_id']
        aggregation = df.loc[row,'aggregation']
        linkage_id = df.loc[row,'linkage_id']
        point_overlay_xy = df.loc[row,'point_overlay_xy']
        display_id = area_layer
        map_field = df.loc[row,'map_field']
        units = df.loc[row,'units']
        evaluate = df.loc[row,'evaluate']
        rate = df.loc[row,'rate']
        rate_units = df.loc[row,'rate_units']
        rate_scale = df.loc[row,'rate_scale']
        units = format_units(units,rate_units,rate_scale)
        target_year = df.loc[row,'year_target']
        set_columns_width(map_field,aggregation)  # adjust settings for display of field names 
        map_name = f'{locale}_ind_{map_name_suffix}'
        source = df.loc[row,'provider']
        publication_year = df.loc[row,'year_published']
        print('\t{}'.format(map_name))
        if os.path.isfile(f'{output_dir}/html/{map_name}.html') and reprocess==False:
            print('\t - File appears to already have been processed (HTML output exists); skipping.')
        else:
            if 'skip_tables' not in sys.argv:
                if not area_layer in areas:
                   print("\t - Please check that the specified 'linkage_layer' corresponds to one of those set up in the Parameters sheet.")
                   continue
                if not areas[area_layer]['id']==linkage_id:
                   print("\t - Please check that the specified 'linkage_id' corresponds to that of the specified linkage layer.")
                   continue
                if description=='':
                    description = map_field
                    df.loc[row,'Description'] = map_field
                
                if 'xlsx:' in dataset:
                    try:
                        # recording 1-indexed Excel header row to 0-index for ingestion with Pandas
                        header_row = int(dataset.split('.xlsx:')[1])-1
                        dataset = dataset.split(".xlsx:")[0] + '.xlsx'
                        mapxls = pd.ExcelFile(f'../{dataset}')
                        mdf = pd.read_excel(mapxls,sheet,header=header_row)
                        mdf = mdf.set_index(linkage_id)
                    except:
                        sys.exit(f"Ingestion of supplied Excel dataset for linkage indicator failed; please check details (e.g. of header row) were correctly supplied.  Error report: { sys.exc_info()}")
                else:
                    mapxls = pd.ExcelFile(f'../{dataset}')
                    mdf = pd.read_excel(mapxls,sheet)
                    mdf = mdf.set_index(linkage_id)
                
                mdf.index.name = area_linkage_id
                fill_na = '{}'.format(df.loc[row,'fill_na'])
                if fill_na not in ['','nan']:
                    fill_na = fill_na.split(',')
                    for field in fill_na:
                        mdf[field] = mdf[field].fillna(method = 'ffill') 
                if '{}'.format(point_overlay_xy) not in ['','nan']:
                    # this means an attempt has been made to define point data locations
                    point_overlay_xy = point_overlay_xy.split(',')
                    point_overlay_name = df.loc[row,'point_overlay_name']
                    point_overlay_hover_field = df.loc[row,'point_overlay_hover_field']
                    point_overlay = gpd.GeoDataFrame(mdf, geometry=gpd.points_from_xy(mdf[point_overlay_xy[0]],mdf[point_overlay_xy[1]]))
                # aggregate data by ID using specified method, if specified.
                aggregation_text = ''
                if aggregation =='count':
                    mdf = mdf.groupby(mdf.index)[map_field].count().to_frame()
                    aggregation_text = f" ({aggregation})"
                if aggregation =='sum':
                    mdf = mdf.groupby(mdf.index)[map_field].sum().to_frame()
                    aggregation_text = f" ({aggregation})"
                elif aggregation == 'average':
                    mdf = mdf.groupby(mdf.index)[map_field].mean().to_frame()
                    aggregation_text = f" ({aggregation})"
                    map_field = f'average {map_field}'
                elif aggregation == 'percent':
                    mdf = mdf.eval(f'`{map_field}`{evaluate}').groupby(mdf.index).mean().to_frame()*100
                    aggregation_text = f" (%)"
                    map_field = f'percent {map_field} {evaluate}'
                elif not '{}'.format(description)=='nan':
                    print("\t\tNo aggregation method specified; assuming that all records map to distinct areas.")
                    mdf = mdf[[map_field]]
                if rate != '':
                    if rate in ['area','population','household']:
                        density_field = df.loc[row,'indicator_measure']
                        rate_variable =  globals()['rate_{}'.format(rate)]
                        sql = f'''
                                SELECT a.{area_linkage_id},
                                       {rate_variable}
                                FROM {area_layer} a
                                '''
                        area_data = pandas.read_sql(sql, engine, index_col=f'{area_linkage_id}')
                        mdf = mdf.join(area_data)
                        mdf[density_field] = mdf[map_field]/(mdf[rate_variable]/rate_scale)
                        mdf.drop([rate_variable,map_field], axis=1, inplace=True)
                        map_field = density_field
                    else:
                        print(f'undefined density "{density}"; please check configuration for this indicator')
                # we create an alternate description field as it may be that the map_field variable is > 63 characters 
                # in which case it would be truncated.  So we use the map_name_suffix as the field name for the data, and populate 'description'
                # with the 
                # mdf['description'] = map_field
                # Send to SQL database
                # print(mdf.columns)
                # mdf.columns = [map_name_suffix]
                if len(mdf.columns) == 1:
                    mdf.columns = [map_name_suffix]
                else:
                    # print([map_name_suffix]+mdf.columns[1:])
                    mdf.columns = [map_name_suffix]+mdf.columns[1:]
                mdf.to_sql(map_name_suffix, engine, if_exists='replace', index=True)
                print(f'\t- postgresql::{db}/{map_name_suffix}')
                mdf.to_sql(map_name_suffix, engine_sqlite, if_exists='replace',index=True)
                print('\t- {path}/{output_name}.gpkg/{layer}'.format(output_name = '{}'.format(study_region),
                                                                path = os.path.join(output_dir,'gpkg'),
                                                                layer = map_name_suffix))
                sql = f'''
                        SELECT a.{area_linkage_id} AS "Census Id",
                               district_en AS "Boundary Name",
                               {target_year} AS Year,
                               {map_name_suffix} AS "Value",
                               NULL AS "Trend"
                        FROM {area_layer} a
                        LEFT JOIN {map_name_suffix} USING ({area_linkage_id})
                        '''
                csv_data = pandas.read_sql(sql, engine, index_col='Census Id')
                s = io.StringIO()
                csv_data.to_csv(s,header=False)
                body = s.getvalue()
                # header = "'Boundary Name','year','Value','Trend'\n"
                sep = '-'*142
                csv_template = (
                     'template_version,1.2,Ignore this row,,\n'
                    f'data_type,{units},0,Set data type as # % or a custom suffix,\r\n'
                     'trend_year_start,,Set the year range for the start of trend calculation,,\r\n'
                     'trend_year_end,,Set the year range for the end of trend calculation,,\r\n'
                    f'{sep},,,,\r\n'
                     'Census Id,Boundary Name,Year,Value,Trend\r\n'
                    f'{sep},,,,\r\n'
                    f'{body}'
                    )
                csv_file = '{path}/{output_name}.csv'.format(output_name = '{}_{}'.format(study_region,
                                                                                          map_name_suffix),
                                                             path = os.path.join(output_dir,'csv'))
                with open(csv_file, 'w') as output_file:
                    output_file.write(csv_template)
                print('\t- {path}/{output_name}.csv'.format(output_name = '{}_{}'.format(study_region,
                                                                                          map_name_suffix),
                                                             path = os.path.join(output_dir,'csv')))
                # df.loc[row,:].to_frame().transpose().to_sql('data_sources', engine, if_exists='replace',index=False)
            
            # Create map
            if 'skip_maps' not in sys.argv:
                area_attribution = areas[area_layer]['attribution']
                data_attribution = f'{source} ({publication_year})'
                attribution = f'{map_attribution} | {area_attribution} | data: {data_attribution}'
                tables    = [buffered_study_region,study_region]
                fields    = ['Description','Description']
                coalesce_na = '{}'.format(df.loc[row,'coalesce_na'])
                if coalesce_na in ['','nan']:
                    sql = '''
                        SELECT a.{id},
                               a.{area},
                               {data_fields}
                               b.{data},
                               ST_Transform(a.geom, 4326) AS geom 
                        FROM {area} a
                        LEFT JOIN {data} b 
                        USING ({id})
                        '''.format(area = area_layer,
                                   data_fields = 'a."{}",'.format('","'.join(pop_data_fields_full)),
                                   data = map_name_suffix,
                                   map_field = map_field,
                                   id = linkage_id)
                else:
                    sql = '''
                        SELECT a.{id},
                               a.{area},
                               {data_fields}
                               COALESCE(b.{data},{coalesce_na}) AS "{data}",
                               ST_Transform(a.geom, 4326) AS geom 
                        FROM {area} a
                        LEFT JOIN {data} b 
                        USING ({id})
                        '''.format(area = area_layer,
                                   data_fields = 'a."{}",'.format('","'.join(pop_data_fields_full)),
                                   data = map_name_suffix,
                                   map_field = map_field,
                                   id = linkage_id,
                                   coalesce_na = coalesce_na)
                map = gpd.GeoDataFrame.from_postgis(sql, engine, geom_col='geom')
                map.rename(columns = {map_name_suffix : map_field}, inplace=True)
                map.rename(columns = column_names, inplace=True)
                map.rename(columns = {'area_km\u00B2':'area (km\u00B2)'}, inplace=True)
                data_fields =[area_layer]+[f.replace('sqkm','km\u00B2').replace('area_km\u00B2','area (km\u00B2)') for f in pop_data_fields_full]+[map_field]    
                # get map centroid from study region
                xy = [float(map.centroid.y.mean()),float(map.centroid.x.mean())]    
                # initialise map
                m = folium.Map(location=xy, zoom_start=11, tiles=None,control_scale=True, prefer_canvas=True,attr=attribution)
                # Add in location names
                folium.TileLayer(tiles='http://tile.stamen.com/toner-labels/{z}/{x}/{y}.png',
                                name='Location labels', 
                                show =False,
                                overlay=True,
                                attr=(
                                   f" {attribution} | "
                                    "Map tiles: <a href=\"http://stamen.com/\">Stamen Design</a>, " 
                                    "under <a href=\"http://creativecommons.org/licenses/by/3.0\">CC BY 3.0</a>, featuring " 
                                    "data by <a href=\"https://wiki.osmfoundation.org/wiki/Licence/\">OpenStreetMap</a>, "
                                    "under ODbL.")
                                ).add_to(m)
                # Add in the actual basemap to be shown
                folium.TileLayer(tiles='http://tile.stamen.com/toner-background/{z}/{x}/{y}.png',
                                name='Basemap: Simple', 
                                show =True,
                                overlay=False,
                                attr=(
                                   f" {attribution} | "
                                    "Map tiles: <a href=\"http://stamen.com/\">Stamen Design</a>, " 
                                    "under <a href=\"http://creativecommons.org/licenses/by/3.0\">CC BY 3.0</a>, featuring " 
                                    "data by <a href=\"https://wiki.osmfoundation.org/wiki/Licence/\">OpenStreetMap</a>, "
                                    "under ODbL.")
                                ).add_to(m)
                # Add in alternate basemap
                folium.TileLayer(tiles='OpenStreetMap',
                                name='Basemap: OpenStreetMap', 
                                show =False,
                                overlay=False,
                                attr=(
                                    " {attribution} | "
                                    "Map tiles: <a href=\"http://openstreetmap.org/\">© OpenStreetMap contributors</a>, " 
                                    "under <a href=\"http://creativecommons.org/licenses/by/3.0\">CC BY 3.0</a>, featuring " 
                                    "data by <a href=\"https://wiki.osmfoundation.org/wiki/Licence/\">OpenStreetMap</a>, "
                                    "under ODbL.")
                                ).add_to(m)
                # Add in satellite basemap
                folium.TileLayer(tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}' ,
                                name='Basemap: ESRI World Imagery (satellite)', 
                                show =False,
                                overlay=False,
                                attr=((
                                    " {} | "
                                    "Map tiles: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community', " 
                                    "under <a href=\"http://creativecommons.org/licenses/by/3.0\">CC BY 3.0</a>, featuring " 
                                    "data by <a href=\"https://wiki.osmfoundation.org/wiki/Licence/\">OpenStreetMap</a>, "
                                    "under ODbL.").format(map_attribution))
                                        ).add_to(m)
                # We add empty tile set in order to force display of data attribution; Basemaps are not overlay layers, so they are easily switchable
                folium.TileLayer(tiles='Null tiles',
                                name='Basemap: off', 
                                show =False,
                                overlay=False,
                                attr=f" {attribution}"
                                ).add_to(m)
                # Create choropleth map
                bins = 6
                # determine how to bin data (depending on skew, linear scale with 6 equal distance groups may not be appropriate)
                # legend_bins = '{}'.format(df.loc[row,'legend_bins'])
                # if legend_bins in ['quartiles']:
                #     bins = list(map[map_field].quantile([0, 0.25, 0.5, 0.75, 1]))
                # if legend_bins.startswith('equal'):
                #     legend_bins = legend_bins.split(':')
                #     if len(legend_bins) != 2:
                #         bins = 6
                #     else:
                #         bins = legend_bins[1]
                # if legend_bins.startswith('custom'):
                #     legend_bins = legend_bins.split(':')
                #     if len(legend_bins) != 2:
                #         bins = 6
                #     else:
                #         legend_bins = legend_bins[1].split(',')
                #         bins = legend_bins
                if bins == 6:
                    value_list = set(map[map_field].dropna().unique())
                    if len(value_list) < 6:
                        bins = len(value_list)
                        if len(value_list) < 3:
                            bins = list(value_list)+[max(value_list)+1]+[max(value_list)+2]
                if len(map_field) > 1:
                    # make first letter of map field upper case for legend
                    legend_title = description[0].upper()+description[1:]
                else:
                    legend_title = description
                legend_name = f'{legend_title}, by {area_layer}{aggregation_text}'
                layer = folium.Choropleth(data=map,
                                geo_data =map.to_json(),
                                name = map_field,
                                columns =[linkage_id,map_field],
                                key_on=f"feature.properties.{linkage_id}",
                                fill_color='YlGn',
                                fill_opacity=0.7,
                                nan_fill_opacity=0.2,
                                line_opacity=0.2,
                                legend_name=legend_name,
                                bins = bins,
                                smooth_factor = None,
                                reset=True,
                                overlay = True
                                ).add_to(m)
                folium.features.GeoJsonTooltip(fields=data_fields,
                                               localize=True,
                                               labels=True, 
                                               sticky=True
                                               ).add_to(layer.geojson)    
                if '{}'.format(point_overlay_xy) not in ['','nan']:
                    point_layer = folium.features.GeoJson(data=point_overlay.to_json(), 
                                                          name=point_overlay_name, 
                                                          tooltip=f"feature.properties.{point_overlay_hover_field}"
                                                          ).add_to(m)
                    folium.features.GeoJsonTooltip(fields=[c for c in point_overlay.columns if c is not 'geometry'],
                                                   localize=True,
                                                   labels=True, 
                                                   sticky=True
                                                   ).add_to(point_layer)  
                # Add layer control
                folium.LayerControl(collapsed=False).add_to(m)
                m.fit_bounds(m.get_bounds())
                m.get_root().html.add_child(folium.Element(map_style))
                # Modify map 
                html = m.get_root().render()
                ## Wrap legend text if too long 
                ## (67 chars seems to work well, conservatively)
                if len(legend_name) > 65:
                    import textwrap
                    legend_lines = textwrap.wrap(legend_name, 65)
                    legend_length = len(legend_name)
                    n_lines = len(legend_lines)
                    legend_height = 25 + 15 * n_lines
                    old = f'''.attr("class", "caption")
        .attr("y", 21)
        .text('{legend_name}');'''
                    new = ".append('tspan')".join(['''.attr('class','caption')
        .attr("x", 0)
        .attr("y", {pos})
        .text('{x}')'''.format(x=x,pos=21+15*legend_lines.index(x)) for x in legend_lines])
                    html = html.replace(old,new)
                    html = html.replace('.attr("height", 40);',f'.attr("height", {legend_height});')
                # move legend to lower right corner
                html = html.replace('''legend = L.control({position: \'topright''',
                                    '''legend = L.control({position: \'bottomright''')
                # save map
                # map_name = '{}_ind_{}'.format(locale,map_name_suffix)
                fid = open(f'{output_dir}/html/{map_name}.html', 'wb')
                fid.write(html.encode('utf8'))
                fid.close()
                folium_to_image(os.path.join(output_dir,'html'),
                                os.path.join(output_dir,'png'),
                                map_name)
                print(f'\t- {output_dir}/html/{map_name}.html')
                print(f'\t- {output_dir}/png/{map_name}.png')
                print('')
    # output to completion log                  
    script_running_log(script, task, start, locale)
    engine.dispose()

if __name__ == '__main__':
    main()