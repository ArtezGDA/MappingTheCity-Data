# Shirin Weather Poster Philadelphia

##### Shared Data collections with data sources about cities and agglomeration.

This repository will hold the collection of data that is to be researched and scraped for the [Mapping the City](https://github.com/ArtezGDA/Course-Material/blob/master/MappingTheCity.md) assignment.

Currently it contains two files:

- [List_of_Resources.md](List_of_Resources.md): a list containing possible source of data
- [Collaborative_Research.md](Collaborative_Research.md): a list of student groups and their research topics

For each research topic the following file structure should be created

- Folder with the topic of the research
	- a `README.md` file describing:
		- url: “https://www.wunderground.com/history/airport/KPHL/1980/1/7/MonthlyHistory.html?req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=“

		- meta data url: does not exist, wunderground is a research institution collecting data about temperatures of Philadelphia (US) from 1941-2016 sortable monthly, daily, weekly
		- As a group we were interested about the temperature fluctuations over the years in this case from 1985-2015 the month January (winter) and July (summer). This research aims to get an impression of the climate in Philadelphia and its changes
		- the data set contains all monthly data from 1941-2016
		- structure scrapped data: <br>[{{months{data},year{}},{},{},...]
		- tools: scraper
		- contributors: Sietske Bartens, Bella Naag, Shirin Pfisterer
	- [LallData_philly.json](allData_philly.json): find all scrapped data here

	- [Philadelphia_weather_scraper.py](Philadelphia_weather_scraper.üy) Philadelphia Weather Scraper
	- [LallData_philly.json](allData_philly.json)