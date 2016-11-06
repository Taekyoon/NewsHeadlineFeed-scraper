import scrapy

from rssnews.items import LatnewslinkItem


class LatRSSSpider(scrapy.Spider):
    name = "latrss"
    start_urls = [
        'http://www.latimes.com/rss2.0.xml',
    ]

    def parse(self, response):
        for rss_item in response.xpath('//item'):
            item = LatnewslinkItem()

            item['company'] = 'lat_rss'
            item['title'] = rss_item.xpath('title/text()').extract()
            item['description'] = rss_item.xpath('description/text()').extract()
            item['link'] = rss_item.xpath('link/text()').extract()
            item['pubDate'] = rss_item.xpath('pubDate/text()').extract()

            yield item
