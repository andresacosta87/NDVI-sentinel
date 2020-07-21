from sys import argv
from os.path import exists
import simplejson as json 

script, in_file, out_file = argv

data = json.load(open('farm_map.json'))

geojson = {
    "type": "FeatureCollection",
    "features": [
    {
        "type": "Feature",
        "geometry" : {
            "type": "Point",
            "coordinates": [d["lon"], d["lat"]],
            },
        "properties" : d,
     } for d in data]
}


output = open('farm_export', 'w')
json.dump(geojson, output)

#print geojson