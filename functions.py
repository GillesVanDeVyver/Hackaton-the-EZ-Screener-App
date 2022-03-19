import logging

from bs4 import BeautifulSoup
from selenium import webdriver
import json
from time import sleep
from random import randrange
import pandas as pd
import urllib
import os
import json

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.extension_connection import LOGGER

from sentiment_analysis import getScore
import sys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options


def getReviews(companyName):
    # url="https://www.google.com/search?q={}%20indeed".format(urllib.parse.quote(companyName))
    # driver = webdriver.Safari()

    firefox_options = Options()
    pc_env = os.getenv('NODE_PC')
    if pc_env == 'stylify':
        print("running headless")
        firefox_options.add_argument("--headless")
    # firefox_options.add_argument("--disable-logging")
    # firefox_options.add_argument("--log-level=3")
    print("start loading indeed search")
    url = "https://www.indeed.com/companies/search?q={}&l=".format(companyName.replace(" ", "+"))
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)
    driver.get(url)
    # rnd=randrange(1,2)
    # sleep(rnd)

    driver.implicitly_wait(10)
    elem = driver.find_element(By.XPATH,
                               '/html/body/div[2]/main/div/div[2]/section/div[1]/div[1]/div[1]/div[2]/div[1]/a')
    part_link = elem.get_attribute('href')
    print('loading review page')
    driver.get('{}/reviews?fcountry=ALL'.format(part_link))
    page = driver.page_source

    soup = BeautifulSoup(page, "html.parser")
    soup.prettify()

    # links = []
    # for elem in soup.find_all("a"):
    #     links.append(elem.get("href"))
    # list_of_links=[]
    #
    # for elem in links:
    #     if "https" in str(elem):
    #         elem.split(':h')
    #         list_of_links.append('h'+elem[1])
    # print(list_of_links)

    # driver = webdriver.Safari()
    # driver.get(url)
    # rnd=randrange(1,2)
    # sleep(rnd)
    # page=driver.page_source

    soup = BeautifulSoup(page, "html.parser")
    soup.prettify()

    print('start parsing reviews')

    reviews = ""
    import re
    for elem in soup.find_all("span", attrs={'class': 'css-82l4gy eu4oa1w0'}):
        with open('review.txt', 'a+') as fp:
            # fp.write(str(elem))
            reviews += str(elem)
    # res = None
    # with open('review.txt', 'a+') as fp:
    #     line=fp.read()
    #     res = re.findall('<.*/>(.*?)</.*?>', line)
    #
    # with open('review.txt', 'a+') as fp:
    #     line = fp.read()
    #     res = re.findall('<.*?>([^(?!<br.*?/>)].*?)</.*?>', line)
    print(reviews)
    res = re.findall('<.*?>([^(?!<br.*?/>)].*?)</.*?>', reviews)
    print(res)
    driver.close()

    return res


def get_histogram(list):
    result = []
    for i in range(10):  # horrible inneficient way of counting the elements
        count = 0
        for elem in list:
            if elem == i:
                count += 1
        result.append(count)

    return result

def get_top_reviews(review_list,scores_list):
    result_pos = []
    result_neg=[]
    scores_sorted = scores_list.copy()
    scores_sorted.sort()
    for i in range(1,4):
        index = scores_list.index(scores_sorted[-i])
        result_pos.append(review_list[index])
    for i in range(3):
        index = scores_list.index(scores_sorted[i])
        result_neg.append(review_list[index])
    return result_pos,result_neg

def preprocess(review_list):
    for review in review_list:
        if review == "Nothing":
            review_list.remove(review)
    return  review_list


if __name__ == "__main__":
    review_list = getReviews(sys.argv[1])
    print(review_list)
    review_list = preprocess(review_list)
    print("after")
    print(review_list)

    word = None
    if len(sys.argv)>2:
        word = sys.argv[2]
    score,scores_list,new_scores_raw = getScore(review_list,word)
    hist_data = get_histogram(scores_list)

    print(hist_data)
    result_pos,result_neg = get_top_reviews(review_list,new_scores_raw)
    print(result_pos)
    print(result_neg)
    output = {'score_list': hist_data, 'score': score, 'result_pos' : result_pos, 'result_neg' : result_neg}
    print("JSON-DATA")
    print(json.dumps(output))
    # print("{ score: {}}".format(score))
