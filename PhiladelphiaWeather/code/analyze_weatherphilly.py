#!/usr/bin/python

import json

def main():
    """docstring for main"""
    with open('january_2016.json', 'r') as inputFile:
        scrapedData = json.load(inputFile)
    print "%d properties of weahter" % (len(scrapedData))
    #
    # Loop through the data
    for prop in scrapedData:
    	# Get the name of the property (e.g. 'Max Temperature')
    	propertyName = prop.keys()[0]
    	# Get the values of this property
    	values = prop[propertyName]
    	# Continue only if there are values
    	if values.keys():
    		# Print the property name
	    	print "{}:".format(propertyName)
	    	#
	    	# Loop through the values
	    	for k in values.keys():
	    		# Get each value
	    		value = values[k]
	    		# And print it
	    		print "\t{}: {}".format(k, value)


if __name__ == '__main__':
    main()
