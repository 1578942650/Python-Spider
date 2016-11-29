import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


#new toy
from seleium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.PhantomJS(executable_path='C:/Users/Administrator/Desktop/Python-Spider/phantomjs-2.1.1-windows/bin/phantomjs')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")

#use Selenium to analyze
#wait for response
#time.sleep(3) (stupid way)
#new way below
try:
    element = WebDriverWait(driver, 10).until(
                       EC.presence_of_element_located((By.ID, "loadedButton")))
finally:
    print(driver.find_element_by_id("content").text)


print("\n-----this is when we use BeautifulSoup-----\n")

#if we want to use Beautiful Soup to find
pageSource = driver.page_source
bsObj = BeautifulSoup(pageSource, "html.parser")
print(bsObj.find(id="content").get_text())

driver.close()