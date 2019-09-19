# -*- encoding: utf-8 -*-

name = "张三"
age = 18
QQ = 12398725367
address = "江苏南京"

split = "-"
splitNum = 20
print(split * splitNum)
print("name:{1}{0}age:{2}{0}QQ:{3}{0}address:{4}".format('\n', name, age, QQ, address))
print(split * splitNum)
print(split * splitNum)
print("name:%s\nage:%d\nQQ:%s\naddress:%s" % (name, age, QQ, address))
print(split * splitNum)
