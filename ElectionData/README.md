# Election Data
Group:  Jesse, Kimberley, Patrick 


###Data sources step 1
1. **Genera:** 
	- http://thewebminer.com
	- https://datahub.io
	- https://www.quandl.com
	- http://www.kdnuggets.com/datasets/index.html
	- http://rs.io/100-interesting-data-sets-for-statistics/
	- http://blog.visual.ly/data-sources/
	- http://www.google.com/publicdata/directory
	- http://cjlab.stanford.edu/2015/09/30/lab-launch-and-data-sets/
	- http://kff.org/other/state-indicator/percent-who-had-all-teeth-extracted/#map
	- https://www.kaggle.com/rafadaguiar/d/kaggle/hillary-clinton-emails/email-network/code
1. **IQ:** 

	- https://iq-research.org/en/page/average-iq-by-country
	- http://www.statisticbrain.com/

1. **Election:** 
	- http://www.globalelectionsdatabase.com
	- http://www.nsd.uib.no/european_election_database/
	- http://www.eui.eu/Research/Library/ResearchGuides/Economics/Statistics/DataPortal/EED.aspx
	- http://www.idea.int/en/db/
	- http://www.presidency.ucsb.edu/elections.php
	- http://www.270towin.com/historical-presidential-elections/

1. **Final:** 
    - https://nl.wikipedia.org/wiki/Tweede_Kamerverkiezingen_ (2012, 2010..) .html
    - http://www.nlverkiezingen.com/TK(2012, 2010..) .html

## Source

As source for the ElectionData-Scraper for the NLVerkiezingen we used:

- http://www.nlverkiezingen.com/TK (2012, 2010..)



As source for the ElectionData-Scraper-Wikipedia we used Wikipedia

- https://nl.wikipedia.org/wiki/Tweede_Kamerverkiezingen_ (2012, 2010..)  

##Scraper
[ElectionDataScraper](elections scraper.py)

```
from bs4 import BeautifulSoup
import urllib
import json
import os
jaren = [str("2010"), str("2012")]
DESIRED_COLUMNS = {1, 2, 5} #scrapes only afk, aantal & zetels
verkiezingsData = []

filename = raw_input('Enter a filename: ') or 'data.json'

#open file and open json array
with open(filename, "w") as file:
    file.write("[{")
for Jaargetal in jaren:
    #url source 
    r = urllib.urlopen("http://www.nlverkiezingen.com/TK" + Jaargetal +".html").read()
    soup = BeautifulSoup(r, "html.parser")
    tables = soup.find_all("table")
    for table in tables:
        header = soup.find_all("h1")[0].getText()
        #print header
        with open(filename, "a+") as file:
            file.write("\"%s\": [" % header)
        trs = table.find_all("tr")[0].getText()
        #print '\n'

        del verkiezingsData[:] #clear list before adding new data
        #add the 3 columns to a list
        for tr in table.find_all("tr")[:22]: 
            for index, val in enumerate(tr.find_all('td')):
                 if index in DESIRED_COLUMNS:
                    verkiezingsData.append(val.getText().strip())

        #grab 3 values and write json array
        for a, b, c in zip(verkiezingsData[::3], verkiezingsData[1::3], verkiezingsData[2::3]):
    		data2 = {'afk':a,"aantal":b, "zetels":c}
    		with open(filename, 'a') as outfile:
      		    json.dump(data2, outfile)
                    outfile.write(",")

        #open file, delete last comma and close array
        with open(filename, 'ab+') as file:
            file.seek(-1, os.SEEK_END)
            file.truncate()
            file.write("],")

#open file, delete last comma, and close array
with open(filename, 'r+b') as file:
    file.seek(-1, os.SEEK_END)
    file.truncate()
    file.write("}]")
#open file and pretty print json data
with open(filename, 'r') as file:
    prettydata = json.load(file)
with open(filename, 'w') as file:
    json.dump(prettydata, file, sort_keys=True, indent=4, separators=(',', ': '))



```
##Result
As a result we got a JSON file called ElectionsData.json.

Top Level of this JSON is a number of votes, followed by the number of seats after the voting.

These are also the keys we used in the pythonfile.

##JSONFILE
[JSONFile](Elections Data.json)


