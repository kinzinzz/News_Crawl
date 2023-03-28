## 뉴스 크롤링

- 당일 네이버 신문사별 뉴스랭킹 1~5위 까지의 뉴스 크롤링
- 크롤링한 뉴스 제목에서 가장 많이 나온 단어 상위 5개 추출
- 개발 환경
  - os : ubuntu
- 프레임 워크
  - 크롤링 : scrapy
  - front-end: streamlit
  - scheduler : airflow
- workflow
  <img src="https://user-images.githubusercontent.com/107156650/228121747-1dc55848-1b7a-48ba-9e81-26ef7220a353.PNG">
  - airflow가 start_date 기준으로 자동으로 하루에 한번 크롤링 진행후 postgres DB에 저장
  - dags가 success 또는 fail 이면 email로 자동으로 alert
- front-end    
  <img src="https://user-images.githubusercontent.com/107156650/228020316-e4967f8a-6107-4386-9002-433f16df36eb.JPG">
  - 뉴스 제목의 특수문자 제거후 Serise로 변환
  - Series를 sum을 이용해 하나의 리스트로 만들고 count 이용해 가장 많은 단어 5개 추출
  - 크롤링한 뉴스들중 랜덤으로 5개만 front-end 나타냄