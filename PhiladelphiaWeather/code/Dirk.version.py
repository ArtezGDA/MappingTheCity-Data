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
    r = urllib.urlopen("https://www.wunderground.com/history/airport/KPHL/2016/1/1/MonthlyHistory.html?&reqdb.zip=&reqdb.magic=&reqdb.wmo=&MR=1").read()
    soup = BeautifulSoup(r, "html.parser")
    tables = soup.find_all("table", class_="responsive airport-history-summary-table")

    weatherdata = []
    scrapedData = {}
    for table in tables:

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
                scrapedData[firstTd.text] = values
                weatherdata.append(scrapedData)

    with open ("january_2016.json", 'w' ) as outFile:
        json.dump(weatherdata, outFile, indent=2)
print "done"
if __name__ == "__main__":
    main()