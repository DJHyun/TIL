import requests
import bs4
import json

url = "http://finance.daum.net/api/trend/market_capitalization?page=1&perPage=30&fieldName=marketCap&order=desc&market=KOSPI&pagination=true"

headers = {
    'Host': 'finance.daum.net',
    'Referer': 'http://finance.daum.net/domestic/market_cap?market=KOSPI',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
response = requests.get(url, headers=headers).text
document = json.loads(response)
data = document['data']

result = []
for i in data:
    data = {
        'name':i['name'],
        'tradePrice':i['tradePrice'],
        'changePrice':i['changePrice']
    }
    result.append(data)

for i in result:
    print('{} -- 현재가 : {} 전일비 : {}'.format(i['name'],i['tradePrice'],i['changePrice']))