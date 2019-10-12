# -*- encoding: utf-8 -*-
import csv
from collections import namedtuple

with open('stocks.csv') as f:
    # 读取为可迭代对象 由列表组成
    f_csv = csv.reader(f)  # <_csv.reader object at 0x000001D865ECD668>
    # 第一行为列名
    headers = next(
        f_csv)  # ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
    # for r in f_csv:
    #     print(r)
    # 将列名生成类 实现成员方式访问 如row.Symbol
    Row = namedtuple('Row', headers)
    # print(type(Row))  # <class 'type'>
    for r in f_csv:
        row = Row(*r)
        print(row)
with open('stocks.csv') as f:
    # 读取为字典对象
    f_csv = csv.DictReader(f)
    for r in f_csv:
        print(r)  # <class 'collections.OrderedDict'>
