#!/usr/bin/python

import json
# import collections

jsonFile='data.json'

with open(jsonFile,'r') as inputFile:
	data = json.load(inputFile)
	print "%d accidents in %s" % (len(data),jsonFile)

types = []
typesAndCount = []

for accident in data:
	industry = accident['Province']
	if industry in types:
		indexOfType = types.index(industry)
		typeCountDict = typesAndCount[indexOfType]
		typeCountDict['count'] = typeCountDict['count'] + 1
	else:
		types.append(industry)
		# create dict to count
		typeCount = {}
		typeCount['name'] = industry
		typeCount['count'] = 1
		typesAndCount.append(typeCount)

print types
print typesAndCount
with open('provinces.json', 'w') as outputFile:
	json.dump(typesAndCount, outputFile, indent = 2)