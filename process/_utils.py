"""

Utility functions
~~~~~~~~~~~~~~~~~

Script:  
    _utils.py
Purpose: 
    These functions may be used in other scripts to undertake specific tasks.
Authors: 
    Carl Higgs
Context: 
    Liveability indicator calculation (general tools for data wrangling)

Todo:
    * further refactor and abstract code as functions for autodoc purposes
    
"""

import os
    
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

# function for printing dictionaries in 'pretty' format to screen 
def pretty(d, indent=0):
    """Print dictionary data structure in 'pretty' format to screen 
    
    Args:       
        d (dict): a python dictionary
    """
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
    """Check if a database table already exists
    
    Args:       
        name (str): a table which may or may not exist
    
    Outputs:
        ret (bool): a logical indication of existance (True or False)
    """
    ret = engine.dialect.has_table(engine, name)
    print('Table "{}" exists: {}'.format(name, ret))
    return ret

# function for returning a pandas type given a string value representing that type
def valid_type(str_of_type):
    """Function for returning a pandas type given a string value representing that type
    
    Args:       
        str_of_type (str): a python type in string form
    
    Outputs:
        the Pandas term for that type
    """
    if str_of_type in ['int','integer']:
        return('Int64')
    elif str_of_type in ['float','double precision']:
        return('float64')
    elif str_of_type in ['str','string','text','object']:
        return('object')
    else:
        return('object')

def style_dict_fcn(type = 'qualitative',colour=0):
    """Return a set of colours for use in maps
    
    Rationale:
        Make use of colourbrewer colour scheme readily accessible and swappable
    
    Args:       
        type (str): Either 'qualitative or 'diverging' for preset schemas
        colour (int): index number of colour to return
    
    Outputs:
        A png file in the specified output directory
    
    Todo:
        * re-think the purpose of this -- perhaps could use an existing colorbrewer library?
        * or just include the standard colorbrewer options (pgrn etc)
    """
    # Colours for presenting maps
    colours = {}
    # http://colorbrewer2.org/#type=qualitative&scheme=Dark2&n=8
    colours['qualitative'] = ['#1b9e77','#d95f02','#7570b3','#e7298a','#66a61e','#e6ab02','#a6761d','#666666']
    # http://colorbrewer2.org/#type=diverging&scheme=PuOr&n=8
    colours['diverging'] = ['#8c510a','#bf812d','#dfc27d','#f6e8c3','#c7eae5','#80cdc1','#35978f','#01665e']
    
    if type not in ['qualitative','diverging']:
        print("Specified type unknown; assuming 'qualitative'.")
        type = 'qualitative'
    return {
        'fillOpacity': 0.5,
        'line_opacity': 0.2,
        'fillColor': colours[type][colour],
        'lineColor': colours[type][colour]
    }

def compile_datasets(df_datasets,full_locale):
    df_datasets.name_s = df_datasets.name_s.fillna('')
    df_datasets.dimension = df_datasets.dimension.fillna('')
    datasets = ['population','boundaries','indicators','destinations']
    query_include = '|'.join(['purpose == "{}"'.format(p) for p in datasets])
    df_datasets = df_datasets.query(f'({query_include}) & region=="{full_locale}" & name_s!=""').copy()
    df_datasets.set_index('name_s',inplace=True)
    df_datasets.areas = df_datasets.areas.str.split(',')
    df_datasets = df_datasets.explode('areas')
    df_datasets.rename(columns={"areas": "linkage_layer"},inplace=True)
    return(df_datasets)

