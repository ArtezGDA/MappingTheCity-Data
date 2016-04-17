#!/usr/bin/python
#Artnapping-image

import urllib2
from bs4 import BeautifulSoup
from urlparse  import urljoin

def main():
    """artnapping"""
	url = "http://www.gestolenkunst.nl/gestolen%20overzicht.htm"  # change to whatever your url is
	page = urllib2.urlopen(url).read()
	soup = BeautifulSoup(page, "html.parser")

	base = "http://www.gestolenkunst.nl/"

	images = [urljoin(base,a["href"]) for a in soup.select("td a[href^=images/]")]

	for url in images:
		#Finds the images in a link out a table
    	img = BeautifulSoup(urllib2.urlopen(url).read(),"lxml").find("img")["src"]
    	with open("myimages/{}".format(img), "w") as f:
    		#Placed al the images in the map myImages
        	f.write(urllib2.urlopen("{}/{}".format(url.rsplit("/", 1)[0], img)).read())

if __name__ == "__main__":
    main()