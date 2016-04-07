#!/usr/bin/python


import urllib2
from bs4 import BeautifulSoup
import json

def main():
    """artnapping"""
    url = 'http://www.gestolenkunst.nl/gestolen%20overzicht.htm'
    soup = BeautifulSoup(urllib2.urlopen(url), "html.parser")

    artworks = []
    for index, table in enumerate(soup.find('table').find_all('table')):
        print "Table #%d" % index
        for tr in table.find_all('tr')[1:]:
            tds = tr.find_all('td')
            datum = tds[0].text.strip()
            plaats = tds[1].text.strip()
            van = tds[2].text.strip()
            laatsteTd = tds[3]
            werk = laatsteTd.text.strip()
            anchor = laatsteTd.find('a')
            artwork = {}
            artwork['datumString'] = datum
            artwork['plaatsNaam'] = plaats
            artwork['fromWho'] = van
            artwork['titel'] = werk
            if anchor:
                artwork['link'] = anchor['href']#link
            artworks.append(artwork)
            print "datum: %s\nplaats: %s\ngestolen van: %s\ngestolen: %s\n" % (datum, plaats, van, werk)
    with open("stolen_artworks.json", 'w') as outFile:
        json.dump(artworks, outFile, indent=2)

if __name__ == "__main__":
    main()