# keyword_crawling_api

## Description
네이버에서 view에서 특정 키워드를 가지고 크롤링한 데이터를 일, 주, 월, 연 랭킹을 구하는 API.
Python Web Framework인 Flask를 사용하여 구현하였습니다.

## Installation
기본적으로 Python3.8과 mysql8.0버전이 설치되어 있어야합니다.

아래 패키지를 설치해야합니다. 
```
pip install flask, requests, pandas, PyJWT, pyMySQL, bcrypt, lxml, schedule
```

## DataBase
DB schema는 아래와 같이 구성되어 있습니다.
```
keyword = id, name
ranking = id, keyword_id, count, rank, date
week_ranking = id, keyword_id, count, rank, date
```

## Examples
- Today data API (ranking 10위까지만 출력이 됩니다.)
```
http://localhost:5000/rank/today
{
  "data": [
    {
      "change": 0, 
      "count": 135, 
      "name": "캐주얼룩", 
      "rank": 1
    }, 
    {
      "change": 0, 
      "count": 94, 
      "name": "레이어드룩", 
      "rank": 2
    }, 
    
    .... 생략
    
    {
      "change": 3, 
      "count": 30, 
      "name": "시스루", 
      "rank": 9
    }, 
    {
      "change": 2, 
      "count": 30, 
      "name": "심플룩", 
      "rank": 10
    }
  ]
}
```
- 전체 Ranking data API(일일, 주, 월(주 단위로 4번), 연(주단위로 52번)
http://localhost:5000/rank/view
```
{
  "data": [
    {
      "today": [
        {
          "change": 0, 
          "count": 135, 
          "name": "캐주얼룩", 
          "rank": 1
        }, 
        {
          "change": 0, 
          "count": 94, 
          "name": "레이어드룩", 
          "rank": 2
        }, 
        {
          "change": 1, 
          "count": 83, 
          "name": "스트릿룩", 
          "rank": 3
        }, 
        
        .... 생략
        
      "week": [
        {
          "date": "2021-10-19 00:00:00", 
          "name": "캐주얼룩", 
          "rank": 1
        }, 
        {
          "date": "2021-10-19 00:00:00", 
          "name": "빈티지룩", 
          "rank": 2
        }, 
        {
          "date": "2021-10-19 00:00:00", 
          "name": "레이어드룩", 
          "rank": 3
        }, 
        {
          "date": "2021-10-19 00:00:00", 
          "name": "스트릿룩", 
          "rank": 4
        }, 
        
        ... 생략
     
     "month": [
        {
          "date": "2021-09-26 00:00:00", 
          "name": "캐주얼룩", 
          "rank": 1
        }, 
        {
          "date": "2021-09-26 00:00:00", 
          "name": "빈티지룩", 
          "rank": 2
        }, 
        {
          "date": "2021-09-26 00:00:00", 
          "name": "레이어드룩", 
          "rank": 3
        }, 
        {
          "date": "2021-09-26 00:00:00", 
          "name": "스트릿룩", 
          "rank": 4
        }, 
        
        ... 생략
        
      "year": [
        {
          "date": "2020-11-01 00:00:00", 
          "name": "캐주얼룩", 
          "rank": 1
        }, 
        {
          "date": "2020-11-01 00:00:00", 
          "name": "빈티지룩", 
          "rank": 2
        }, 
        {
          "date": "2020-11-01 00:00:00", 
          "name": "레이어드룩", 
          "rank": 3
        }, 
        {
          "date": "2020-11-01 00:00:00", 
          "name": "스트릿룩", 
          "rank": 4
        }, 
        
        ... 
```
