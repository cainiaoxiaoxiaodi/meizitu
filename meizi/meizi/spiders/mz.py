# -*- coding: utf-8 -*-
from pprint import pprint
from bs4 import BeautifulSoup

import scrapy


class MzSpider(scrapy.Spider):
    name = 'mz'
    allowed_domains = ['meizitu.com', 'mm.chinasareview.com']
    start_urls = ['http://www.meizitu.com/a/more_1.html']

    def parse(self, response):
        # 初始化bs4
        data = BeautifulSoup(response.text, 'lxml')
        # 取出每个带有套图页url的div标签
        div_list = data.select('ul > li.wp-item > div > div')
        for div in div_list:
            # 每个套图的url
            map_url = div.a['href']
            # 构造套图页请求
            return scrapy.Request(map_url, callback=self.get_img_url, dont_filter=True)

    def get_img_url(self, response):
        item = {}  # 构造字典
        data = BeautifulSoup(response.text, 'lxml')
        img_list = data.select('div > p > img')
        for img in img_list:
            img_url = img['src']
            print(img_url)
            break
