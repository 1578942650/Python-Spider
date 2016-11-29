from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re


#selenium + phantomJS for javascript load website
from selenium import webdriver

#dynamic assert page has been load or not
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#this part help input the data and get a response from the website
params = {'SimpleSearchBody:SimpleSearchForm:keywords': 'comp'}

r = requests.post("https://handbook.unimelb.edu.au/faces/htdocs/user/search/SimpleSearch.jsp",
					data = params)

print(r.url)