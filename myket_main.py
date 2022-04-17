print('بسمه الله الرحمن الرحیم')
print('salam bar mohammadreza dehghan amiri')
import copy
import datetime
import itertools
import json
import re
import time
from collections import OrderedDict
from copy import deepcopy
from curses import COLOR_BLACK

import numpy as np
import pandas as pd
import requests
import schedule
from bs2json import bs2json
from bs4 import BeautifulSoup as b
from iteration_utilities import unique_everseen
from rich import print
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from sqlalchemy import create_engine

import myket_categori_name
import myket_content_link
import myket_get_more_links
import myket_meta


def get_cat_link_name(page_link):
    s = requests.session()
    sg = myket_categori_name.GETCATEGORI(page_link,s)
    sgg = sg.get_cat_link_name()
    return(myket_categori_name.cat_link_name_list)


def get_more_link(page_link):
    s = requests.session()
    sg = myket_get_more_links.GETMORELINK(page_link,s)
    sgg = sg.get_link()
    return(myket_get_more_links.more_link_list)


def get_total_links(page_link):
    driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
    gf = myket_content_link.Getcontentlink(driver, page_link)
    gf.get_link()
    driver.close()
    return (myket_content_link.content_link_list)

def get_metadata(content_link):
    s = requests.session()
    sg = myket_meta.GETMETA(content_link,s)
    sgg = sg.get_meta()
    return(myket_meta.meta_data_list)
##############################################################    
engine = create_engine('postgresql://postgres:12344321@10.32.141.17/Myket',pool_size=20, max_overflow=100,)
con=engine.connect()
############################################################

# print(cat_game_link)
# print(cat_game_name)
############################################
# more_link=get_more_link('https://myket.ir/apps/persona lization')[0]
# print(more_link)
############################################
# content_link=get_total_links('https://myket.ir/list/best-new-word-games')
# print(content_link)
#########################################
# meta=get_metadata('https://myket.ir/app/com.dv.adm')
# print(meta)


date_a=datetime.datetime.now()
cat_program=get_cat_link_name('https://myket.ir/apps')
cat_program_link=cat_program[0]
cat_program_name=cat_program[1]
print(cat_program_link)
print(cat_program_name)
cat_game=get_cat_link_name('https://myket.ir/games')
cat_game_link=cat_game[0]
cat_game_name=cat_game[1]

for i in range(len(cat_program_link)):
    more_link=get_more_link(cat_program_link[i])[0]
    for j in range(len(more_link)):
        content_link=get_total_links(more_link[j])
        for k in range(len(content_link)):
            meta=get_metadata(content_link[k])
            date_i=datetime.datetime.now()
            meta[0]['crawling_date']=str(date_i.date()).replace('-','')+str(date_i.time()).split(':')[0]
            meta[0]['categori_name']=cat_program_name[i]
            meta[0]['cat']='program'
            data_frame =pd.DataFrame(meta[0],index=[0])
            data_frame.to_sql('myket_meta'+str(date_a.date()).replace('-','')+str(date_a.time()).split(':')[0],con,if_exists='append', index=False)
            print(meta[0])


for i in range(len(cat_game_link)):
    more_link=get_more_link(cat_game_link[i])[0]
    for j in range(len(more_link)):
        content_link=get_total_links(more_link[j])
        for k in range(len(content_link)):
            meta=get_metadata(content_link[k])
            date_i=datetime.datetime.now()
            meta[0]['crawling_date']=str(date_i.date()).replace('-','')+str(date_i.time()).split(':')[0]
            meta[0]['categori_name']=cat_program_name[i]
            meta[0]['cat']='game'
            data_frame =pd.DataFrame(meta[0],index=[0])
            data_frame.to_sql('myket_meta'+str(date_a.date()).replace('-','')+str(date_a.time()).split(':')[0],con,if_exists='append', index=False)
            print(meta[0])
