import csv
import scrapy
from scrapy.crawler import CrawlerProcess

class WallapopSpider(scrapy.Spider):
    name = "hacker news"

    def start_requests(self):
        url = 'https://es.wallapop.com/'
        return [scrapy.Request(url=url, callback=self.parse)]

    def parse(self, response):
        rows = []
        for row in response.css('.card-product-product-info'):
            title = row.css('.product-info-title::text').get().strip()
            price = row.css('.product-info-price::text').get().strip()

            rows.append({
                'title': title,
                'price': price
            })

        with open('data.csv', 'w') as csvfile:
            fieldnames = ['title', 'price']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in rows:
                writer.writerow(row)

process = CrawlerProcess()
process.crawl(WallapopSpider)
process.start()

