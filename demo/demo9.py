# -*- encoding: utf-8 -*-

import random

# 列表推导式
list1 = [random.randint(1, 101) for x in range(20)]
print(list1)
list2 = [x for x in list1]
print(list2)
list3 = [x for x in list2 if x <= 50]
print(list3)
set = {x for x in list1}
print(set)
dict = {x: x * x for x in list3}
print(dict)
print(dict.items())
print(sorted(dict.items(),key=lambda item:item[0])) # 按key排序
print(sorted(dict.items(),key=lambda item:item[1])) # 按value排序

