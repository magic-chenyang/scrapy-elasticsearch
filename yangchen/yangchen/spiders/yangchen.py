#-*- coding: utf-8 -*-
import scrapy
import requests
from yangchen.items import YangchenItem
#from scrapy.spider import Spider

class YangchenSpider(scrapy.Spider):
        name = 'yangchen'
        #allow_domains = ['sina.com.cn']
        start_urls = ['http://47.52.73.177:8888/']

#        urls2 = ('http://www.jd.com',
#                'https://www.taobao.com',
#                'http://47.52.73.177:8888/',
#                'http://sina.com.cn',
#                'http://www.baidu.com',
#                )
#        def start_requests(self):
#                for url in self.urls2:
#                        yield self.make_requests_from_url(url)
        def parse(self,response):
                item = YangchenItem()
                item['urladdr'] = response.xpath("//p/text()").extract()
                item['urlname'] = response.xpath("//title/text()").extract()
                #print(item['urlname'])
                item['urllen'] = len(response.body)
                item['urlcr'] = str(len(requests.get(response.url).content))
                #print(item['urlcr'])
                return item
                print(item)

