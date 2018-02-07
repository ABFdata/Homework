import time
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    excutable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', headless=False)
    # return Browser("chrome", headless=False)


def scrape():
    browser = init_browser()
    # create mars_data dict that we can insert into mongo
    mars_data = {}

    # visit mars site
    mars_site = "https://mars.nasa.gov/news/"
    browser.visit(mars_site)

    # Retrieve page with the requests module\n",
    response = requests.get(url)

    # Create BeautifulSoup object; parse with 'html.parser'\n",
    soup = BeautifulSoup(response.text, 'html.parser')

    # this script finds some of the titles of the articles
    results = soup.find_all(class_="content_title")

    # this prints the latest article title
    news_title = results[0].text.strip()
    # news_title

    # print the news_p headline
    article_teasers = soup.find_all('div', class_="rollover_description_inner")
    news_p = article_teasers[0].text.strip()
    # news_p

    # search for surfing
    # browser.fill("searchKeyword", "surfing") #

    # find button and click it to search
    # button = browser.find_by_name("button") #
    # button.click() #
    # time.sleep(2) #
    # html = browser.html #
    
    # create a soup object from the html
    # img_soup = BeautifulSoup(html, "html.parser") #
    # elem = img_soup.find(id="gridMulti") #
    # img_src = elem.find("img")["src"] #

    time.sleep(2)
    
    # add our src to surf data with a key of src
    # surf_data["src"] = img_src #

    # add our src to mars data with a key of src
    mars_data["src"] = img_src 
    
    # visit surfline to get weather report
    # weather = "http://www.surfline.com/surf-forecasts/southern-california/santa-barbara_2141" #
    # browser.visit(weather) #

    # visit nasa to get image 
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    # grab our new html from surfline
    # html = browser.html #

    # grab image from nasa
    browser.visit(image_url)

    # click on image link 
    browser.click_link_by_partial_text("FULL IMAGE")

    # soup.find_all searches for footer
    full_img = soup.find_all('footer')

    # index the first element of full_img and assign it to the variable full
    full = full_img[0]
    
    # finds the url to the full size image
    featured_image = full.a['data-fancybox-href']

    # concatenate main url w/ image url
    main_url = 'https://www.jpl.nasa.gov'
    featured_image_url = main_url + featured_image  
    
    # create soup object from html
    # forecast_soup = BeautifulSoup(html, "html.parser") # 
    # report = forecast_soup.find(class_="forecast-outlook") #
    # surf_report = report.find_all("p") #
    
    # add it to our surf data dict
    # surf_data["report"] = build_report(surf_report) #
    
    # return our surf data dict
    # return surf_data #


# helper function to build surf report
# def build_report(surf_report): #
#     final_report = "" #
#     for p in surf_report: #
#         final_report += " " + p.get_text() #
#         print(final_report) #
#     return final_report #
