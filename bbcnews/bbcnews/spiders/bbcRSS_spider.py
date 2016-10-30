import scrapy

from bbcnews.items import BbcnewslinkItem

class bbcRSSSpider(scrapy.Spider):
    name = "bbcrss"
    start_urls = [
        'http://feeds.bbci.co.uk/news/rss.xml',
    ]

    def parse(self, response):
        for rss_item in response.xpath('//item'):
            item = BbcnewslinkItem()

            item['title'] = rss_item.xpath('title/text()').extract()
            item['description'] = rss_item.xpath('description/text()').extract()
            item['link'] = rss_item.xpath('link/text()').extract()
            item['pubDate'] = rss_item.xpath('pubDate/text()').extract()
            if rss_item.xpath('guid/@isPermaLink').extract() is 'true':
                item['guid'] =  rss_item.xpath('guid/text()').extract()
            else:
                item['guid'] = "None"

            yield item