import time
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import requests

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    excutable_path = {'executable_path': 'chromedriver'}
    return Browser("chrome", headless=False)


def scrape():
    browser = init_browser()
    
    # create mars_data dict that we can insert into mongo 
    mars_data = {}

    # visit mars site
    mars_site = "https://mars.nasa.gov/news/"
    # browser.visit(mars_site)

    # Retrieve page with the requests module\n",
    response = requests.get(mars_site)

    # Create BeautifulSoup object; parse with 'html.parser'\n",
    soup = BeautifulSoup(response.text, 'html.parser')

    # this script finds some of the titles of the articles
    results = soup.find_all(class_="content_title")

    # this prints the latest article title
    news_title = results[0].text.strip()
    print(news_title)

    # print the news_p headline
    article_teasers = soup.find_all('div', class_="rollover_description_inner")
    news_p = article_teasers[0].text.strip()
    print(news_p)

    # time.sleep(2)
    
    # add our src to surf data with a key of src
    # surf_data["src"] = img_src #

    # add our src to mars data with a key of src
    # mars_data["src"] = img_src 
    ### ^^^ img src is not defined
    
    # visit nasa to get image 
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    # grab image from nasa
    browser.visit(image_url)

    # grab our new html from jpl nasa.gov
    html = browser.html

    # create a new soup object
    soup_image = BeautifulSoup(html, 'html.parser')

    # click on image link 
    browser.click_link_by_partial_text("FULL IMAGE")

    # soup.find_all searches for footer
    full_img = soup_image.find_all('footer')

    # index the first element of full_img and assign it to the variable full
    full = full_img[0]
    
    # finds the url to the full size image
    featured_image = full.a['data-fancybox-href']

    # concatenate main url w/ image url
    main_url = 'https://www.jpl.nasa.gov'
    featured_image_url = main_url + featured_image  
    print(featured_image_url)

    # mars facts
    facts_url = "https://space-facts.com/mars/"

    # Retrieve page with the requests module
    response2 = requests.get(facts_url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup_facts = BeautifulSoup(response2.text, 'html.parser')

    # read_html in pandas automatically scrapes any tabular data
    tables = pd.read_html(facts_url)
    
    # read table in pandas
    initial_df = tables[0]
    initial_df.columns = ['description', 'value']
    df = initial_df.set_index('description')
    print(df)

    # mars_weather
    # tweepy dependencies
    import json
    import tweepy

    # twitter api
    consumer_key = "Oe5kkX8IMqhbKyTP9jYqBo1fh"
    consumer_secret = "2uRriHsWqhb12BJXIpvgKIm0Fp7YyF4oXd9Clc0MiS35Udxpx4"
    access_token = "878718601250746368-hYV10B9TwbwFmzHq535sQkAcHSuD3WW"
    access_token_secret = "PXzLIgPxF8ykJNFqaO6y7VhjSnDy1mdwrC2Z3bzeVtEZi"

    # Setup Tweepy API Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # set target user to scrape mars weather twitter
    target_user = ("@MarsWxReport")

    # create empty list to store weather report after scraping
    mars_list = []

    # use API.user_timeline
    # returns the 20 most recent statuses posted 
    public_tweets = api.user_timeline(target_user)

    # loop through all tweets
    for tweet in public_tweets:
        # Print Tweet
        print(tweet["text"])
        
        # store tweet in mars_weather
        mars_list.append(tweet["text"])
    
    print('----------')

    # latest weather report 
    mars_weather = mars_list[1]
    print(mars_weather)

    # mars_hemispheres

    # url of page to be scraped
    hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    # uses selenium to navigate website
    browser.visit(hemi_url)

    # Retrieve page with the requests module
    response3 = requests.get(hemi_url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup_hemi = BeautifulSoup(response3.text, 'html.parser')

    # filter results by div tag and item class
    results_hemi = soup_hemi.find_all('div', class_="item")

    # create a func to pass through hemi_click in loop instead of all the code
    # below it
    def hemi_click (title):
        browser.click_link_by_partial_text('Enhanced')
        browser.click_link_by_text('Sample')
        link = result.a['href']
    
        print(title)
        print(link)
    
    for result in results_hemi:
        
        title = result.find('h3').text
    
        if title == "Cerberus Hemisphere Enhanced":
            hemi_click(title)
            img_url_0 = browser.windows[0].next.url
            print(img_url_0)
            print('----------')
        
        elif title == "Schiaparelli Hemisphere Enhanced":
            hemi_click(title)
            img_url = browser.windows[1].next.url
            print(img_url)
            print('----------')
    
        elif title == "Syrtis Major Hemisphere Enhanced":
            hemi_click(title)
            img_url_2 = browser.windows[2].next.url
            print(img_url_2)
            print('----------')
    
        else:
            hemi_click(title) 
            img_url_3 = browser.windows[3].next.url
            print(img_url_3)
            print('----------')

    # create empty list and append hemispheres to all hemi
    all_hemi = []
    for result in results_hemi:
        t = result.find('h3').text
        all_hemi.append(t)
    print(all_hemi)

    # Cerberus
    cerberus = all_hemi[0].rsplit(' ',1)[0]
    print(cerberus)

    # Schiaparelli
    schiaparelli = all_hemi[1].rsplit(' ',1)[0]
    print(schiaparelli)

    # Syrtis
    syrtis = all_hemi[2].rsplit(' ',1)[0]
    print(syrtis)

    # Valles
    valles = all_hemi[3].rsplit(' ',1)[0]
    print(valles)

    img_url_1 = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'

    # print image links
    print(img_url_0)
    print(img_url_1)
    print(img_url_2)
    print(img_url_3)

    # create dictionary for all_hemi titles
    cerberus_dict = {'title': cerberus, 'img_url': img_url_0}
    print(cerberus_dict)

    schiaparelli_dict = {'title': schiaparelli,'img_url': img_url_1}
    print(schiaparelli_dict)

    syrtis_dict = {'title': syrtis,'img_url': img_url_2}
    print(syrtis_dict)

    valles_dict = {'title': valles,'img_url': img_url_3}
    print(valles_dict)

    print('----------')

    hemisphere_image_urls = [cerberus_dict, schiaparelli_dict, syrtis_dict, valles_dict]
    print(hemisphere_image_urls)

    # build / store data that was scraped

    # the following objects need to be displayed
        # news_title
        # news_p
        # featured_image_url
        # mars_weather
        # df
        # hemisphere_image_urls

    # adding objects into mars_data{}
    mars_data['news_title'] = news_title
    mars_data['news_p'] = news_p
    mars_data['featured_image_url'] = featured_image_url
    mars_data['mars_weather'] = mars_weather
    mars_data['df'] = df
    mars_data['hemisphere_image_urls'] = hemisphere_image_urls

    # not sure if i need this, but copied from scrape surf
    # mars_data['report'] = build_report(mars_report)

    # return mars_data dict
    return mars_data

# helper function to build mars report
# def build_report(mars_report): 
#     final_report = "" 
#     for p in mars_report: 
#         final_report += " " + p.get_text()
#         print(final_report) #
#     return final_report #
