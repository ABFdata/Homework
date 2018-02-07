# import scraping dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

excutable_path = {'executable_path': 'chromedriver.exe'}

browser = Browser('chrome', headless=False)

# url of page to be scraped
url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

# uses selenium to navigate website
browser.visit(url)

# Retrieve page with the requests module
response = requests.get(url)

# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')

# filter results by div tag and item class
results = soup.find_all('div', class_="item")

# create empty list and append hemispheres to all hemi
all_hemi = []
for result in results:
    t = result.find('h3').text
    all_hemi.append(t)
all_hemi

# Cerberus
cerberus = all_hemi[0].rsplit(' ',1)[0]
cerberus

# Schiaparelli
schiaparelli = all_hemi[1].rsplit(' ',1)[0]
schiaparelli

# Syrtis
syrtis = all_hemi[2].rsplit(' ',1)[0]
syrtis

# Valles
valles = all_hemi[3].rsplit(' ',1)[0]
valles

# create dictionary for all_hemi titles
cerberus_dict = {'title': cerberus, 'img_url': ''}
cerberus_dict

schiaparelli_dict = {'title': schiaparelli,
                    'img_url': ''}
schiaparelli_dict

syrtis_dict = {'title': syrtis,
                    'img_url': ''}
syrtis_dict

valles_dict = {'title': valles,
                    'img_url': ''}
valles_dict

hemisphere_image_urls = [cerberus_dict, schiaparelli_dict, 
                 syrtis_dict, valles_dict]
hemisphere_image_urls

