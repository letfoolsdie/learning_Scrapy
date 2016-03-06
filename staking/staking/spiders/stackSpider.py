# -*- coding: utf-8 -*-
"""
Created on Sat Mar 05 21:56:03 2016

@author: Nikolay
"""

import scrapy
from staking.items import StakingItem

class StakingSpider(scrapy.Spider):
    name = "staking"
    allowed_domains = ["gipsyteam.ru"]
    start_urls = [
    "http://forum.gipsyteam.ru/backing/forum?fid=43"
       ]
    
    def parse(self, response):
        for sel in response.xpath('//tr/td/h2/a'):
            item = StakingItem()
            item['link'] = sel.xpath('@href').extract()
            item['title'] = sel.xpath('text()').extract()
            yield item
#            print title, link
            
        