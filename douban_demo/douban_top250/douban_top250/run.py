# -*- encoding: utf-8 -*-
from scrapy import cmdline
import os
name='douban_spider'
filename='../douban-top250.csv'
if os.path.exists(filename):
    os.remove(filename)
cmd='scrapy crawl {0} -o {1}'.format(name,filename)
cmdline.execute(cmd.split())