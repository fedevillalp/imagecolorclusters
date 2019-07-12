#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: federico
"""
import time
import urllib
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen


base_url = 'https://www.vincent-van-gogh-gallery.org'
url = 'https://www.vincent-van-gogh-gallery.org/the-complete-works.html?pageno='
thumbnails =[]
complete_image_links =[]
soup = []
i=1
j=1
first_page = 1
last_page = 85


#-----------Scrape image links and return them in a list-------
def scrape_image_links(first_page,last_page, url):
    for j in range(first_page, last_page):
        print(url+str(j))
        print(j)
        html = urlopen(url + str(j))
        soup = BeautifulSoup(html)
        
        
        
        for res in soup.findAll('img'):
            if ('thumbnail' and 'mini_small') in res.get('src').split('/'):
                    print(res.get('src'))
                    complete_image_links.append(base_url + res.get('src'))
            
    return complete_image_links
#--------------------------------------------------------------
    
#-----------Download Image Files given an array of links-------
def download_images(complete_image_links,i):
    for link in complete_image_links:
        img_data = requests.get(link).content
        img_name = str(i) + '.jpg'
        print('this is img_name:', img_name)
        with open(img_name, 'wb') as handler:
            handler.write(img_data)
        i=i+1
#--------------------------------------------------------------

complete_image_links = scrape_image_links(first_page,last_page,url)

download_images(complete_image_links,i)
