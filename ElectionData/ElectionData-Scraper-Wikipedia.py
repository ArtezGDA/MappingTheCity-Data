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
