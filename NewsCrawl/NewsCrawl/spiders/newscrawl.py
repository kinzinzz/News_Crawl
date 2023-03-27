import scrapy
from ..items import NewscrawlItem
from scrapy.http import Request

class NewscrawlSpider(scrapy.Spider):
    name = "newscrawl"
    allowed_domains = ["news.naver.com"]
    start_urls = ["http://news.naver.com/"]

    start_urls = ["https://news.naver.com/main/ranking/popularDay.naver"]

    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    }
    def start_requests(self):
        
        yield Request(url="https://news.naver.com/main/ranking/popularDay.naver",
                      callback=self.parse,
                      headers=self.HEADERS 
                      )
    
    
    def parse(self, response):
        items = NewscrawlItem()
        
        # 크롤링
        
        news_ranking = response.css('.list_ranking_num::text').extract()
        news_title = response.css('div.list_content a::text').extract()
        news_url = response.css('div.list_content a::attr(href)').extract()
        
        items['news_ranking'] = news_ranking
        items['news_title'] = news_title
        items['news_url'] = news_url
        
        yield items
               
    