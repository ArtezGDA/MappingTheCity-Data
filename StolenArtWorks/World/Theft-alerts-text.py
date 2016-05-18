#!/usr/bin/python
#Theft-alerts-text

import urllib2
from bs4 import BeautifulSoup
import json

theftalerts = []
for i in range(1, 19):
	# change to whatever your url is
	connection = urllib2.urlopen("http://www.theft-alerts.com/index-%d.html" % i)

	soup = BeautifulSoup(connection.read().replace("<br>","\n"), "html.parser")

	# for the categories we wanted out the text
	for sp in soup.select("table div.itemspacingmodified"):
		theftDict = {}
		for wd in sp.select("div.itemindentmodified"):
			text = wd.text
			if text.startswith("Crime Ref"):
				ref = text.split(":")[1]
				ref = ref.strip()
				ref = ref.strip("\n")
				theftDict['CrimeRef'] = ref
			elif text.startswith("No of items stolen"):
				ref = text.split(":")[1]
				ref = ref.strip()
				ref = ref.strip("\n")
				theftDict['nItemsStolen'] = ref
			elif text.startswith("Location"):
				values = text.split("\n")
				for v in values:
					if v.startswith("Location"):
						ref = v.split(":")[1]
						ref = ref.strip()
						ref = ref.strip("\n")
						theftDict['Location'] = ref
					if v.startswith("Category"):
						ref = v.split(":")[1]
						ref = ref.strip()
						ref = ref.strip("\n")
						theftDict['Category'] = ref
					if v.startswith("ID"):
						ref = v.split(":")[1]
						ref = ref.strip()
						ref = ref.strip("\n")
						theftDict['ID'] = ref
			elif text.startswith("Item ONE"):
				ref = text.split(":")[1]
				ref = ref.strip()
				ref = ref.strip("\n")
				theftDict['ItemONE'] = ref
			elif text.startswith("Contact"):
				ref = text.split(":")[1]
				ref = ref.strip()
				ref = ref.strip("\n")
				theftDict['Contact'] = ref
			elif text.startswith("ID"):
				ref = text.split(":")[1]
				ref = ref.strip()
				ref = ref.strip("\n")
				theftDict['ID'] = ref
			else:
				print text
			if not text.startswith("Images :"):
				pass
		theftalerts.append(theftDict)

#Shows the results
print len(theftalerts)
#Makes a json file in your map
with open("theft-alerts.json", 'w') as outFile:
	json.dump(theftalerts, outFile, indent=2)