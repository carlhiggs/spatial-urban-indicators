import json
import os

# import custom _utils.py file
from _utils import *

folder_path = '../data/air4thai'

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
            json_data['features'][i] = add_json_datetime_property(
                                         recast_json_properties(
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
output = os.path.join(folder_path,'geojson_air4thai_combined.geojson')
with open(output, "w") as output_file:
    json.dump(geojson_join, output_file, indent=4, sort_keys=True)
print("Saved: {}".format(output))