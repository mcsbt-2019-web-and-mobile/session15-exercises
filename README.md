# 

## Session 15

# 

## Plan for today

* scraping
* explain individual assignment

#

## Scraping

Scraping is the process of extracting data from webpages
automatically.

## scrapy lib

in our examples we'll be using python's scrapy library:

`pip3 install scrapy`

## scrapy terminology

Scrapy uses the term `Spider` to refer to classes that know how to
scrap data from a particular webiste.

## Creating our first Spyder

``` python
import scrapy

class HackerNewsSpider(scrapy.Spider):
    name = "hacker news"

    def start_requests(self):
        url = 'https://news.ycombinator.com'
        return [scrapy.Request(url=url, callback=self.parse)]

    def parse(self, response):
		# in this method we do our magic
        pass
```

## Creating our first Spyder

the important bit in the last example is the `start_request` method.
That's the method that tells scrapy which URLs to crawl(**url=url**),
and how to handle the response (**callback=self.parse**).

## parsing the response

When a request is done in scrapy, the callback is executed, pasing the
response to it.  Once the callback is executed (the `parse` method in
our previous example), we can access information from the response
using different techniques.

- xpath
- css

## CSS selectors (remember CSS dinner?)

the following block is printing out the text inside all `a` tags with
the `link` class.

``` python
...
def parse(self, response):
	for link in response.css('a.link::text'):
		print(a.get())
...		
```


## Example1

See the `hackernews` folder for an example spider that gets the
frontpage of hackernews and just prints the outputs.

## more interesting stuff

What else could we do with scraping?  The normal approach for
scrapping applications is getting data from the web and storing it
somewhere for later use.  This somewhere may be a CSV file, database,
etc.

## saving data from a webpage to a CSV file

``` python
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
```

## Example2

See the `wallapop` folder for an example spider that gets the
frontpage of wallapop and stores the classified ads in a CSV file.

## running our spyders

There are two main ways of running our scrapy spyders:

- using the `scrapy` command line tool
- as normal python programs (using `python program.py`)

#

## Interlude:  Individual assignment 2

You're asked to create a service that allows users to keep track of
the analytics in their websites (think of Google Analytics).

All analytics must be stored in a SQLite database.

#

## Exercise

Create a scraper for fotocasa.com that gets the data first page and
then saves the data to a CSV file





