from itemadapter import ItemAdapter
import psycopg2
from datetime import datetime
from .settings import DB_HOST_NAME, DB_NAME, DB_USER_NAME, DB_PASSWORD, DB_PORT

class NewscrawlPipeline:
    def __init__(self):
        
        self.conn = psycopg2.connect(
            host=DB_HOST_NAME,
            dbname=DB_NAME,
            user=DB_USER_NAME,
            password=DB_PASSWORD,            
            port=DB_PORT
            )
        self.curr = self.conn.cursor()
        self.curr.execute("""CREATE TABLE IF NOT EXISTS news_data_tb(                        
                        
                        news_ranking text,
                        news_title text,
                        news_date date,
                        news_url text
                                
                        )""")
           
    def process_item(self, item, spider):
        item['news_date'] = datetime.today()
        
        for i in range(len(item['news_title'])):
            self.curr.execute("""insert into news_data_tb values(%s, %s, %s, %s)""",(
                
                item['news_ranking'][i],
                item['news_title'][i],
                item['news_date'],
                item['news_url'][i],
        ))
            self.conn.commit()
        
        return item  

    def close_spider(self, spider):
    
        self.curr.close()
        self.conn.close()