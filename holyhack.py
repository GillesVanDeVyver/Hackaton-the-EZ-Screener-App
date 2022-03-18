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
    list_of_links=[]

    for elem in links:
        if "https" in str(elem):
            elem.split(':h')
            list_of_links.append('h'+elem[1])

    return list_of_links

googlesearch("halff indeed")
