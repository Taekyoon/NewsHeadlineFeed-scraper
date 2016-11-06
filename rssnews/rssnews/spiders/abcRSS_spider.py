import scrapy

from rssnews.items import AbcnewslinkItem


class abcRSSSpider(scrapy.Spider):
    name = "abcrss"
    start_urls = [
        'http://feeds.abcnews.com/abcnews/topstories',
    ]

    def parse(self, response):
        for rss_item in response.xpath('//item'):
            item = AbcnewslinkItem()

            item['company'] = 'abc_rss'
            item['title'] = rss_item.xpath('title/text()').extract()
            item['description'] = rss_item.xpath('description/text()').extract()
            item['link'] = rss_item.xpath('link/text()').extract()
            item['pubDate'] = rss_item.xpath('pubDate/text()').extract()
            item['guid'] = rss_item.xpath('guid/text()').extract()

            yield item
