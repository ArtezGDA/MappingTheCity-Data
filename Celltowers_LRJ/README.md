#Celltowers
Reinier, Leonie, Jeanine

### Process of scraping
First of we wanted to do something with all the mobile data traffic and ended up with all the celltowers of the Netherlands. We informed a company how they could assist us with receiving al this data about these towers. When we speak of data we mean:

- Location
- Type
- Coordinates
- Height

When we received an answer from this company they wanted something in return. So the first thing that came up was creating the posters and handing it over to them. Unfortunately we agreed not to do it. 

We found another paga/database of all the celltowers in the Netherlands. We came across the website "antennebureau.nl". On this same page there was an .ODS file(a file that works with Open Office). We had to download [Open Office](https://www.openoffice.org) to open this specific file.

We had to convert this data from the .ODS file to use it in a .JSON file. Reinier found a online converter named [Mr Data Converter](https://shancarter.github.io/mr-data-converter/). With this converter we could change the data from the .ODS file into data for a .JSON file.

After we created this .JSON file we came across another problem. The data of the coordinates was really messy and the data was not really useable. After we discussed this we had to change the file in a better way. We had to split up the pieces and make some of the data into floats so the terminal doesn't read it as text but as digits. 

When we did this we had converted 1 line of data and we had 41373 more lines to come. It was almost impossible for us to do this line by line. So had to make some of converter. 

Unfortunately we didnt have the knowlegde to create some sort off converting tool. We spoke to another student and he helped us out to create the tool to complete our task.

Last but probably not least of our problems we thought the file was still messy because all of this data was on 1 line. To solve we found this Sublime Text 2 plugin called [Pretty JSON](https://github.com/dzhibas/SublimePrettyJson). This little plugin gave the file a better overview of all this data.

###Data sources

[Antenne Bureau](http://www.antennebureau.nl/onderwerpen/algemeen/antenneregister) is the website we used for all data.

####Additional sources
- [Antenne Register](http://www.antenneregister.nl/)
- [GSMMasten](http://www.gsmmasten.nl/)
- [Ertyu](http://www.ertyu.org/steven_nikkel/cancellsites.html)
- [Data Overheid](https://data.overheid.nl/data/dataset/roet-ec-2014)
- [Data Overheid Standaarden](https://data.overheid.nl/data/dataset?theme_facet=http%3A%2F%2Fstandaarden.overheid.nl%2Fowms%2Fterms%2FNatuur_en_milieu)




###Json File

Our json file contains the following information

-	**city** - Location
-	**type** - Type celltower
-	**coordinates_la** - lattitude
-	**coordinates_lo** - longitude 
-	**x** - x position
-	**y** - y position
-	**ant_height** - the height of the antenna

###The MIT License (MIT)

Copyright (c) 2016 Graphic Design Arnhem at ArtEZ Academy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.