#!/usr/bin/python
#Theft-alerts-image

import  requests

from bs4 import BeautifulSoup
from urlparse  import urljoin

def get_pages(start):
        soup = BeautifulSoup(requests.get(start).content, "lxml")
        images = [img["src"] for img in soup.select("div.itemspacingmodified a img")]
        yield  images
        nxt = soup.select("code.resultnav a")[-1]
        #Finds the images on the next pages
        while True:
            soup = BeautifulSoup(requests.get(urljoin(url, nxt["href"])).content)
            nxt = soup.select("code.resultnav a")[-1]
            if nxt.text != "Next":
                break
            yield [img["src"] for img in soup.select("div.itemspacingmodified a img")]
# change to whatever your url is
url = "http://www.theft-alerts.com/"
#Shows the names link of the images
for images in get_pages(url):
    print(images)
#Placed al the images in the map myImages
with open("myimages/{}".format(img), "w") as f:
    f.write(urllib2.urlopen("{}/{}".format(url.rsplit("/", 1)[0], img)).read())
if __name__ == "__main__":
    main()