def expand_indicators(df):
    d = df.copy()
    d.rate = d.rate.str.split(',')
    d = d.explode('rate')
    d['rate_scale'] = d.rate.apply(lambda x: str(x).split(':')[-1]).replace(['nan','overall'],'1').astype('float')
    d.rate = d.rate.apply(lambda x: str(x).split(':')[0]).replace(['nan','overall'],'').str.strip()
    d['rate_units'] = d.rate.replace('area','km²').replace('households','household')
    d['table_out_name'] = d.index
    # set general naming convention for indicators
    d.loc[d.purpose=='indicators','table_out_name'] = d.loc[d.purpose=='indicators',:].apply(lambda x: '_'.join([str(x['linkage_layer']),
                                                               str(x.name),
                                                               ('', '_rate_'+str(x.rate))[str(x.rate) not in ['','nan']]])
                                                               .replace('__','_').rstrip('_'),
                                           axis=1)
    # set naming convention for accessibility indicators
    d.loc[d.type=='access','table_out_name'] = d.loc[d.type=='access',].apply(lambda x: '{}_access_{}_{}m_pop_pct'.format(x['linkage_layer'],
                                                                                                                          x.name,
                                                                                                                          x['resolution']),
                                                                              axis=1)
    # set destination name from index value for access indicators only
    d['destination'] = ''
    d.loc[d.type=='access','destination'] = d.loc[d.type=='access',].index
    # set table out name as the dataframe index
    d.index = d.table_out_name
    for field in ['alias']:
        d.loc[d.rate.astype('str') != '',field] = d.loc[d.rate.astype('str') != ''].apply(lambda x: (x[field], x[field] +' per {}'.format(
                                                                (x.rate_units,'{:,g} {}'.format(x.rate_scale,x.rate_units))[x.rate_scale!=1]
                                                              ))[x['rate'] != ''],
                                      axis=1)
                                      
    d.loc[d.rate.astype('str') != '','method_description_ind'] = d.loc[d.rate.astype('str') != ''].apply(lambda x: (x['method_description_ind'], 
                                                  x['method_description_ind'] 
                                                        + '  The indicator was rated as the rate per {}.'.format(
                                                                (x.rate_units,'{:,g} {}'.format(x.rate_scale,x.rate_units))[x.rate_scale!=1]
                                                              ))[x['rate'] != ''],
                                       axis=1) 
    
    d = d.drop_duplicates()
    return(d)

def folium_to_image(input_dir='',output_dir='',map_name='',formats=['png'],width=1000,height=800,pause=3,strip_elements=["leaflet-control-zoom","leaflet-control-layers"]):
    """This function converts an input html page to a png image
    
    Rationale:
        Leaflet is useful for creating interactive maps; this function is used to 
        re-purpose these as static maps too.
    
    Args:       
        input_dir (str): the input directory for an html file
        output_dir (str): the output directory for a png file
        map_name (str): the file basename
        formats (str): the desired output format
        width (int): width in pixels (default = 1000)
        height (int): height in pixels (default = 800)
        pause (int): a delay time to allow the web page to fully load (e.g. online basemaps)
        strip_elements (str array): A list of div tags to remove (e.g. interactive legend, zoom controls)
    
    Outputs:
        A png file in the specified output directory
    
    Todo:
        * input should be path not seperate dir and file; can get base path from the single file path
        * modify this to also allow to pdf -- perhaps using pdfkit
            * https://stackoverflow.com/questions/54390417/how-to-download-a-web-page-as-a-pdf-using-python
            * I think in future should use puppeteer with headless chrome (or pyppeteer)
    """
    import selenium.webdriver
    import time
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
            driver.save_screenshot(f'{output_dir}/{map_name}.png')
        if 'pdf' in formats:
            import pdfkit
            pdfkit.from_string(driver.page_source, f'{output_dir}/{map_name}.pdf')
            # with open("{}/__folium_temp.html".format(output_dir), "w") as f:
                # f.write(driver.page_source)
            # pdfkit.from_file("{}/__folium_temp.html".format(output_dir), 
                             # '{}/{}.pdf'.format(output_dir,map_name))
            # os.remove("{}/__folium_temp.html".format(output_dir))
        driver.close()
    except Exception as error:
        print("Export of {} failed.".format('{}/{}.png: {}'.format(output_dir,map_name,error)))

def define_geojson_coordinates(i,coords=['lat','long']):
    """Updates json coordinates for display as geojson.
    
    This function takes a json feature collection feature which has been 
    set up as though it were a geojson (ie. with correct structure and
    tags) and replaces the template null geometry tags with the actual
    coordinates recorded for that feature.
    
    Rationale:
        The `Air4Thai`_ data can be saved as json. 
        This records measurements for various pollutants at stations across 
        Thailand, as well as metadata for each station including its coordi-
        nates in latitude and longitude.  
        
        However some manipulation is required to reformat this json data for
        correct display as a geojson, retaining all the included attributes.
    
    Example input:
    
        ::
        
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        0,
                        0
                    ]
                },
                "properties": {
                    ...
                    "lat": "13.666183",
                    "long": "100.605742",
                    ...
               }
            }
        
    Example output:
    
        ::
        
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        100.605742,
                        13.666183
                    ]
                },
                "properties": {
                    ...
                    "lat": "13.666183",
                    "long": "100.605742",
                    ...
               }
            }
    
    Args:
        i (geojson feature): This is a geojson feature, containing incorrect
        coords (2-tuple of strings): a 2-item list of 
            string names for the latitude and longitude coordinates
    
    Returns:
        geojson feature: Geojson feature with coordinates replaced as per the specified
        coordinates in the input feature's properties record.
    
    .. _Air4Thai:
        http://air4thai.pcd.go.th

    """
    i['geometry']['coordinates'][0] = float(i['properties'][coords[1]])
    i['geometry']['coordinates'][1] = float(i['properties'][coords[0]])
    return i

