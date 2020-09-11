#import dependencies
import pandas as pd
import requests
import time
from splinter import Browser
from bs4 import BeautifulSoup

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    browser = init_browser()

##### NASA Scraping
    #Define url and browser
    nasa_url = "https://mars.nasa.gov/news/"
    browser.visit(nasa_url)

    #Time pause five seconds
    time.sleep(5)

    #Connect to soup
    nasa_html = browser.html
    news_soup = BeautifulSoup(nasa_html, "html.parser")

    #Collect the latest News Title and Paragraph Text
    article = news_soup.find("div", class_="list_text")
    news_title = article.find("div", class_="content_title").text
    news_p = article.find("div", class_="article_teaser_body").text

##### JPL Scraping
    #Define url and browser
    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_url)

    #Click "Full Image"
    browser.click_link_by_partial_text("FULL IMAGE")

    #Time pause five seconds
    time.sleep(5)

    #Click "more info"
    browser.click_link_by_partial_text("more info")
    #Time pause five seconds
    time.sleep(5)

    #Connect to soup browser
    jpl_html = browser.html
    jpl_soup = BeautifulSoup(jpl_html, "html.parser")

    #Collect Featured image
    img_url = jpl_soup.find("img", class_="main_image")["src"]
    featured_img = f"https://www.jpl.nasa.gov{img_url}"
    #Time pause five seconds
    time.sleep(5)

##### Mars Facts Scraping
    #Define url and browser
    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)

    #Connect to soup browser
    facts_html = browser.html
    facts_soup = BeautifulSoup(facts_html, 'html.parser')

    #Collect the table contents
    facts = pd.read_html(facts_url)


    mars_facts = facts[0]
    mars_facts.columns = ["Mars Planet Profile"," "]
    mars_facts

##### USGS Scraping
    #Define url and browser
    usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(usgs_url)

    usgs_base_url = "https://astrogeology.usgs.gov"

    #Connect to browser
    usgs_html = browser.html
    usgs1_soup = BeautifulSoup(usgs_html, "html.parser")

    #Navigate to the Cerberus Hemisphere img and title
    browser.click_link_by_partial_text("Cerberus Hemisphere Enhanced")

    #Time pause five seconds
    time.sleep(5)

    #browser.click_link_by_href("https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced")
    browser.click_link_by_partial_text("Open")

    #Time pause five seconds
    time.sleep(5)

    #Connect to soup browser
    usgs_html = browser.html
    usgs1_soup = BeautifulSoup(usgs_html, "html.parser")

    cerberus_src = usgs1_soup.body.find("img", class_ = "wide-image")["src"]

    #Time pause five seconds
    time.sleep(5)

    cerberus_url = usgs_base_url + cerberus_src
    print(cerberus_url)

    #Define url and browser
    usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(usgs_url)

    usgs_base_url = "https://astrogeology.usgs.gov"

    #Connect to soup browser
    usgs_html = browser.html
    usgs2_soup = BeautifulSoup(usgs_html, "html.parser")

    #Navigate to the Schiaparelli Hemisphere img and title
    browser.click_link_by_partial_text("Schiaparelli Hemisphere Enhanced")

    #Time pause five seconds
    time.sleep(5)

    #browser.click_link_by_href("https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced")
    browser.click_link_by_partial_text("Open")

    #Time pause five seconds
    time.sleep(5)

    schiaparelli_src = usgs2_soup.body.find("img", class_ = "wide-image")["src"]

    #Time pause five seconds
    time.sleep(5)

    schiaparelli_url = usgs_base_url + schiaparelli_src
    print(schiaparelli_url)

    #Define url and browser
    usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(usgs_url)

    usgs_base_url = "https://astrogeology.usgs.gov"

    #Connect to soup browser
    usgs_html = browser.html
    usgs3_soup = BeautifulSoup(usgs_html, "html.parser")

    #Navigate to the Syrtis Major Hemisphere img and title
    browser.click_link_by_partial_text("Syrtis Major Hemisphere Enhanced")

    #Time pause five seconds
    time.sleep(5)

    #browser.click_link_by_href("https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced")
    browser.click_link_by_partial_text("Open")

    #Time pause five seconds
    time.sleep(5)

    #Connect to soup browser
    usgs_html = browser.html
    usgs1_soup = BeautifulSoup(usgs_html, "html.parser")

    #Collect image and title
    syrtis_src = usgs1_soup.body.find("img", class_ = "wide-image")["src"]

    #Time pause five seconds
    time.sleep(5)

    syrtis_url = usgs_base_url + syrtis_src
    print(syrtis_url)

    #Define url and browser
    usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(usgs_url)

    usgs_base_url = "https://astrogeology.usgs.gov"

    #Connect to soup browser
    usgs_html = browser.html
    usgs4_soup = BeautifulSoup(usgs_html, "html.parser")

    #Navigate to the Valles Marineris Hemisphere img and title
    browser.click_link_by_partial_text("Valles Marineris Hemisphere Enhanced")

    #Time pause five seconds
    time.sleep(5)

    #browser.click_link_by_href("https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced")
    browser.click_link_by_partial_text("Open")

    #Time pause five seconds
    time.sleep(5)

    #Connect to soup browser
    usgs_html = browser.html
    usgs1_soup = BeautifulSoup(usgs_html, "html.parser")

    valles_src = usgs1_soup.body.find("img", class_ = "wide-image")["src"]

    #Time pause five seconds
    time.sleep(5)

    valles_url = usgs_base_url + valles_src
    print(valles_url)

    #Create dictionary list of for hemisphere image urls
    hemisphere_image_urls = [
        {"title": "Cerberus Hemisphere", "img_url": cerberus_url},
        {"title": "Schiaparelli Hemisphere", "img_url": schiaparelli_url},
        {"title": "Syrtis Major Hemisphere", "img_url": syrtis_url},
        {"title": "Valles Marineris Hemisphere", "img_url": valles_url},
    ]

    hemisphere_image_urls

     #Mars Data in Python Dictionary

    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_img": featured_img,
        "mars_facts": mars_facts,
        "hemisphere_image_urls": hemisphere_image_urls
    }

    # Close the browser after scraping
    browser.quit()

    #Return mars_data   
    return mars_data




