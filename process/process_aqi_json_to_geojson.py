import json
import os

folder_path = '../data/air4thai'


def define_geojson_coordinates(i,
            coords=['lat','long']):
    """Updates air4thai json coordinates for display as geojson
    
    The `Air4Thai`_ data can be saved as json. 
    This records measurements for various pollutants at stations across 
    Thailand, as well as metadata for each station including its coordi-
    nates in latitude and longitude.  
    
    However some manipulation is required to reformat this json data for
    correct display as a geojson, retaining all the included attributes.
    
    This function takes a json feature collection feature which has been 
    set up as though it were a geojson (ie. with correct structure and
    tags) and replaces the template null geometry tags with the actual
    coordinates recorded for that feature.
    
    Example input:
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
                "stationID": "05t",
                "nameTH": "กรมอุตุนิยมวิทยาบางนา",
                "nameEN": "Thai Meteorological Department ",
                "areaTH": "แขวงบางนา, เขตบางนา, กรุงเทพฯ",
                "areaEN": "Bang Na, Khet Bang Na, Bangkok",
                "stationType": "GROUND",
                "lat": "13.666183",
                "long": "100.605742",
                ...
           }
        }
    Example output:
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
    
    .._Air4Thai:
        http://air4thai.pcd.go.th
    
    Todo:
        * abstract function further and add to utils.py module

    """
    i['geometry']['coordinates'][0] = float(i['properties'][coords[1]])
    i['geometry']['coordinates'][1] = float(i['properties'][coords[0]])
    return i

def unnest_json_property(i,nested_property):
    """ Un-nests a nested property list and returns these as new properties
    The air4thai data (http://air4thai.pcd.go.th) can be saved as json. 
    This records measurements for various pollutants at stations across 
    Thailand.  However, this is recorded as a nested list, which without 
    further processing (un-nesting) cannot be mapped or 
    analysed directly.
    
    This function takes each item of the nested list and returns as a 
    property in its own right, prefixed by an underscore '_' to mitigate
    risk of name clash.  For any nested items, the nested list name is
    taken as a prefix and append to any child items.  
    
    Once updated with the new un-nested properties, the object is returned.
    
    Args:
        i (geojson feature): This is a geojson feature, containing incorrect
        nested_property (string): a string identifying a nested propert
    Returns:
        geojson feature: Geojson feature with its nested property un-nested.
    """
    for x in i['properties'][nested_property]:
        if type(i['properties'][nested_property][x]) is not dict:
            i['properties']['_{}'.format(x)] = i['properties'][nested_property][x]
        else:
            for n in i['properties'][nested_property][x]:
                i['properties']['_{}_{}'.format(x,n)] = i['properties'][nested_property][x][n]
    return i

def recast_geojson_properties(i,na=[]):
    """ Attempt to cast geojson strings to numeric or float as appropriate
    The air4thai data (http://air4thai.pcd.go.th) can be saved as json. 
    This records measurements for various pollutants at stations across 
    Thailand.  However, numeric values are presented as strings, and 
    have hard-coded text "N/A" values for not applicable data.
    
    This function iterates over properties and recasts to integer or float 
    values as appropriate.  Any "N/A" values are replaced as 
    
    Args:
        i (geojson feature): This is a geojson feature, containing incorrect
        na (string array): a list of strings representing values which should be 
        interpreted as nan
    Returns:
        geojson feature: Geojson feature with recast properties
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

def add_geojson_datetime_property(i,date='_date',time='_time',format= '{d}T{t}:00',datetime_field='time'):
    """ Format datetime field based on given date, time, and format
    
    Some applications require a joint date-time variable in a specific format.
    Given an input json feature with properties and the names of fields 
    representing 'date' and 'time', a 'datetime' field is returned 
    
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


master_geojson_initialised = False
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path,filename)
        output = '{}.geojson'.format(os.path.splitext(file_path)[0])
        
        with open(file_path, 'r') as f:
            raw_data = f.read()
        
        # remove line breaks
        data = raw_data.replace('\r\n','')
        # add on feature collection header and tail
        data = data.replace('{"stations":','{"type": "FeatureCollection", "features":')
        # add on feature wrapper for properties
        data = data.replace('{"stationID":','{"type": "Feature", "geometry": {"type": "Point","coordinates": [0,0]},"properties": {"stationID":')
        # add on tail for new feature
        data = data.replace('"}}}','"}}}}')
        
        # load data string as a json structure
        json_data = json.loads(data)
        
        for i in range(0,len(json_data['features'])):
            json_data['features'][i] = add_geojson_datetime_property(
                                         recast_geojson_properties(
                                           i = unnest_json_property(
                                                 i = define_geojson_coordinates(json_data['features'][i]),
                                                 nested_property='LastUpdate'),
                                           na = ["N/A","-"])
                                           )
        
        # output formatted geojson data to file
        with open(output, "w") as output_file:
            json.dump(json_data, output_file, indent=4, sort_keys=True)
        print("Saved: {}".format(output))
        if not master_geojson_initialised:
            geojson_join = json_data
            master_geojson_initialised = True
        else:
            geojson_join['features'] = geojson_join['features'] + json_data['features']
        i+=1
        
# output combine geojson features to file (e.g. for timeseries mapping)
with open(output, "w") as output_file:
    json.dump(geojson_join, output_file, indent=4, sort_keys=True)