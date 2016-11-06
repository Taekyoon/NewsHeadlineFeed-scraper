import scrapy

from rssnews.items import NytnewslinkItem


class NytRSSSpider(scrapy.Spider):
    name = "nytrss"
    start_urls = [
        'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
    ]

    def parse(self, response):
        for rss_item in response.xpath('//item'):
            item = NytnewslinkItem()

            item['company'] = 'nyt_rss'
            item['title'] = rss_item.xpath('title/text()').extract()
            item['description'] = rss_item.xpath('description/text()').extract()
            item['link'] = rss_item.xpath('link/text()').extract()
            item['pubDate'] = rss_item.xpath('pubDate/text()').extract()
            if rss_item.xpath('guid/@isPermaLink').extract()[0] == 'true':
                item['guid'] = rss_item.xpath('guid/text()').extract()

            yield item
