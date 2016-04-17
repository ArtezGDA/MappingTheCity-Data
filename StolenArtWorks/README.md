# Stolen artworks

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

Some of the `Date` are not complete, linke only a year date.

### Process

```
https://en.wikipedia.org/wiki/Lists_of_cities_by_country
     +
     |
     |         ╔════════════════════════════╗
     |         ║                            ║
     +--------->  scrape_wiki_countries.py  ║
               ║                            ║
               ╚════════════════════════════╝
                             |
                             |
                             v
                  +----------+--------+\
                  |                   | \
                  |   countries.json  +--\
                  |                      |
                  +----------+-----------+
                             |
     +-----------------------+
     |
     |          ╔══════════════════════════╗
     |          ║                          ║
     +---------->  scrape_wiki_cities.py   ║
                ║                          ║
                ╚════════════╤═════════════╝
                             |
                             |
                             v
                    +--------+-------+\
                    |                | \
                    |   cities.json  +--\
                    |                   |
                    +--------+----------+
                             |
     +-----------------------+
     |
     |      ╔══════════════════════════════════╗
     |      ║                                  ║
     +------>  scrape_wiki_city_population.py  ║
            ║                                  ║
            ╚════════════════╤═════════════════╝
                             |
                             |
                             v
               +-------------+-----------+\
               |                         | \
               |  city_populations.json  +--\
               |                            |
               +-------------+--------------+
                             |
     +-----------------------+
     |
     |          ╔══════════════════════════╗
     |          ║                          ║
     +---------->  analyze_populations.py  ║
     |          ║                          ║
     |          ╚═════════╤════════════════╝
     |                    |
     |                    |     +-----------------------------+
     |                    |     |                             |
     |      ╔═════════════v═════v══════════════╗              |
     |      ║                                  ║           Iterate
     +------>  analyze_populations_filter.py   ║            until
     |      ║                                  ║          satisfied
     |      ╚════════════════╤═════════════════╝              ^
     |                       |                                |
     |                       +--------------------------------+
     |
     |          ╔══════════════════════════╗
     |          ║                          ║
     +---------->  filter_populations.py   ║
                ║                          ║
                ╚════════════╤═════════════╝
                             |
                             |
                             v
             +---------------+--------------+\
             |                              | \
             |   population_of_cities.json  +--\
             |                                 |
             +---------------------------------+
```	

### More information

While creating and debuggin this scraping script, detailed notes were taken for lecturing purposes. Read these [Lecture Notes](https://github.com/ArtezGDA/Course-Material/blob/master/Lesson_09_Scraping_Notes.md) to learn more about the evolution of this code.

And because the results of that research were copied into this repository, the original commits are missing here. To find out and read the original commits, please refer to the [original repository](https://github.com/ArtezGDA/Course-Material/tree/master/ScrapingLecture)


##License (MIT License)

Apeace Leaflet is released under the MIT license.

Copyright © 2016 Lydienne Albertoe, Esmee Ellson and Angela ten Nag.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.