# -*- coding: utf-8 -*-
"""
Created on Wed Mar 02 19:41:08 2016

@author: Nikolay
"""

import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
    "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
    "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
       ]
    
    def parse(self, response):
        filename = response.url.split('/')[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
            
        