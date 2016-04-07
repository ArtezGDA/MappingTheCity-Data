from bs4 import BeautifulSoup
import urllib2
url = "https://www.wunderground.com/history/airport/KPHL/2016/1/1/MonthlyHistory.html?&reqdb.zip=&reqdb.magic=&reqdb.wmo=&MR=1"  #

page = urllib2.urlopen(url).read()
import urllib
urllib.urlopen("https://www.wunderground.com/history/airport/KPHL/2016/1/1/MonthlyHistory.html?&reqdb.zip=&reqdb.magic=&reqdb.wmo=&MR=1").read()

r = urllib.urlopen("https://www.wunderground.com/history/airport/KPHL/2016/1/1/MonthlyHistory.html?&reqdb.zip=&reqdb.magic=&reqdb.wmo=&MR=1").read()
BeautifulSoup(r)

soup = BeautifulSoup(r)
soup.findAll("table”)

table = soup.findAll(“table”)
new.table = soup.find_all("table", class_="responsive airport-history-summary-table")

Structure of Json file
[{“header”:
					{”fact 1”:”max”, “avg”, “min”, “sum”},
					{”fact 2”:”max”, “avg”, “min”, “sum”}
					{”fact 3”:”max”, “avg”, “min”, “sum”}}
]