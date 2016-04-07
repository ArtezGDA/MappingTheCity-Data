import urllib2
from bs4 import BeautifulSoup

url = "http://www.gestolenkunst.nl/gestolen%20overzicht.htm"  # change to whatever your url is
page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")
link = soup.a

def main():
	"""scrape some wikipedia"""

for link in soup.find_all('a'):
	print link["href"]
	print link.renderContents()