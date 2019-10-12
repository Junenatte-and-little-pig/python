# -*- encoding: utf-8 -*-

name = "女子高中生的虚度日常"
for x in name:
    print(x, end=",")  # 女,子,高,中,生,的,虚,度,日,常,
print()
print(name[2:5])  # 高中生
print(name[2:7:2])  # 高生虚
print(name[2:])  # 高中生的虚度日常
print(name[2::2])  # 高生虚日
print(name[:7])  # 女子高中生的虚
print(name[:7:2])  # 女高生虚
print(name[::])  # 女子高中生的虚度日常
print(name[::2])  # 女高生虚日
print(name[::-1])  # 常日度虚的生中高子女
print(name[::-2])  # 常度的中子
print(name[7:2:-2])  # 度的中
print(name[7::-2])  # 度的中子
print(name[:7:-2])  # 常
print(name[7:2])  #

name = "hello world"
# 可指定start end
print(name.find("o"))
print(name.rfind("o"))
print(name.index("o"))
print(name.rindex("o"))
print(name.count("o"))
# 可指定次数
print(name.replace("o", "e"))
# 分割字符串为前后 返回列表 输出为方括号 可指定次数
print(name.split("e"))
print(name.split())  # 无参以空格分割
# 大小写
print(name.capitalize())
print(name.title())
print(name.istitle())
print(name.lower())
print(name.upper())
# 字符串检查 可指定start end
print(name.startswith("h"))
print(name.endswith("d"))
print(name.isalpha())
print(name.isdigit())
print(name.isalnum())
print(name.isspace())
# 输出填充
print(name.ljust(20))
print(name.ljust(20, "*"))
print(name.rjust(20))
print(name.rjust(20, "-"))
print(name.center(20))
print(name.center(20, "+"))
# 删除空白字符
print("hello     ".rstrip())
print("hello*****".rstrip("*"))
print("     world".lstrip())
print("*****world".lstrip("*"))
# 分割字符串为前中后 返回元组 输出为小括号
print(name.partition("o"))
print(name.rpartition("o"))
# 分割行
print("hello\nworld".splitlines())
# 合并
print(".".join(["com", "junenatte", "python"]))
