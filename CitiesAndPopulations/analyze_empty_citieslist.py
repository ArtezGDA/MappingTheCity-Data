#!/usr/bin/python

# analyze_empty_citieslist.py

import json

def main():
	"""analyzing empty cities list"""
	with open("cities.json", 'r') as inputFile:
		citiesData = json.load(inputFile)
	print "Analyzing %d countries" % (len(citiesData))
	emptyCitiesCountry = []
	for i, country in enumerate(citiesData):
		if country.has_key('cities'):
			if not country['cities']:
				emptyCountryDict = {}
				emptyCountryDict['index'] = i
				emptyCountryDict['country'] = country['country']
				emptyCitiesCountry.append(emptyCountryDict)
		else:
			emptyCountryDict = {}
			emptyCountryDict['index'] = i
			emptyCountryDict['country'] = country['country']
			emptyCitiesCountry.append(emptyCountryDict)
	print "There are %d countries without cities:" % (len(emptyCitiesCountry))
	for emptyCountry in emptyCitiesCountry:
		print "  %d: \t%s" % (emptyCountry['index'], emptyCountry['country'])
	
if __name__ == '__main__':
	main()