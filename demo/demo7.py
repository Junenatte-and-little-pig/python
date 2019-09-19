# -*- encoding: utf-8 -*-

nameDict = {'name': "张三", 'age': 18, 'address': '江苏南京'}
print(nameDict.get('name'))
print(nameDict.get('birthday'))
print(nameDict.get('birthday', "2000-01-01"))
print(nameDict.keys())
print(nameDict.values())
print(nameDict.items())

for k in nameDict:
    print("key=%s,\tvalue=%s" % (k, nameDict[k]), end="")
print()
for k in nameDict.keys():
    print("key=%s,\tvalue=%s" % (k, nameDict[k]), end="")
print()
for v in nameDict.values():
    print(v, end=" ")
print()
for k, v in nameDict.items():
    print("key=%s,\tvalue=%s" % (k, v), end="")
print()

nameDict.setdefault('birthday', "2000-01-01")
print(nameDict)
print(nameDict.pop('birthday'))
print(nameDict)
print(nameDict.popitem())
print(nameDict)
del nameDict['age']
print(nameDict)
