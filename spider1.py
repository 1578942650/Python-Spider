from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:	#in case there is no such html
        return None
    try: 
        bsObj = BeautifulSoup(html.read(), "html.parser") #"html.parser" is html reader
        title = bsObj.body.h1
    except AttributeError as e:	#incase there is no such tag
        return None
    return title


title = getTitle("http://www.pythonscraping.com/pages/page1.html") #target page

if title == None:
	printf("No such url")
else:
	print(title) #extract a specific tag