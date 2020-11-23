import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/',
        'http://quotes.toscrape.com/page/2/'
    ]

    def parse(self, response):
        for quote_div in response.xpath('//div[@class="quote"]'):
            yield {
                'quote': quote_div.xpath('.//span[@class="text"]/text()').get(),
                'author': quote_div.xpath('.//small[@class="author"]/text()').get()
            }
