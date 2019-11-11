# -*- coding: utf-8 -*-
import scrapy


class YoudaoSpider(scrapy.Spider):
    name = 'youdao'
    allowed_domains = ['fanyi.youdao.com/']
    start_urls = ['http://fanyi.youdao.com//']

    scrapy.Request()
    def parse(self, response):
        pass