def unnest_json_property(i,nested_property):
    """This function takes each item of the nested list and returns as a 
    property in its own right, prefixed by an underscore '_' to mitigate
    risk of name clash.  For any nested items, the nested list name is
    taken as a prefix and append to any child items.  
    
    Rationale:
        The `Air4Thai`_ data can be saved as json. 
        This records measurements for various pollutants at stations across 
        Thailand.  However, this is recorded as a nested list, which without 
        further processing (un-nesting) cannot be mapped or analysed directly.
    
    Args:
        i (geojson feature): This is a geojson feature, containing incorrect
        nested_property (string): a string identifying a nested property
    
    Returns:
        geojson feature: Geojson feature with its nested property un-nested.
    
    .. _Air4Thai:
        http://air4thai.pcd.go.th
    """
    for x in i['properties'][nested_property]:
        if type(i['properties'][nested_property][x]) is not dict:
            i['properties']['_{}'.format(x)] = i['properties'][nested_property][x]
        else:
            for n in i['properties'][nested_property][x]:
                i['properties']['_{}_{}'.format(x,n)] = i['properties'][nested_property][x][n]
    return i

def recast_json_properties(i,na=[]):
    """This function iterates over properties and recasts to integer or float 
    values as appropriate.  Any "N/A" values are replaced as numpy nan values.
    
    Rationale:
        The `Air4Thai`_ data can be saved as json. 
        This records measurements for various pollutants at stations across 
        Thailand.  However, numeric values are presented as strings, and 
        have hard-coded text "N/A" values for not applicable data.
    
    Args:
        i (json feature): This is a json feature
        na (string array): a list of strings representing values which should be 
        interpreted as nan
    
    Returns:
        geojson feature: Geojson feature with recast properties
    
    .. _Air4Thai:
        http://air4thai.pcd.go.th
    """
    import numpy as np
    for p in i['properties']:
        # print(i['properties'][p])
        if type(i['properties'][p]) is not dict:
            # if appears to be integer, cast to int
            if '{}'.format(i['properties'][p]).isdigit():
                i['properties'][p] = int(i['properties'][p])
            # if appears to be float, cast as float
            elif '{}'.format(i['properties'][p]).replace('.','',1).isdigit():
                i['properties'][p] = float(i['properties'][p])
            # if appears to be na, cast as np.nan
            elif '{}'.format(i['properties'][p]) in na:
                i['properties'][p] = np.nan
            # otherwise, let it be - probably a string
    
    return i

def add_json_datetime_property(i,date='_date',time='_time',format= '{d}T{t}:00',datetime_field='time'):
    """Format datetime field based on given date, time, and format.
    
    Rationale:
        Some applications require a joint date-time variable in a specific format.
        Given an input json feature with properties and the names of fields 
        representing 'date' and 'time', a 'datetime' field is returned.
    
    Args:
        i (geojson feature): This is a geojson feature, containing incorrect
        date (string): Property name of date string
        time (string): Property name of time string
        format (string): A parameterised format for combining these two fields
        datetime_field : A new field to contain the formatted datetime variable
    
    Returns:
        geojson feature: Geojson feature with date time variable
    """
    t = i['properties']['_time']
    d = i['properties']['_date']
    i['properties'][datetime_field] = format.format(d=d,t=t)
    return i

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
                     
