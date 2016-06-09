#!/usr/bin/python
#weather.scraper

from bs4 import BeautifulSoup
import urllib
import json

def main():
    # weatherData = weather_philadelphia_data #Json beginns here
    # with open(jsonfile, 'w') as outputFile:
    #     json.dump(weatherData, outputFile)
    # #scrapping beginns here
    r = urllib.urlopen("https://www.wunderground.com/history/airport/KPHL/1980/1/7/MonthlyHistory.html?req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=").read()
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
    # filter only interested data
    weatherPerMonth = {}
    filteredProperties = ["Max Temperature", "Min Temperature"]
    for wd in weatherdata:
        firstKey = wd.keys()[0]
        if firstKey in filteredProperties:
            weatherPerMonth[firstKey] = wd[firstKey]


    with open ("july_1980.json", 'w' ) as outFile:
        json.dump(weatherPerMonth, outFile, indent=2)


print "done"
if __name__ == "__main__":
    main()