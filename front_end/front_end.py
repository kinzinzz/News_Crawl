import pandas as pd
from sqlalchemy import create_engine
import streamlit as st
from datetime import datetime

# 오늘 날짜
today = datetime.today()
format = '%Y-%m-%d'
str_datetime = datetime.strftime(today,format)
# DB Load
engine = create_engine('postgresql://postgres:postgres@localhost:5432/news_data')
news_data = pd.read_sql_query(sql = f"select * from news_data_tb where news_date = '{str_datetime}'", con=engine, index_col=None) 
df = news_data[['news_date','news_title','news_url']]
df = df.rename({"news_date": "날짜", "news_title":"제목", "news_url":"링크"}, axis=1)

word_list = news_data['news_title'].str.replace(pat=r'[^\w]', repl=r' ', regex=True)
word_list = word_list.apply(lambda x: x.split(' '))
word_list = pd.Series(word_list.sum())

# 랜덤으로 뉴스 5개 선택
df = df.sample(n=5)
st.markdown(df.to_html(render_links=True), unsafe_allow_html=True)


# 타이틀
st.title(f"뉴스로 보는 {str_datetime} 키워드")
# 상위 5개 키워드
cnt = 1
keywords_list = list(word_list.value_counts()[0:6].to_dict().keys())
for key in keywords_list:
    if key != '':
        st.header(f"{cnt}. {key}")
        cnt += 1