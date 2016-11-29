from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")	#create an object from class BesutifulSoup

nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
	print(name.get_text()) #get rid of tag list <span class = "green"> </spac>

print("\n-----------------This is no get_text() version-----------------------\n")

for name in nameList:
	print(name)


print("\n----------------find specific text----------------\n")
nameList = bsObj.findAll(text = "the prince")
print(len(nameList))
print(nameList)