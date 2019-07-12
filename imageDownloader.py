#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 17:18:23 2019

@author: federico
"""

from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"van gogh painting","limit":20,"print_urls":True, "size": "icon"}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths[0])  