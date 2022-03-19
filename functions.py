from bs4 import BeautifulSoup
from selenium import webdriver
import json
from time import sleep
from random import randrange
import pandas as pd
import urllib
from sentiment_analysis import getScore
import sys
from webdriver_manager.firefox import GeckoDriverManager

def getReviews(companyName):
    url="https://www.google.com/search?q={}%20indeed".format(urllib.parse.quote(companyName))
    #driver = webdriver.Safari()
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
    print(list_of_links)


    url="https://www.indeed.com/cmp/Halff-Associates,-Inc./reviews"
    #driver = webdriver.Safari()
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    driver.get(url)
        #rnd=randrange(1,2)
        #sleep(rnd)
    page=driver.page_source
    driver.close()

    soup = BeautifulSoup(page, "html.parser")
    soup.prettify()

    import re
    for elem in soup.find_all("span", attrs={'class': 'css-82l4gy eu4oa1w0'}):
            with open('review.txt', 'a+') as fp:
                fp.write(str(elem))

    with open('review.txt', 'a+') as fp:
        line=fp.read()
        res = re.findall('<.*/>(.*?)</.*?>', line)
    res = None
    with open('review.txt', 'r') as fp:
        line=fp.read()
        res = re.findall('<.*?>([^(?!<br.*?/>)].*?)</.*?>', line)

    return res


if __name__ == "__main__":
    review_list = getReviews(sys.argv[0])
    score,scores_list = getScore(review_list)
    print(score)
    print(scores_list)
    #print("{ score: {}}".format(score))