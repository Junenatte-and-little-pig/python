# -*- coding: utf-8 -*-
import scrapy


class SpiderDemoSpider(scrapy.Spider):
    name = 'spider_demo'
    allowed_domains = ['https://woodenrobot.me/']
    start_urls = ['https://woodenrobot.me/']

    def parse(self, response):
        # print(response.text)
        # a=response.xpath('//a[@class="post-title-link"]/text()')  # list consists of <Seletor xpath='//a[@class="post-title-link"]/text()' data=>
        a = response.xpath(
            '//a[@class="post-title-link"]/text()').extract()  # 将数据提取出来
        print(a)
