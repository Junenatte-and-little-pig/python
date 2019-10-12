# -*- coding: utf-8 -*-
import scrapy

from douban_top250.items import DoubanTop250Item


class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    url = 'https://movie.douban.com/top250'
    # allowed_domains = ['movie.douban.com/top250']
    # start_urls = ['https://movie.douban.com/top250/']
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
    }

    def start_requests(self):
        yield scrapy.Request(self.url, headers=self.headers)

    def parse(self, response):
        item = DoubanTop250Item()
        movies = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            ranking = movie.xpath('.//div[@class="pic"]/em/text()').extract()
            movie_name = movie.xpath(
                './/div[@class="hd"]/a/span[1]/text()').extract()
            score = movie.xpath(
                './/div[@class="star"]/span[@class="rating_num"]/text()').extract()
            score_num = movie.xpath('.//div[@class="star"]/span/text()').re(
                r'(\d+)人评价')
            quote = movie.xpath('.//p[@class="quote"]/span/text()').extract()
            if ranking:
                item['ranking'] = ranking[0]
            if movie_name:
                item['movie_name'] = movie_name[0]
            if score:
                item['score'] = score[0]
            if score_num:
                item['score_num'] = score_num[0]
            if quote:
                item['quote'] = quote[0]
            yield item
        next_page = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_page:
            next_url = self.url + next_page[0]
            yield scrapy.Request(next_url, headers=self.headers)
