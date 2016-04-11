#!/usr/bin/python

# analyze_empty_citieslist.py

import json

def main():
	"""analyzing empty cities list"""
	with open("cities.json", 'r') as inputFile:
		citiesData = json.load(inputFile)
	print "Analyzing %d countries" % (len(citiesData))
	emptyCitiesCountry = []
	for country in citiesData:
		if country.has_key('cities'):
			if not country['cities']:
				emptyCitiesCountry.append(country['country'])
		else:
			emptyCitiesCountry.append(country['country'])
	print "There are %d countries without cities:" % (len(emptyCitiesCountry))
	for emptyCountry in emptyCitiesCountry:
		print "\t- %s" % emptyCountry
	
if __name__ == '__main__':
	main()