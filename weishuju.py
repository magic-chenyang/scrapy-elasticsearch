# 随机字符串做伪数据,上传到elasticsearch中.

import json
import random
from elasticsearch import Elasticsearch
from datetime import datetime
a = '1234567890qwertyuioplkjhgfdsamnbvcxzQWERTYUIOPLKJHGFDSAZCXVBNM'
f = open("foo.json",'a')
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)
for i in range(20):
    t1 = []
    t2 = []
    for s in range(15):
        t1.append(random.choice(a))
    for b in range(60):
        t2.append(random.choice(a))
    tt = str(''.join(t1))   #去除t1中的逗号,使tt的内容变为字符串
    ss = str(''.join(t2))
    data = {}
    data['title'] = 'docker'
    data['data'] = ss + ' '+'compose' + ' '+ tt
    data['url'] = 'http://' + tt + 'docker' + '.com'
    data['descriptions'] = ss + ss + tt + ' '+'docker'
    data['text'] = ss + ' '+'compose' + ' '+ tt
    data['@timestamp'] = datetime.now()
    x = json.dumps(dict(data),ensure_ascii=False,cls=ComplexEncoder)
    f.write(x+ '\n')    #写入一个文件中,测试使用
f.close()
server = 'http://192.168.56.147:9200'
index_name = 'shuju-test'
type_name = 'test'

es = Elasticsearch([server])
es.index(index=index_name,doc_type=type_name,body=data)
es.indices.refresh(index=index_name)
