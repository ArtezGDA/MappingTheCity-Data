import json

with open("masten3.json", 'r') as inputFile:
    data = json.load(inputFile)

# Create two lists for latitude and longitude
latitudes = []
longitudes = []

for celltower in data:
	longitudes.append(celltower['coordinates_lo'])
	latitudes.append(celltower['coordinates_la'])

print max(latitudes)
print min(latitudes)
print max(longitudes)
print min(longitudes)