# def generate_isid_csv_template(engine,area_layer, area_linkage_id, target_year, measure, units, schema, table, csv_file):
def generate_isid_csv_template(engine,df_row, out_path, schema='public', prefix='',suffix='',table='',measure=''):
    """Prepare a CSV data template according to ISID specifications
    
    Args:
        
    engine: sql db connection
    df_row: a dataframe row of indicator attributes (Pandas)
    out_path: directory to save file
    schema: SQL database schema (if not public)
    prefix: optional prefix for map table name (string)
    suffix: optional suffix for map table name (string)
    table: optional override of table name
    measure: optional override of table attribute to map
    
    Saves
    -------
    
    csv file matching template for upload to ISID map portal
    """
    import io
    import pandas
    
    if table =='':
        table = df_row.table_out_name
    # get information about this measure
    description = df_row.alias
    aggregation = df_row.aggregation
    area_layer = df_row.linkage_layer
    linkage_id = df_row.linkage_id
    map_field = df_row.map_field
    target_year = df_row.year_target
    units = df_row.units
    rate = df_row.rate
    rate_units = df_row.rate_units
    rate_scale = df_row.rate_scale
    units = format_units(units,rate_units,rate_scale)
    if measure=='':
        measure=map_field
    csv_file = f'{out_path}/{prefix}_{table}.csv'
    sql = f'''
            SELECT a.{linkage_id} AS "Census Id",
                   district_en AS "Boundary Name",
                   {target_year} AS Year,
                   {measure} AS "Value",
                   NULL AS "Trend"
            FROM {area_layer} a
            LEFT JOIN {schema}.{table} USING ({linkage_id})
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
    with open(csv_file, 'w') as output_file:
        output_file.write(csv_template)
    print(f'\t- {csv_file}')

def get_df_data_fields(df,fields):
    """
    Return attribute fields for df covariates for use when mapping
    
    df: a dataframe (eg of population data with various attributes)
    fields: a list of fields of interest when mapping

    Returns
    -------
    attributes list
    """
    import numpy as np
    df_numeric = [c for c in df.columns if np.issubdtype(df[c].dtype, np.number)]
    data_fields = fields.split(',')
    data_fields_full = ['area_sqkm']
    for f in data_fields:
        data_fields_full.append(f)
        if f in df_numeric:
            data_fields_full.append(f'{f} per sqkm')
    return(data_fields_full)
    
# def generate_map(engine,map_name,map_attribution, attribution, area, measure, description, map_field, linkage_id, schema, table, legend_bins, coalesce_na, data_fields,column_names, map_style,outpath, aggregation_text = '',point_overlay_xy= ''):
def generate_map(engine,df_row,out_path='.',data_fields='',prefix='',suffix='',map_attribution='',area_attribution='', map_style_html_css='',schema='public',table='',measure=''):
    """
    Generate html and png maps for a calculated indicator
    
    engine: sql db connection
    df_row: a dataframe row of indicator attributes (Pandas)
    data_fields: a list of fields of interest when mapping (list)
    prefix: optional prefix for map table name (string)
    suffix: optional suffix for map table name (string)
    map_attribution: attribution details for this map (ie. who is making it)
    area_attribution: attribution details for area layers
    map_tyle_html_css: html code defining style for map
    schema: schema where sql table is found
    table: optional override for table name (if other than defined in df_row)
    
    Saves
    -------
    
    html and png files
    """
    import geopandas as gpd
    import pandas as pd
    import folium
    import re
    if table =='':
        table = df_row.table_out_name
    map_name = f'{prefix}_ind_{table}'
    # get information about this measure
    description = df_row.alias
    aggregation = df_row.aggregation
    area = df_row.linkage_layer
    linkage_id = df_row.linkage_id
    point_overlay_xy = df_row.point_overlay_xy
    map_field = df_row.map_field
    if measure=='':
        measure=map_field
    source = df_row.provider
    year_published = df_row.year_published
    coalesce_na = str(df_row.coalesce_na)
    legend_bins = str(df_row.legend_bins)
    aggregation - df_row.aggregation
    aggregation_text = get_aggregation_text(aggregation)
    attribution = f'{map_attribution} | {area_attribution} | data: {source} ({year_published})'
    potential_column_width = len(f'{map_field}_{aggregation}')
    if potential_column_width < pd.get_option("display.max_colwidth"):
        pd.set_option("display.max_colwidth", potential_column_width)
    if data_fields!='':
        additional_data = ','.join([f'a."{d}"' for d in data_fields])
        if additional_data != '':
            additional_data = f'{additional_data},'
        # create dictionary of additional covariate names for mapping (with superscript 2)
        column_names = {}
        # format to display superscript 2 for square kilometres
        for f in data_fields:
            column_names[f] = f.replace('sqkm','km\u00B2')
    if coalesce_na in ['','nan']:
        sql = f'''
            SELECT a.{area},
                   {additional_data}
                   b.{measure},
                   ST_Transform(a.geom, 4326) AS geom 
            FROM {area} a
            LEFT JOIN {schema}.{table} b 
            USING ({linkage_id})
            '''
    else:
        sql = f'''
            SELECT a.{area},
                   {additional_data}
                   COALESCE(b.{measure},{coalesce_na}) AS "{measure}",
                   ST_Transform(a.geom, 4326) AS geom 
            FROM {area} a
            LEFT JOIN {schema}.{table} b 
            USING ({linkage_id})
            '''
    map = gpd.GeoDataFrame.from_postgis(sql, engine, geom_col='geom')
    map.rename(columns = {measure : map_field}, inplace=True)
    map.rename(columns = column_names, inplace=True)
    map.rename(columns = {'area_km\u00B2':'area (km\u00B2)'}, inplace=True)
    data_fields =[area]+[f.replace('sqkm','km\u00B2').replace('area_km\u00B2','area (km\u00B2)') for f in data_fields]+[map_field]    
    # get map centroid from study region
    xy = [float(map.centroid.y.mean()),float(map.centroid.x.mean())]    
    # initialise map
    m = folium.Map(location=xy, zoom_start=11, tiles=None,control_scale=True, prefer_canvas=True,attr='{}'.format(attribution))
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
    legend_bins = legend_bins
    if legend_bins in ['quartiles']:
        bins = list(map[map_field].quantile([0, 0.25, 0.5, 0.75, 1]))
    if legend_bins.startswith('equal'):
        legend_bins = legend_bins.split(':')
        if len(legend_bins) != 2:
            bins = 6
        else:
            bins = legend_bins[1]
    if legend_bins.startswith('custom'):
        legend_bins = legend_bins.split(':')
        if len(legend_bins) != 2:
            bins = 6
        else:
            legend_bins = legend_bins[1].split(',')
            bins = legend_bins
    if bins == 6:
        value_list = set(map[map_field].dropna().unique())
        if len(value_list) < 6:
            bins = len(value_list)
            print(bins)
            if len(value_list) < 3:
                bins = list(value_list)+[max(value_list)+1]+[max(value_list)+2]
    if len(description) > 1:
        # make first letter of description upper case for legend
        legend_title = description[0].upper()+description[1:]
    else:
        legend_title = description
    legend_name = f'{legend_title}, by {area}{aggregation_text}'
    layer = folium.Choropleth(data=map,
                    geo_data =map.to_json(),
                    name = map_field,
                    columns =[area,map_field],
                    key_on=f"feature.properties.{area}",
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
    m.get_root().html.add_child(folium.Element(map_style_html_css))
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
    
    ## Modify map heading (above legend)
    # color_map =  re.search(r"color_map_[a-zA-Z0-9_]*\b|$",html).group()
    # old = '{}.svg = d3.select(".legend.leaflet-control").append("svg")'.format(color_map)
    # new = f'''
    # {color_map}.title = d3.select(".legend.leaflet-control").append("div")
            # .attr("style",'vertical-align: text-top;font-weight: bold;')
            # .text("{heading}");
    # {color_map}.svg = d3.select(".legend.leaflet-control").append("svg")
    # '''
    # html = html.replace(old,new)
    
    # save map
    fid = open(f'{out_path}/html/{map_name}.html', 'wb')
    fid.write(html.encode('utf8'))
    fid.close()
    # folium_to_image(os.path.join(out_path,'html'),
                    # os.path.join(out_path,'pdf'),
                    # map_name,
                    # formats=['pdf'])
    folium_to_image(os.path.join(out_path,'html'),
                                os.path.join(out_path,'png'),
                                map_name)
    print(f'\t- {out_path}/html/{map_name}.html')
    print(f'\t- {out_path}/png/{map_name}.png')
    print('')

def get_aggregation_text(aggregation):
    """
    input: 
        aggregation: aggregation description (string)
    output: 
        formatted aggregation description or map field (string)
    """
    aggregation_text = ''
    if aggregation =='count':
        aggregation_text = f" ({aggregation})"
    elif aggregation =='sum':
        aggregation_text = f" ({aggregation})"
    elif aggregation == 'average':
        aggregation_text = f" ({aggregation})"
    elif aggregation == 'percent':
        aggregation_text = f" (%)"
    else:
        if str(aggregation)!='nan':
            print(f"The aggregation '{aggregation}' is not recognised")
        return('')
    return(aggregation_text)