#Celltowers

team: Reinier, Leonie, Jeanine

###Data sources

http://www.antennebureau.nl/onderwerpen/algemeen/antenneregister

We used this website as a source for our data. 

This source contains all the coordinates of the celltowers in Holland. 

###Json File

Our json file contains the following information

-	city 
-	type: the type of celltower
-	coordinates_nb: lattitude
-	coordinates_ol: lottitude 
-	x
-	y
-	ant_height: the height of the celltower


### Process of scraping

We downloaded a .ods file wich we converted this one to a json file. 
First we changed the names that where used to define the information from Dutch to English. 
Then we cleaned up the notation. The way the coordinates where notated where messy so we startet with splitting the different coordinates so the terminal doesn't read it as text but as digits.
Now we are able to calculate the information we have. 
The next step will be creating a code that applies this specefic code to every line of the json file. 

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