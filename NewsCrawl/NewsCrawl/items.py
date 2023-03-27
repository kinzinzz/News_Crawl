# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewscrawlItem(scrapy.Item):
    # define the fields for your item here like:
    news_ranking = scrapy.Field()
    news_title = scrapy.Field()    
    news_date = scrapy.Field()
    news_url = scrapy.Field()
    
