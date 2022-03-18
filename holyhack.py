from bs4 import BeautifulSoup
from selenium import webdriver
import json
from time import sleep
from random import randrange
import pandas as pd

url='https://www.indeed.com/cmp/'+(input(x)+'/reviews'
driver = webdriver.Safari()
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

if 'https://www.indeed.com/cmp//reviews' in links:
    print('yes')