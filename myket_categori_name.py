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
cat_link_name_list=[]

class GETCATEGORI():
    def __init__ (self,page_link,s):
        self.page_link =page_link
        self.s=s
        ##################################################################################

    def get_cat_link_name(self):
        cat_link_name_list.clear()
        response = self.s.get(self.page_link, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"})
        page_html=response.text
        page_html_soup = b(page_html, 'html.parser')

        converter = bs2json()
        class_find_name= page_html_soup.findAll('a', {'class': 'category-item'}) 
        # class_find_name= page_html_soup.findAll('div', {'class': 'tab-pane fade in active show padding-top-20'}) 
        json_class_find_name = converter.convertAll(class_find_name)
        categori_link_list=[]
        categori_name_list=[]
        # # print('salam bar hossein')
        # print(json_class_find_name)
        # print(json_class_find_name[0]['attributes']['href'])
        # print(json_class_find_name[0]['attributes']['title'])
        # print(len(json_class_find_name))
 

        for i in range(len(json_class_find_name)):
            try:
                categori_link_list.append(json_class_find_name[i]['attributes']['href'])
                categori_name_list.append(json_class_find_name[i]['attributes']['title'])
            except:
                    pass
        cat_link_name_list.append(categori_link_list)
        cat_link_name_list.append(categori_name_list)