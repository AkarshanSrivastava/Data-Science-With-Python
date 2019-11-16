################# IMDB reviews extraction ######################## Time Taking process as this program is going
# to operate the web page while extracting reviews 
############# time library in order to sleep and make it to extract for that specific page 
#### We need to install selenium for python
#### pip install selenium
#### time library to make the extraction process sleep for few seconds 
from selenium import webdriver
browser = webdriver.Chrome() # opens the chrome browser
from bs4 import BeautifulSoup as bs
#page = "http://www.imdb.com/title/tt0944947/reviews?ref_=tt_urv"
#page = "http://www.imdb.com/title/tt6294822/reviews?ref_=tt_urv" # required url page where the movie reviews are residing
#page = "http://www.imdb.com/title/tt2704998/reviews?ref_=tt_urv"
#page = "http://www.imdb.com/title/tt2873282/reviews?ref_=tt_urv"

## Moana Movie #####
page= "http://www.imdb.com/title/tt3521164/reviews?ref_=tt_urv"
# Importing few exceptions to surpass the error messages while extracting reviews 
from selenium.common.exceptions import NoSuchElementException 
from selenium.common.exceptions import ElementNotVisibleException

browser.get(page)
import time
reviews = []
i=1
# Below while loop is to load all the reviews into the browser till load more button dissapears
while (i>0):
    #i=i+25
    try:
        # Storing the load more button page xpath which we will be using it for click it through selenium 
        # for loading few more reviews
        button = browser.find_element_by_xpath('//*[@id="load-more-trigger"]') # //*[@id="load-more-trigger"]
        button.click()
        time.sleep(5)
    except NoSuchElementException:
        break
    except ElementNotVisibleException:
        break

# Getting the page source for the entire imdb after loading all the reviews
ps = browser.page_source 
#Converting page source into Beautiful soup object
soup=bs(ps,"html.parser")

#Extracting the reviews present in div html_tag having class containing "text" in its value
reviews = soup.findAll("div",attrs={"class","text"})
for i in range(len(reviews)):
    reviews[i] = reviews[i].text

##### If we want only few recent reviews you can either press ctrl+c to break the operation in middle but the it will store 
##### Whatever data it has extracted so far #######

# Creating a data frame 
import pandas as pd
movie_reviews = pd.DataFrame(columns = ["reviews"])
movie_reviews["reviews"] = reviews

movie_reviews.to_csv("movie_reviews.csv",encoding="utf-8")
