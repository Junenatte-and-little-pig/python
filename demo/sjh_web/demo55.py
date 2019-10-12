# -*- encoding: utf-8 -*-
import urllib3

pcUserAgent = {
    'IE-agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windwos NT 6.1; Trident/5.0;',
    'firefox-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
    'chrome-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
}
mobileUserAgent = {
    'Touch capable Windows 8 device': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; Touch)',
    'Kindle Fire': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-us; Silk/1.1.0-80) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16 Silk-Accelerated=true',
    'iPad': 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10',
    'Samsung Galaxy S3': 'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'BlackBerry': 'BlackBerry9700/5.0.0.862 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/331 UNTRUSTED/1.0 3gpp-gba',
    'iPhone': 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3',
    'UC standard': 'NOKIA5700/ UCWEB7.0.2.37/28/999'
}

http = urllib3.PoolManager()
r = http.request('GET', 'http://www.baidu.com/s', {'wd': 'hello'},
                 pcUserAgent['ff-agent'])  # 伪造头部信息欺骗服务器
print(r)  # <urllib3.response.HTTPResponse object at 0x000002A0FB49EE88>
print(r.status)  # 200
print(r.data.decode('utf-8'))
