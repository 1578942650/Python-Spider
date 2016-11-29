
"""
This program require two outside program:
	PhantomJS
	tesseract
"""
import sys

#image processing
import time
from urllib.request import urlretrieve
import subprocess

#selenium + phantomJS for javascript-loaded website
from selenium import webdriver

#dynamic assert page has been load or not
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
#simulate submit form
from selenium.webdriver.common.keys import Keys


class houseinfo:

	def __int__(self, price, address, house_type, date_sold, suburb, bed, bath, car_park):
		self.price  = price
		self.address = address
		self.house_type = house_type
		self.date_sold = date_sold
		self.bed = bed
		self.bath = bath
		self.car_park = car_park
		self.suburb = suburb

def Searchfor(location, mode = "sold"):
	elem = driver.find_element_by_name("where")
	elem.clear()  #to clear the remand field
	elem.send_keys(location)
	elem.send_keys(Keys.RETURN) #press enter to finish entering data
	
def fetchdata2():
	properties = driver.find_elements_by_class_name("property-card__content")
	properties_info = []

	global item
	for item in properties:
		#不懂为啥这里的property是蓝色的
		property = houseinfo()
		property.price = findprice() #加一个识别图像的
		property.address = findelement("property-card__street-address")
		property.house_type = findelement("property-card__property-type")
		property.date_sold = findelement("property-card__sold-date")
		property.suburb = findelement("property-card__suburb")
		property.bed = findelement("property-card__beds")
		property.bath = findelement("property-card__baths")
		property.car_park = findelement("property-card__cars")

		properties_info.append(property)

		print(property.address,
			property.suburb, 
			property.price, 
			property.house_type, 
			property.date_sold, 
			property.bed, 
			property.bath, 
			property.car_park)

	return properties_info
	
def findprice():
	value = item.find_element_by_class_name("property-price")

	if (value.text == "None") or (value.text == "") :
		#in the case this is a image
		#locate image
		image = value.find_element_by_class_name("property-price__image").get_attribute("src")

		#retrive to local and use TESSERACT to read it
		urlretrieve(image, "image.jpg")
		image_to_string = subprocess.Popen(["tesseract", "image.jpg", "image"],
                            		 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		image_to_string.wait()

		#read result and get rid of white space
		value= open("image.txt", "r").read().strip()

		#return the result
		return value

	else:
		#in the case this is a text
		return value.text

def findelement(classname):
	try:
		value = item.find_element_by_class_name(classname).text
	except NoSuchElementException:
		value = "Not Specific"
	return value

def getnextpage():

	driver.find_element_by_link_text("Next page").click()

	try:
		driver.find_element_by_class_name("tier-two")	#
		driver.close()
		sys.exit("this is the end")
	except NoSuchElementException:
		print(driver.current_url)
		



#Setup and load pages
driver = webdriver.PhantomJS(executable_path='C:/Users/Administrator/Desktop/Python-Spider/phantomjs-2.1.1-windows/bin/phantomjs')
driver.get("https://www.realestate.com.au/sold")

#search for ashburton and convert to BeautifulSoup
Searchfor("Ashburton")

#fetch data
while True:
	properties_info = fetchdata2()
	getnextpage()

#this is the end
driver.close()


