#!/usr/bin/python
import urllib2

import  requests
import urllib
from bs4 import BeautifulSoup
from urlparse  import urljoin

def get_pages(start):
        soup = BeautifulSoup(requests.get(start).content, "lxml")
        images = [img["src"] for img in soup.select("div.itemspacingmodified a img")]
        yield  images
        nxt = soup.select("code.resultnav a")[-1]
        while True:
            soup = BeautifulSoup(requests.get(urljoin(url, nxt["href"])).content)
            nxt = soup.select("code.resultnav a")[-1]
            if nxt.text != "Next":
                break
            yield [img["src"] for img in soup.select("div.itemspacingmodified a img")]

url = "http://www.theft-alerts.com/"

for images in get_pages(url):
    for img in images:
        print(img)
        filename = img.split('/')[-1]
        urllib.urlretrieve(img, filename)