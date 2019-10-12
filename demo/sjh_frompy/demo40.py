# -*- encoding: utf-8 -*-
import re

print(dir(re))

pattern = "[a-zA-Z]+:[0-9]+"
str1 = "qwe:123"
str2 = "qwe:"
str3 = ":123"
str4 = "asd:456zxc:678"

p = re.compile(pattern)
# match 从起始位置进行匹配
# same as re.match(pattern, str1)
print(p.match(str1))  # <re.Match object; span=(0, 7), match='qwe:123'>
print(p.match(str2))  # None
print(p.match(str3))  # None
print(p.match(str4))  # <re.Match object; span=(0, 7), match='asd:456'>
# search 全文检索匹配
# same as re.search(pattern, str1)
print(p.search(str1))  # <re.Match object; span=(0, 7), match='qwe:123'>
print(p.search(str2))  # None
print(p.search(str3))  # None
print(p.search(str4))  # <re.Match object; span=(0, 7), match='asd:456'>
print(p.findall(str4))  # ['asd:456', 'zxc:678']
print(p.search(str4).span())  # (0, 7)
print(p.search(str4).start())  # 0
print(p.search(str4).end())  # 7
# substitute 对字符串中符合正则表达式的部分替换成需要的内容 或根据函数进行处理
print(re.sub('\d{3}', '123', '123456789'))  # 123123123


def add123(matched):
    str_int = matched.group(1)
    value = int(str_int)
    value += 12
    return str(value)


print(re.sub('(\d{3})', add123, '123456789'))  # 135468801
# n为替换次数
print(re.subn('\d{3}', '123', '123456789'))  # ('123123123', 3)
print(re.split(':', str4))  # ['asd', '456zxc', '678']
pattern = "(.\d+):(.\w+)"
str5 = ".123:.qwe"
p = re.compile(pattern)
print(p.match(str5))  # <re.Match object; span=(0, 9), match='.123:.qwe'>
# 在正则表达式中使用()进行分组 并通过group获取各个组的内容
print(p.match(str5).group())  # .123:.qwe
print(p.match(str5).group(0))  # .123:.qwe
print(p.match(str5).group(1))  # .123
print(p.match(str5).group(2))  # .qwe
