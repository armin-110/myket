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
more_link_list=[]

class GETMORELINK():
    def __init__ (self,page_link,s):
        self.page_link =page_link
        self.s=s
        ##################################################################################

    def get_link(self):
        more_link_list.clear()
        response = self.s.get(self.page_link, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"})
        page_html=response.text
        page_html_soup = b(page_html, 'html.parser')

        converter = bs2json()
        class_find_name= page_html_soup.findAll('a', {'class': 'pull-left text-info btn-all-apps'})  
        json_class_find_name = converter.convertAll(class_find_name)
        
        print(json_class_find_name[0]['attributes']['href'])
        print(len(json_class_find_name))
        more_link=[]
        for i in range(len(json_class_find_name)):
            try:
                more_link.append(json_class_find_name[i]['attributes']['href'])

            except:
                    pass
        more_link_list.append(more_link)
        