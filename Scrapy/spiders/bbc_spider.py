import scrapy
from Scrapy.items import NewsItem

class BBCSpider(scrapy.Spider):
    name = "bbc_spider" 
    allowed_domains = ["bbc.net"]  
    start_urls = []  
    
    custom_settings = {
        'FEEDS': {
            'bbc_arabic.json': {
                'format': 'json',
                'encoding': 'utf8',
                'overwrite': True,
            },
        }
    }
    def parse(self, response):
        articles = response.css(".gc__content")
        for article in articles:
            item = NewsItem()
            item["title"] = article.css("h3.gc__title a span::text").get()
            item["content"] =  article.css(".gc__excerpt p::text").get() 
            item["pub_date"] = article.css('.gc__date__date .date-simple span[aria-hidden="true"]::text').get()
            yield item