import scrapy
from scrapy.crawler import CrawlerProcess

class HackerNewsSpider(scrapy.Spider):
    name = "hacker news"

    def start_requests(self):
        url = 'https://news.ycombinator.com'
        return [scrapy.Request(url=url, callback=self.parse)]

    def parse(self, response):
        for row in response.css('tr.athing'):
            title = row.css('a.storylink::text').get()
            website = row.css('span.sitebit a span::text').get()
            print({
                title: title,
                website: website
            })

process = CrawlerProcess()
process.crawl(HackerNewsSpider)
process.start()
