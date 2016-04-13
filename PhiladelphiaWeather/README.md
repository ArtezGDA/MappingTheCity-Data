#Philadelphia

Team 4: Shirin, Bella, Sietske 

###Data sources

1. **General:** https://www.opendataphilly.org/
	- http://www.city-data.com/forum/philadelphia/
	- http://www.city-data.com/city/Philadelphia-Pennsylvania.html
2. **Crime:** https://www.phillypolice.com/crime-maps-stats/ 
	- http://data.inquirer.com/crime
	- https://www.crimereports.com/agency/philadelphia
	- http://www.neighborhoodscout.com/pa/philadelphia/crime/
	- https://www.opendataphilly.org/dataset/crime-incidents
	- http://nis.cml.upenn.edu/crimebase/ 
	- http://www.trulia.com/local/philadelphia-pa/tiles:1%7Cpoints:1_crime
	- <i>**Police**</i> https://www.opendataphilly.org/dataset?tags=Police+Department
3. **Weather:** https://www.wunderground.com/history/airport/KPHL/2013/12/1/DailyHistory.html
4. **Trees:** https://www.opentreemap.org/phillytreemap/map/
5. **Historic landmarks:** http://www.pasda.psu.edu/uci/FullMetadataDisplay.aspx?file=PhiladelphiaHistoricSites_NatlReg201201.xml
6. **Public art:** http://philart.net/
7. **Architecture:** http://www.preservationalliance.com/directory/mcmar/index.php
8. **Transportation:** https://www.opendataphilly.org/dataset?groups=transportation-group
	- **Parks/Recreation:** https://www.opendataphilly.org/dataset?groups=transportation-group&groups=parks-recreation-group
9. **Real Estate:** https://www.opendataphilly.org/dataset?groups=real-estate-land-records-group
10. **History:** https://www.opendataphilly.org/dataset?groups=real-estate-land-records-group&groups=arts-culture-history-group

###Scraping History

Original url: [Philadephia weather](https://www.wunderground.com/history/airport/KPHL/2016/1/1/MonthlyHistory.html?&reqdb.zip=&reqdb.magic=&reqdb.wmo=&MR=1)

```
from bs4 import BeautifulSoup
import urllib2
url = "https://www.wunderground.com/history/airport/KPHL/2016/1/1/MonthlyHistory.html?&reqdb.zip=&reqdb.magic=&reqdb.wmo=&MR=1"  #

page = urllib2.urlopen(url).read()
import urllib
urllib.urlopen("https://www.wunderground.com/history/airport/KPHL/2016/1/1/MonthlyHistory.html?&reqdb.zip=&reqdb.magic=&reqdb.wmo=&MR=1").read()

r = urllib.urlopen("https://www.wunderground.com/history/airport/KPHL/2016/1/1/MonthlyHistory.html?&reqdb.zip=&reqdb.magic=&reqdb.wmo=&MR=1").read()
BeautifulSoup(r)

soup = BeautifulSoup(r)
soup.findAll("table”)

table = soup.findAll(“table”)
new.table = soup.find_all("table", class_="responsive airport-history-summary-table")

Structure of Json file
[{“header”:
					{”fact 1”:”max”, “avg”, “min”, “sum”},
					{”fact 2”:”max”, “avg”, “min”, “sum”}
					{”fact 3”:”max”, “avg”, “min”, “sum”}}
]
```
