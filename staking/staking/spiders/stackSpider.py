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
    start_urls = ['http://forum.gipsyteam.ru/backing/forum?fid=43&page='+str(i) for i in range(1,50)]#['http://forum.gipsyteam.ru/backing/forum?fid=43&page=22']
    
    def parse(self, response):
        for sel in response.xpath('//tr/td/h2/a'):
            item = StakingItem()
            item['link'] = [i.replace('first-unread', '') for i in sel.xpath('@href').extract()]
            item['title'] = sel.xpath('text()').extract()[0]
            stake_url = response.urljoin(item['link'][0])
            request = scrapy.Request(stake_url, callback=self.get_stake_data)
            request.meta['item'] = item
            yield request

    
    def get_stake_data(self, response):
        item = response.meta['item']
        data = response.xpath('//table[@class="saids_stats"]//tr//td[not(@class)]//text()').extract()
        item['total_buyin'] = data[0]
        item['percent_for_sale'] = data[1]
        item['coef'] = data[2]
        item['min_share'] = data[3]
        item['booking_ending'] = data[4]
        if len(data) > 5:   ##yeah, this is stupid
            item['special_cond'] = data[5] 
        else:
            item['special_cond'] = 'None'
        result = response.xpath('//div[@class="b_result"]//span//text()').extract()
        if len(result) > 0:
            item['result'] = result[0]
        status = response.xpath('//span[contains(@class, "b_status")]//text()').extract()
        if len(status) > 0:
            item['deal_status'] = status[0]
        yield item
