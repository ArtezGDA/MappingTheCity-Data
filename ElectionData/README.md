# Election Data
Group:  Jesse, Kimberley, Patrick 


###Data sources step 1
1. **Genera:** 
	- http://thewebminer.com
	- https://datahub.io
	- https://www.quandl.com
	- http://www.kdnuggets.com/datasets/index.html
	- http://rs.io/100-interesting-data-sets-for-statistics/
	- http://blog.visual.ly/data-sources/
	- http://www.google.com/publicdata/directory
	- http://cjlab.stanford.edu/2015/09/30/lab-launch-and-data-sets/
	- http://kff.org/other/state-indicator/percent-who-had-all-teeth-extracted/#map
	- https://www.kaggle.com/rafadaguiar/d/kaggle/hillary-clinton-emails/email-network/code
1. **IQ:** 

	- https://iq-research.org/en/page/average-iq-by-country
	- http://www.statisticbrain.com/

1. **Election:** 
	- http://www.globalelectionsdatabase.com
	- http://www.nsd.uib.no/european_election_database/
	- http://www.eui.eu/Research/Library/ResearchGuides/Economics/Statistics/DataPortal/EED.aspx
	- http://www.idea.int/en/db/
	- http://www.presidency.ucsb.edu/elections.php
	- http://www.270towin.com/historical-presidential-elections/

1. **Final:** 
    - https://nl.wikipedia.org/wiki/Tweede_Kamerverkiezingen_ (2012, 2010..) .html
    - http://www.nlverkiezingen.com/TK(2012, 2010..) .html

## Source

As source for ElectionData-Scraper-NLVerkiezingen url:
- http://www.nlverkiezingen.com/TK (2012, 2010..)



As source for ElectionData-Scraper-Wikipedia Wikipedia was used.
- https://nl.wikipedia.org/wiki/Tweede_Kamerverkiezingen_ (2012, 2010..)  



```
from bs4 import BeautifulSoup
import urllib

    
r = urllib.urlopen("https://nl.wikipedia.org/wiki/Tweede_Kamerverkiezingen_2012").read()
soup = BeautifulSoup(r, "html.parser")
    
for item in soup.findAll("div", {"class": "thumb tright"}):
    tekst   =  item.findAll("div", {"class": "thumbcaption"}) [0].getText()
    lijstSP   =  item.findAll('p', {"style": "margin:0px;font-size:90%;"})[0].getText()
    SP      =  item.findAll('a', {"title": "Socialistische Partij (Nederland)"})[0].getText()
    
 
    print tekst
    print lijstSP
    
    print SP



```




```
Both of the url have a string which links to other years as well.
```


```
from bs4 import BeautifulSoup
import urllib

f = open('/Users/Kimberleyterheerdt/Desktop/ElectionDataScraper/output.txt','w')
errorFile = open('/Users/Kimberleyterheerdt/Desktop/ElectionDataScraper/errorfile.txt','w')

Jaargetal = str("2010")
r = urllib.urlopen("http://www.nlverkiezingen.com/TK" + Jaargetal +".html").read()

soup = BeautifulSoup(r, "html.parser")
table = soup.find_all("table")

for table in table:
            header = soup.find_all("h1")[0].getText()
            
            try:
                print header
                trs = table.find_all("tr")[0].getText()
                print '\n'
                for tr in table.find_all("tr"): 
                    print "|".join([x.get_text().replace('\n','') for x in tr.find_all('td')])
                print trs[1]
            
            except Exception as e: 
                errorFile.write (str(x) +'"""""""""' + str(e) + '"""""""""'+ str(col) + '\n')
                pass

f.close
errorFile.close


```
