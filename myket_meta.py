from curses import meta
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
meta_data_list=[]

class GETMETA():
    def __init__ (self,content_link,s):
        self.content_link =content_link
        self.s=s
        ##################################################################################

    def get_meta(self):
        meta_data_list.clear()
        meta_dic = {'cat':'','categori_name':'','content_name': '','content_link':self.content_link,'rate':'','ratings':'','Size':'','Download':'','Current Version':'','Last Update':'','Creator':'','crawling_date':''}
        # try:
        response = self.s.get(self.content_link, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"})
        page_html=response.text
        page_html_soup = b(page_html, 'html.parser')

        converter = bs2json()
        try:
            class_find_name= page_html_soup.findAll('h1', {'style': 'line-height:1.4;margin-bottom:10px;font-size:20px'}) 
            json_class_find_name = converter.convertAll(class_find_name)
            print(json_class_find_name)
            meta_dic['content_name']=json_class_find_name[0]['text']#title
        except:
            class_find_name= page_html_soup.findAll('h1', {'style': 'line-height: 1.4;margin-bottom: 10px;font-size: 20px;'})
            json_class_find_name = converter.convertAll(class_find_name)
            meta_dic['content_name']=json_class_find_name[0]['text']#title
        


        class_find_name= page_html_soup.findAll('div', {'class': 'tbl-app-detail'})  
        json_class_find_name = converter.convertAll(class_find_name)
        # print(json_class_find_name[0]['table']['tr'][0]['th']['text'])#tag
        # print(json_class_find_name[0]['table']['tr'])
        # print(len(json_class_find_name[0]['table']['tr']))
        for i in range(len(json_class_find_name[0]['table']['tr'])):
            if json_class_find_name[0]['table']['tr'][i]['th']['text']=='نسخه':
                meta_dic['Current Version']=json_class_find_name[0]['table']['tr'][i]['td']['text']
            if json_class_find_name[0]['table']['tr'][i]['th']['text']=='تعداد دانلود':
                meta_dic['Download']=json_class_find_name[0]['table']['tr'][i]['td']['text']  
            if json_class_find_name[0]['table']['tr'][i]['th']['text']=='امتیاز':
                meta_dic['rate']=json_class_find_name[0]['table']['tr'][i]['td']['text']       
            if json_class_find_name[0]['table']['tr'][i]['th']['text']=='تعداد نظرات':
                meta_dic['ratings']=json_class_find_name[0]['table']['tr'][i]['td']['text'] 
            if json_class_find_name[0]['table']['tr'][i]['th']['text']=='حجم':
                meta_dic['Size']=json_class_find_name[0]['table']['tr'][i]['td']['text'] 
            if json_class_find_name[0]['table']['tr'][i]['th']['text']=='آخرین بروزرسانی':
                meta_dic['Last Update']=json_class_find_name[0]['table']['tr'][i]['td']['text'] 
            if json_class_find_name[0]['table']['tr'][i]['th']['text']=='سازنده':
            #    print(json_class_find_name[0]['table']['tr'][i]['td']['a']['text']) 
               meta_dic['Creator']=json_class_find_name[0]['table']['tr'][i]['td']['a']['text']
            
        meta_data_list.append(meta_dic)

        # except:
        #     meta_data_list.append(meta_dic)
