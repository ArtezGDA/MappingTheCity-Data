#!/usr/bin/python
#weather.scraper

from bs4 import BeautifulSoup
import urllib

def main():
    """weather scraper"""
    r = urllib.urlopen("https://www.wunderground.com/history/airport/KPHL/2016/1/1/MonthlyHistory.html?&reqdb.zip=&reqdb.magic=&reqdb.wmo=&MR=1").read()
    soup = BeautifulSoup(r, "html.parser")
    tables = soup.find_all("table", class_="responsive airport-history-summary-table")

    scrapedData = {}
    for table in tables:
        print 'Weather Philadelphia'

        for tr in table.find_all("tr"):
            firstTd = tr.find("td")
            if firstTd and firstTd.has_attr("class") and "indent" in firstTd['class']:
                values = {}
                tds = tr.find_all("td")
                maxVal = tds[1].find("span", class_="wx-value")
                avgVal = tds[2].find("span", class_="wx-value")
                minVal = tds[3].find("span", class_="wx-value")
                print maxVal, avgVal, minVal
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
            # for each row of current table, write it using | between cells
            #print '|'.join([x.get_text().replace('\n','') for x in tr.find_all('td')])
            # header = trs[2].find_all("span")
            # print header[0]
            # print header[1]
            # print header[2]
    print scrapedData

if __name__ == "__main__":
    main()