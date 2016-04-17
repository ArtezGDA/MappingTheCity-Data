# Stolen artworks
Lydienne, Esmee en Angela

## Data collection of all the stolen artworks in the Netherlands.

As source is the following url used:

- http://www.gestolenkunst.nl/gestolen%20overzicht.htm

In total the scraping script analyzed **143** stolen art works, found the date, place, from who, what and the images off the art works.

- Code source:

### Results

The result of all the scraping is a map off Images called **`myimages`** and JSON file called **`stolen _artworks.json`**.<br>
[JSON file](stolen_artworks.json)

###### The image map is a map with *stolen artworks images*. 

Not all images are placed in the map because some images have the same name that gives errors. 


###### The JSON file is a list with *stolen artworks*. 
For each stolen artwork there are the following keys:

- `Date`: the date off each stolen artwork.
- `Link`: the image link of off each stolen artwork.
- `Title`: What kind of artwork and the name who has made it.
	- `Extra information`: if it's found back, how much it's worth or if the offender is arrested.
- `Place`: the place where it is stolen and in there:
	- `m` the coordinate x.
	- `m` the coordinate y.
- `FromWho`: from the person or company that the artwork belongs too.

Not all keys will be present for the Extra information.  
`Extra information` can be an empty string or it stands after (`\r\n`) 

Some of the `Date` are not complete, like only a year date.

### Process scraping

[Image](Artnapping-image.py)

```
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

```	
[Text](Artnapping-text.py)

```
#!/usr/bin/python
#Artnapping-text

import urllib2
from bs4 import BeautifulSoup
import json

def main():
    """artnapping"""
    url = 'http://www.gestolenkunst.nl/gestolen%20overzicht.htm' # change to whatever your url is
    soup = BeautifulSoup(urllib2.urlopen(url), "html.parser")

    artworks = []
    for index, table in enumerate(soup.find('table').find_all('table')):
        print "Table #%d" % index
        for tr in table.find_all('tr')[1:]:
        # for each row of the table among divided into categories in rows
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
            #Shows the results
    with open("stolen_artworks.json", 'w') as outFile:
        #Makes a json file in your map 
        json.dump(artworks, outFile, indent=2)

if __name__ == "__main__":
    main()
    
```	

##License (MIT License)

Apeace Leaflet is released under the MIT license.

Copyright © 2016 Lydienne Albertoe, Esmee Ellson and Angela ten Nag.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.