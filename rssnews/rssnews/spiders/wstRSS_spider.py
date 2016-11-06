import scrapy

from rssnews.items import WstnewslinkItem


class WstRSSSpider(scrapy.Spider):
    name = "wstrss"
    start_urls = [
        'http://www.washingtontimes.com/rss/headlines/news/',
    ]

    def parse(self, response):
        for rss_item in response.xpath('//item'):
            item = WstnewslinkItem()

            item['company'] = 'wst_rss'
            item['title'] = rss_item.xpath('title/text()').extract()
            item['description'] = rss_item.xpath('description/text()').extract()
            item['link'] = rss_item.xpath('link/text()').extract()
            item['pubDate'] = rss_item.xpath('pubDate/text()').extract()
            item['guid'] = rss_item.xpath('guid/text()').extract()

            yield item
