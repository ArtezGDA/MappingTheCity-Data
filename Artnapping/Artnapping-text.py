import urllib2
from bs4 import BeautifulSoup

def main():
    """artnapping"""
url = 'http://www.gestolenkunst.nl/gestolen%20overzicht.htm'
soup = BeautifulSoup(urllib2.urlopen(url), "html.parser")

for index, table in enumerate(soup.find('table').find_all('table')):
    print "Table #%d" % index
    for tr in table.find_all('tr')[1:]:
        tds = tr.find_all('td')
        print "datum: %s\nplaats: %s\ngestolen van: %s\ngestolen: %s\n"% \
        (tds[0].text.strip(), tds[1].text.strip(), tds[2].text.strip(), tds[3].text.strip())

if __name__ == "__main__":
    main()