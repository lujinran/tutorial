# -*- coding: utf-8 -*-
import scrapy


class AbcSpider(scrapy.Spider):
    name = "abc"
    allowed_domains = ["www.baidu.com"]
    start_urls = (
        'http://www.www.baidu.com/',
    )

    def parse(self, response):
        pass
