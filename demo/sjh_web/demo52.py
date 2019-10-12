# -*- encoding: utf-8 -*-
from urllib import request

# response=request.urlopen("http://www.baidu.com")
req = request.Request("http://www.baidu.com")
response = request.urlopen(req)
print(dir(type(response)))
print(response.geturl())  # http://www.baidu.com
print(response.info())
'''
Bdpagetype: 1
Bdqid: 0xc288e86f001c86cd
Cache-Control: private
Content-Type: text/html
Cxy_all: baidu+1f3ed468194724c05af152bb128a031f
Date: Fri, 11 Oct 2019 01:09:51 GMT
Expires: Fri, 11 Oct 2019 01:09:40 GMT
P3p: CP=" OTI DSP COR IVA OUR IND COM "
Server: BWS/1.1
Set-Cookie: BAIDUID=26A9A53A1837059BDBF905DB3C54CDFC:FG=1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
Set-Cookie: BIDUPSID=26A9A53A1837059BDBF905DB3C54CDFC; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
Set-Cookie: PSTM=1570756191; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
Set-Cookie: delPer=0; path=/; domain=.baidu.com
Set-Cookie: BDSVRTM=0; path=/
Set-Cookie: BD_HOME=0; path=/
Set-Cookie: H_PS_PSSID=1427_21126_29721_29567_29220_26350; path=/; domain=.baidu.com
Vary: Accept-Encoding
X-Ua-Compatible: IE=Edge,chrome=1
Connection: close
Transfer-Encoding: chunked
'''
print(response.getcode())  # 200
html = response.read()
html = html.decode("utf-8")
print(html)
