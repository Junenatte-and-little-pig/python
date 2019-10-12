# -*- encoding: utf-8 -*-
import requests

r1 = requests.get('https://www.baidu.com/s', {'wd': 'nba'})
# print(r1.text)

r2 = requests.post('https://www.baidu.com/s', json={'wd': 'nba'})
# print(r2.text)
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
}
r3 = requests.request('POST', 'https://www.baidu.com/s', headers=headers)
print(r3.encoding)  # ISO-8859-1
print(r3.apparent_encoding)  # utf-8
print(r3)  # <Response [200]>
print(r3.content.decode('utf-8'))
