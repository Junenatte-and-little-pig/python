# -*- encoding: utf-8 -*-

try:
    name = input("请输入你的名字：")
    age = int(input("请输入你的年龄："))
except ValueError:
    print("请输入正确的数据")
else:
    if 0 <= age <= 150:
        print("name:{1}{0}age:{2}{0}".format('\n', name, age))
    else:
        print("请输入正确的数据")
