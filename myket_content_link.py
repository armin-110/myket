from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import pandas as pd
import numpy as np
from bs2json import bs2json
import re
import json
import copy
from copy import deepcopy
import requests
from collections import OrderedDict
from iteration_utilities import unique_everseen
import time
import itertools


content_link_list=[]
class Getcontentlink():
    def __init__ (self,driver,page_link):
        self.driver=driver
        self.page_link=page_link
    def get_link(self):
        content_link_list.clear()
        # try:
        try:
            self.driver.get(self.page_link)
        except:
            try:
                time.sleep(3)
                self.driver.get(self.page_link)
            except:
                time.sleep(3)
                self.driver.get(self.page_link)

        converter = bs2json()
        self.driver.get(self.page_link)
        SCROLL_PAUSE_TIME = 4
        last_height = self.driver.execute_script("return document.documentElement.scrollHeight")
        start1=time.time()
        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.documentElement.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            scroll_time=time.time()-start1
            print(scroll_time)
            try:
                element = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'body > article > section > div.row.text-center.more-app > button')))
                element.click()
            except:
                pass
            
        try:
            fb= WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > article')))
        except:
            fb= WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH, '/html/body/article')))
        html=self.driver.execute_script("return arguments[0].outerHTML;",fb)
        html_soup=b(html,'html.parser')
        converter = bs2json()
       
        class_find=html_soup.findAll('a',{'class':"app-detail-link" })
        json_class_find = converter.convertAll(class_find)
        print(json_class_find[0]['attributes']['href'])
        print(len(json_class_find))
        if len(json_class_find)>0:
            for i in range(len(json_class_find)):
                content_link_list.append(json_class_find[i]['attributes']['href'])
        else:
            print('content link not found')        
        # # except:
        #     print('content link not found')