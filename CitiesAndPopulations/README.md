# Cities and Populations

## Data collection of all the Cities in the World and their Populations

As source Wikipedia was used. The following (single) url was used as starting point of the data:

- https://en.wikipedia.org/wiki/Lists_of_cities_by_country

In total the scraping script analyzed **227** countries, found **17343** cities (or settlements), of which **12599** cities have a population figure.

### Result

The result of all the scraping is a JSON file called **`population_of_cities.json`**.

Top level of this JSON is a list with *countries*. Then for each country we have the following keys:

- `country`: the name of the country
- `citiesList`: the wikipedia page title of the *list of cities* for this country.
- `cities`: a list of cities. Each city can have the following keys:
	- `name`: the name of the city
	- `url`: the url of the wikipedia page of this city
	- `lon`: the *longitude* of the location of the city (as Float)
	- `lat`: the *latitude* of the location of the city (as Float)
	- `population`: the number of inhabitants of the city

Not all keys will be present for all countries and cities.  
`citiesList` can be an empty string (`""`) if wikipedia doesn't have a page listing the cities for that country. Therefor some countries won't have a `cities` list or the list will be empty.  
If a city does not have a coordinate (in Wikipedia) it will not be listed, so all cities have a `name`, a `url`, a `lon` and a `lat`. However there are a lot of cities that do not have a population, because the *population* row could not be found in the `infobox` or because it only contained irrelevant keys (like Demonym or Density).  
So in processing the JSON files, take into account that some keys can be empty or missing.

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

### Ways to improve this list

Despite the efforts to create this list and scrape the cities, not all the cities will be included in this list. The following countries and issues should be looked after to see if the data can be improved:

- Brazil (list of cities should maybe be this one instead https://en.wikipedia.org/wiki/List_of_municipalities_of_Brazil)
- Barbados is has an empty cities list
- Akrotiri and Dhekelia is empty
- Dominica is empty
- Ecuador is empty (scraping the list of cities should also attempt to parse `ul` and `ol` inside a div (maybe only with `class_="div-col"`))
- Gibraltar is empty (should have a list of one city: Gibraltrar)
- ... more countries are empty
- Fix Tehran (`<span style="display:none" class="sortkey">7,006,884,678,200,000,000♠</span>`) and similar
- Remove Guangdong (and other provinces)
- Remove Bihar (and other states)


##### Authored by Dirk van Oosterbosch
