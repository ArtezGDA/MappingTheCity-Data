# Shirin Weather Poster Philadelphia

The following is the description of the data scraper Weather Poster Philadelphia.
“Wunderground” is a research institution collecting data about temperatures of Philadelphia (US) from 1941-2016 sortable monthly, daily, weekly. Please find the URL here:
	- Source URL: <br>“https://www.wunderground.com/history/airport/KPHL/1980/1/7/MonthlyHistory.html?req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=“
		
- As a group we were interested about the temperature fluctuations over the years in this case from 1985-2015 the month January (winter) and July (summer). This research aims to get an impression of the climate in Philadelphia and its changes

- the data set contains all monthly data from 1941-2016

- structure scrapped data: <br>[<br>{<br>{months<br>{data},<br>year{}<br>},<br>{},<br>{},<br>...]
		<br>- tools: scraper
		<br>- contributors: Sietske Bartens, Bella Naag, Shirin Pfisterer
	- [LallData_philly.json](allData_philly.json): find all scrapped data here

	- [Philadelphia_weather_scraper.py](Philadelphia_weather_scraper.py) Philadelphia Weather Scraper
	- [LallData_philly.json](allData_philly.json)
