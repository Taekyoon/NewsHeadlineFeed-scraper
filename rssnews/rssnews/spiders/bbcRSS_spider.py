import scrapy

from rssnews.items import BbcnewslinkItem


class bbcRSSSpider(scrapy.Spider):
    name = "bbcrss"
    start_urls = [
        'http://feeds.bbci.co.uk/news/rss.xml',
    ]

    def parse(self, response):
        for rss_item in response.xpath('//item'):
            item = BbcnewslinkItem()

            item['company'] = 'bbc_rss'
            item['title'] = rss_item.xpath('title/text()').extract()
            item['description'] = rss_item.xpath('description/text()').extract()
            item['link'] = rss_item.xpath('link/text()').extract()
            item['pubDate'] = rss_item.xpath('pubDate/text()').extract()
            if rss_item.xpath('guid/@isPermaLink').extract()[0] == 'true':
                item['guid'] = rss_item.xpath('guid/text()').extract()
                
            yield item
