# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class RssnewslinkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    link = scrapy.Field()
    guid = scrapy.Field()
    pubDate = scrapy.Field()
    Read = scrapy.Field()
    pass

class BbcnewslinkItem(RssnewslinkItem):
    media_src = scrapy.Field()
    pass

class AbcnewslinkItem(RssnewslinkItem):
    pass

class NytnewslinkItem(RssnewslinkItem):
    pass

class LatnewslinkItem(RssnewslinkItem):
    pass

class TimenewslinkItem(RssnewslinkItem):
    pass

class WstnewslinkItem(RssnewslinkItem):
    pass
