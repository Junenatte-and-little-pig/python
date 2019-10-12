# -*- encoding: utf-8 -*-
from urllib import request,parse
import json

# 表单数据
'''
i	asds
from	AUTO
to	AUTO
smartresult	dict
client	fanyideskweb
salt	15707574374967
sign	d4553d5b2b782dabe877a77ece2b684e
ts	1570757437496
bv	e2a78ed30c66e16a857c5b6486a1d326
doctype	json
version	2.1
keyfrom	fanyi.web
action	FY_BY_REALTlME
'''
# url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule" 不是有效的接口
url="http://fanyi.youdao.com/translate"  # 这个才是
form_data={}
form_data['i']='hello'
form_data['from']='AUTO'
form_data['to']='AUTO'
form_data['smartresult']='dict'
form_data['client']='fanyideskweb'
form_data['salt']=15707574374967
form_data['sign']='d4553d5b2b782dabe877a77ece2b684e'
form_data['ts']=1570757437496
form_data['bv']='e2a78ed30c66e16a857c5b6486a1d326'
form_data['doctype']='json'
form_data['version']='2.1'
form_data['keyfrom']='fanyi.web'
form_data['action']='FY_BY_REALTlME'
form_data=parse.urlencode(form_data).encode('utf-8')
response=request.urlopen(url,form_data)
html = response.read().decode('utf-8')
result = json.loads(html)
print(result)
print(result['translateResult'][0][0]['src'])
print(result['translateResult'][0][0]['tgt'])
