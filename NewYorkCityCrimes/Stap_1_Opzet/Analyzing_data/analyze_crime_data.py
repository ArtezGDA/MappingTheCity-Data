import json

jsonFile = 'manhattan.json' 

with open(jsonFile, 'r') as inputFile:
    data = json.load(inputFile)
print "%d crimes in %s" % (len(data), jsonFile)

# Analyze the types of offenses
typesOfOffenses = []
offensesAndTheirCount = []
for crime in data:
	typeOfO = crime['Offense']
	if typeOfO in typesOfOffenses:
		# We already have this type of offense
		#
		# Get the index of the type in the list of strings
		indexOfType = typesOfOffenses.index(typeOfO)
		# Get already stored dictionary
		offenseType = offensesAndTheirCount[indexOfType]
		# Increment the count by 1
		offenseType['count'] += 1
	else:
		# This type of offense was not yet found
		offenseType = {}
		offenseType['name'] = typeOfO
		offenseType['count'] = 1
		offensesAndTheirCount.append(offenseType)
		typesOfOffenses.append(typeOfO)
# print the results
print offensesAndTheirCount		