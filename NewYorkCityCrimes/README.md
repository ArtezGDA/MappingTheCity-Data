# New York City Crimes

##Source
<br>

This is the web page where we use our data from. 

https://data.cityofnewyork.us/Public-Safety/NYPD-7-Major-Felony-Incidents/hyij-8hr7

<br>
## The purpose of the research, research goal or hypothesis
<br>
The purpose of this research is to discover what kind of crime is most common in which borough. We have decided to focus on three neighborhoods that are very different from each other in terms of amount of tourism in that area and the general image of the wealth in that area. Manhattan is the paragon of an upperclass neighborhood with heaps of tourism while Bronx on the other hand contains one of the five poorest districts in the US and has relatively high crime rates. We chose Brooklyn as a third borough because it seems like the in between category. Lively area’s with nice living areas. 

The file we found focuses on 6 felonies:<br> 
- rape <br>
- burglary<br>
- robbery<br>
- grand larceny of motor vehicle<br>
- felony assault<br>
- murder <br>
 
Our hypothesis that more serious felonies such as murder and rape happen more often in the Bronx while petty felonies as robbery happen more often in Manhattan where tourist are an easy target. Brooklyn is probably in between those borough in these matters. 

<br>
## The contents of the source data
<br>
Our source data contains, as stated before, the information of 6 different felonies in five different boroughs in New York City District.  



## Stap 1 opzet - Data collecting

- download the file from the page as .csv file 
- open the file in excel and indicate that every comma need to be a new collom
- save the file and copy it
- make a .json file from the data (this is a handy web page for the translation: https://shancarter.github.io/mr-data-converter/)
- now you have a .json file but it is way to big to open it. So you need to contain the information you need. We choose for the tree boroughs. 
- open the terminal and type in (image): cat (the place where your .json file is restord) |grep "(the thing you want to filter out, like MANHATTAN)" >(newfilename).json 
- so now the terminal made a new file where only manhattan is part of it. And you have your new, smaller file. 
- We greped the files on fellony because we wanted te files to be smaller. 

![NewYorkCityCrimes](Stap_1_Opzet/Analyzing_data/terminal.png)


## Stap 1 opzet - first iteration

- We now knew what data we wanted to work with.
- The next step was to visualise how we wanted the posters to look. 
- we made a sketch in illustrator.

![NewYorkCityCrimes](Stap_1_Opzet/Schetsen/poster1.png)
![NewYorkCityCrimes](Stap_1_Opzet/Schetsen/poster2.png)
![NewYorkCityCrimes](Stap_1_Opzet/Schetsen/poster3.png)

##Stap 2 plotdevice- data analysis

- Using plot device, we started analysing the data we had collected.
The first element we analysed was the which crimes had happened in the boroughs. In our code we let the json files be filtered on crime, so the the amount of crimes were counted one by one.
- As outcome we got the list of crimes with the amount of occurrences. 
- Our main question then became: What crime happens most often at which hour? 
- We grepped our json files again: this time to seperate the crimes. We ended up with 6 different files with the date of the different crimes.
- Now we changed the analysis file: we filtered on the hour, so our end result was the list of hours (from 0 till 23) with the corresponding amount. 
- Now we had exactly the data we needed. 

##Stap 3 Illustrator- drawing circle graphs

- With the relevant data we started sketching with the help of the example of the visualising the long tail.
- In Plotdevice we used the same code as we had used to the analysis; only now we added the part of code that visualised this data. 
- The first part of the code consisted of the analysis, of which the results are printed in the box below
- The second part draws the bargraph 
- The third part draws the horizontal lines which indicate the amount of crimes, every bar stands for 50 crimes 
-After some difficulty we manages to add the hours underneath the bar graph. <br>
[analysis file](Stap_2_Plotdevice/manhattan/MANHATTAN-ASSAULT.pv)

![NewYorkCityCrimes](Stap_2_Plotdevice/brooklyn/brooklyn_fellonyassault.png)

![NewYorkCityCrimes](Stap_2_Plotdevice/brooklyn/brooklyn_bulglary_2.png)

 


##Stap 4 Eindresultaat - Final Posters


We found a example of a code that would work better for our idea. 

-next step illustrator codering
for this you need:
- illustrator (adobe)
- extended tool kid (adobe)

in the file: Stap 3 illustrator are all the files you need

1. We worked with a illustrator file that has 24 hours in a clock. 
2. From there on you need to use the code that is final_code_jsx
3. you load the json file into the final_code_jsx than save it.
4. go to the shapeToModify24.ai file open it in illustror
5. then under fil you click stripting and click on final_code_jsx
6. now the code that is linked to one crime date will be seen in the illustrator file
7. continue with all the six crimes.




These are examples of how the illustrator file should look like:


![NewYorkCityCrimes](Stap_3_illustrator/Bronx/circle_graphs-01.png)
![NewYorkCityCrimes](Stap_3_illustrator/Bronx/circle_graphs-02.png)
![NewYorkCityCrimes](Stap_3_illustrator/Bronx/circle_graphs-03.png)
![NewYorkCityCrimes](Stap_3_illustrator/Bronx/circle_graphs-04.png)
![NewYorkCityCrimes](Stap_3_illustrator/Bronx/circle_graphs-05.png)

![NewYorkCityCrimes](Stap_4_eindresultaat/Bronx/4_logaritmisch.png)






## Collaborators

- Isabel Zoetbrood
- Lola Beumer
- Nikki Gersen


##License (MIT License)

Apeace Leaflet is released under the MIT license.

Copyright © 2016 GDA Artez Lola Beumer, Nikki Gersen, Isabel zoetbrood.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
<br><br><br>