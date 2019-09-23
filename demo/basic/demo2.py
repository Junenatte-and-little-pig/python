# -*- encoding: utf-8 -*-

name = input("请输入你的名字：")
age = input("请输入你的年龄：")
if age.isdigit():
    age = int(age)
    if 0 <= age <= 150:
        print("name:{1}{0}age:{2}{0}".format('\n', name, age))
    else:
        print("请输入正确的数据")
else:
    print("请输入正确的数据")
