# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#import json

#import codecs
#class YangchenPipeline(object):
#    def __init__(self):
#        self.file = codecs.open("/root/yangchen/tezt.json","wb",encoding="utf-8")
#    def process_item(self, item, spider):
#        #name = item['urlname']
#        #body = item['urllen']
#        #kuan = item['urlcr']
#        #i = {"name":name,"body":body,"len2":kuan}        
#        data = json.dumps(dict(item),ensure_ascii=False) + "\n"
#        print(data)
#        self.file.write(data)
#        return item
#    def close_spider(self,spider):
#        self.file.close()


from elasticsearch import Elasticsearch
from scrapy.conf import settings
from datetime import datetime


class YangchenPipeline(object):
    def __init__(self):
        self.server = 'http://192.168.56.147:9200'
        self.index_name = 'scrapy-yangchen'
        self.type_name = 'item'
        self.es = Elasticsearch(['http://192.168.56.147:9200'])

    def process_item(self, item, spider):
        data = dict(item)
        data['@timestamp'] = datetime.now()
        self.es.index(index=self.index_name, doc_type=self.type_name, body=data)
        self.es.indices.refresh(index=self.index_name)
        return item
