import json
from LatLon import LatLon, Latitude, Longitude
 
tdata = open("masten2.json").read()
jdata = json.loads(tdata)
 
length = len(jdata)
 
def convert(coord):
    ind = coord.index('\xba')
    degree = float(coord[:ind-1])
    temp = coord[ind+1:].strip()
    ind = temp.index("'")
    minute = float(temp[:ind])
    second = float(temp[ind+1:].strip())
    return [degree, minute, second]
 
for i in range(0,length):
    lat = convert(jdata[i]["coordinates_la"].encode("utf8"))
    lon = convert(jdata[i]["coordinates_lo"].encode("utf8"))
 
    c = LatLon(Latitude(degree=lat[0], minute=lat[1], second=lat[2]), Longitude(degree=lon[0], minute=lon[1], second=lon[2]))
    jdata[i]["coordinates_la"] = float(c.lat)
    jdata[i]["coordinates_lo"] = float(c.lon)
 
with open('masten3.json', 'w') as outfile:
    json.dump(jdata, outfile)