```
[
    {
        "Tweede-Kamerverkiezingen - 12 september 2012": [
            {
                "aantal": "Aantal",
                "afk": "Afk.",
                "zetels": "Zetels"
            },
            {
                "aantal": "2504948",
                "afk": "VVD",
                "zetels": "41"
            },
            {
                "aantal": "2340750",
                "afk": "PvdA",
                "zetels": "38"
            },
            {
                "aantal": "950263",
                "afk": "PVV",
                "zetels": "15"
            },
            {
                "aantal": "909853",
                "afk": "SP",
                "zetels": "15"
            },
            {
                "aantal": "801620",
                "afk": "CDA",
                "zetels": "13"
            },
            {
                "aantal": "757091",
                "afk": "D66",
                "zetels": "12"
            },
            {
                "aantal": "294586",
                "afk": "CU",
                "zetels": "5"
            },
            {
                "aantal": "219896",
                "afk": "GrLinks",
                "zetels": "4"
            },
            {
                "aantal": "196780",
                "afk": "SGP",
                "zetels": "3"
            },
            {
                "aantal": "182162",
                "afk": "PvdD",
                "zetels": "2"
            },
            {
                "aantal": "177631",
                "afk": "50PLUS",
                "zetels": "2"
            },
            {
                "aantal": "30600",
                "afk": "Piraten",
                "zetels": ""
            },
            {
                "aantal": "18310",
                "afk": "MenS",
                "zetels": ""
            },
            {
                "aantal": "12982",
                "afk": "SOPN",
                "zetels": ""
            },
            {
                "aantal": "8194",
                "afk": "PvdT",
                "zetels": ""
            },
            {
                "aantal": "7363",
                "afk": "DPK",
                "zetels": ""
            },
            {
                "aantal": "4163",
                "afk": "LP",
                "zetels": ""
            },
            {
                "aantal": "2842",
                "afk": "NedLok",
                "zetels": ""
            },
            {
                "aantal": "2126",
                "afk": "LibDem",
                "zetels": ""
            },
            {
                "aantal": "2013",
                "afk": "AEP",
                "zetels": ""
            },
            {
                "aantal": "62",
                "afk": "NXD",
                "zetels": ""
            }
        ],
        "Tweede-Kamerverkiezingen - 9 juni 2010": [
            {
                "aantal": "Aantal",
                "afk": "Afk.",
                "zetels": "Zetels"
            },
            {
                "aantal": "1929575",
                "afk": "VVD",
                "zetels": "31"
            },
            {
                "aantal": "1848805",
                "afk": "PvdA",
                "zetels": "30"
            },
            {
                "aantal": "1454493",
                "afk": "PVV",
                "zetels": "24"
            },
            {
                "aantal": "1281886",
                "afk": "CDA",
                "zetels": "21"
            },
            {
                "aantal": "924696",
                "afk": "SP",
                "zetels": "15"
            },
            {
                "aantal": "654167",
                "afk": "D66",
                "zetels": "10"
            },
            {
                "aantal": "628096",
                "afk": "GrLinks",
                "zetels": "10"
            },
            {
                "aantal": "305094",
                "afk": "CU",
                "zetels": "5"
            },
            {
                "aantal": "163581",
                "afk": "SGP",
                "zetels": "2"
            },
            {
                "aantal": "122317",
                "afk": "PvdD",
                "zetels": "2"
            },
            {
                "aantal": "52937",
                "afk": "TROTS",
                "zetels": ""
            },
            {
                "aantal": "26196",
                "afk": "MenS",
                "zetels": ""
            },
            {
                "aantal": "10471",
                "afk": "Piraten",
                "zetels": ""
            },
            {
                "aantal": "7456",
                "afk": "Lijst17",
                "zetels": ""
            },
            {
                "aantal": "2042",
                "afk": "\u00e9\u00e9n",
                "zetels": ""
            },
            {
                "aantal": "2010",
                "afk": "NwNed",
                "zetels": ""
            },
            {
                "aantal": "1255",
                "afk": "HeelNL",
                "zetels": ""
            },
            {
                "aantal": "924",
                "afk": "EPN",
                "zetels": ""
            },
            {
                "aantal": "",
                "afk": "",
                "zetels": ""
            },
            {
                "aantal": "9416001",
                "afk": "",
                "zetels": "150"
            },
            {
                "aantal": "18147",
                "afk": "",
                "zetels": ""
            }
        ]
    }
]

```


