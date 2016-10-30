# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BbcnewslinkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    link = scrapy.Field()
    guid = scrapy.Field()
    pubDate = scrapy.Field()
    media_src = scrapy.Field()
    pass
