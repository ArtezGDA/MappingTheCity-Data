#!/usr/bin/python
#weather.scraper

from bs4 import BeautifulSoup
import urllib

def main():
    """weather scraper"""
    r = urllib.urlopen("https://www.wunderground.com/history/airport/KPHL/2016/1/1/MonthlyHistory.html?&reqdb.zip=&reqdb.magic=&reqdb.wmo=&MR=1").read()
    soup = BeautifulSoup(r, "html.parser")
    tables = soup.find_all("table", class_="responsive airport-history-summary-table")

    for table in tables:
        print 'Weather Philadelphia'

        trs = table.find_all("tr")

        #for tr in trs:
            # for each row of current table, write it using | between cells
            #print '|'.join([x.get_text().replace('\n','') for x in tr.find_all('td')])
    header = trs[2].find_all("span")
    print header[0]
    print header[1]
    print header[2]

if __name__ == "__main__":
    main()