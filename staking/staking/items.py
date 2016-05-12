# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StakingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()
    title = scrapy.Field()
    total_buyin = scrapy.Field()
    percent_for_sale = scrapy.Field()
    coef = scrapy.Field()
    min_share = scrapy.Field()
    booking_ending = scrapy.Field()
    special_cond = scrapy.Field()
    result = scrapy.Field()
    deal_status = scrapy.Field()
