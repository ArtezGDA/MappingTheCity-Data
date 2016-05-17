#!/usr/bin/python
#weather.scraper
from bs4 import BeautifulSoup
import urllib
import json

allData = []
# this loops through all the Weather years
for y in range(1941, 2017):
    yearData = {}
    yearData['year'] = y
    months = []
    for m in range(1, 13):
        def main():
        # weatherData = weather_philadelphia_data #Json beginns here
        # with open(jsonfile, 'w') as outputFile:
        #     json.dump(weatherData, outputFile)
        # scrapping beginns here
            url = "https://www.wunderground.com/history/airport/KPHL/%d/%d/1/MonthlyHistory.html" % (y, m)
            r = urllib.urlopen(url).read()
            soup = BeautifulSoup(r, "html.parser")
            tables = soup.find_all("table", class_="responsive airport-history-summary-table")

            weatherdata = []
            for table in tables: #reason for it to do it 12x

                for tr in table.find_all("tr"):
                     firstTd = tr.find("td")
                     if firstTd and firstTd.has_attr("class") and "indent" in firstTd['class']:
                         values = {}
                         tds = tr.find_all("td")
                         maxVal = tds[1].find("span", class_="wx-value")
                         avgVal = tds[2].find("span", class_="wx-value")
                         minVal = tds[3].find("span", class_="wx-value")
                         if maxVal:
                             values['max'] = maxVal.text
                         if avgVal:
                             values['avg'] = avgVal.text
                         if minVal:
                             values['min'] = minVal.text
                         if len(tds) > 4:
                             sumVal = tds[4].find("span", class_="wx-value")
                             if sumVal:
                                 values['sum'] = sumVal.text
                         scrapedData = {}
                         scrapedData[firstTd.text] = values
                         weatherdata.append(scrapedData)
                         break
                         monthData = {}
                         monthData['month'] = m
                         monthData['weather'] = weatherPerMonth
                         months.append(monthData)
            yearData['months'] = months
            allData.append(yearData)

            with open ("%d_%d.json", 'w' ) as outFile:
                json.dump(allData, outFile, indent=2)


print "done"
if __name__ == "__main__":
    main()
