from bs4 import BeautifulSoup
from selenium import webdriver
import json
from time import sleep
from random import randrange
import pandas as pd
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

def googlesearch(inputString):
    splittedInput = inputString.split( )
    url="https://www.google.com/search?q="
    for word in splittedInput:
        url = url + word + "%20"

    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get(url)
        #rnd=randrange(1,2)
        #sleep(rnd)
    page=driver.page_source
    driver.close()

    soup = BeautifulSoup(page, "html.parser")
    soup.prettify()


    links = []
    for elem in soup.find_all("a"):
        links.append(elem.get("href"))
    result = []
    for link in links:
        if link is not None and "review" in link:
            result.append(link)

    print(result)
    print(len(result))
    return result

def scrapsite(url):
    #driver = webdriver.Safari()
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get(url)
    # rnd=randrange(1,2)
    # sleep(rnd)
    page = driver.page_source
    driver.close()

    soup = BeautifulSoup(page, "html.parser")
    soup.prettify()

    for elem in soup.find_all("span", attrs={'class': 'css-82l4gy eu4oa1w0'}):
        with open('reviews.txt', 'a+') as fp:
            fp.write(str(elem))


googlesearch("halff indeed")
