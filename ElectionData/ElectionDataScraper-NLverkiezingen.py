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
