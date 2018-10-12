# -*- coding: utf-8 -*-
import json
import scrapy
from ..items import DouyuItem
import time

class DouyumeinvSpider(scrapy.Spider):
    name = 'douyumeinv'
    allowed_domains = ['apiv2.douyucdn.cn']

    offect = 0
    url = 'https://apiv2.douyucdn.cn/gv2api/rkc/roomlist/1_8/'
    start_urls = [url + str(offect)+'/20/android?client_sys=android']
    times = time.time()
    time_ = int(times)

    headers = {
        'aid': 'android1',
        'time': time_,
        'auth': '5e6f7d5bbd1644193f3b6dedb691ede8',
        'Host': 'apiv2.douyucdn.cn',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'Cookie': 'acf_did=1c76e5c20765f5da45823a2230305111',
    }

    def parse(self, response):
        data = json.loads(response.text)['data']
        li = data['list']
        if len(li):
            for l in li:
                item = DouyuItem()
                item['nickname'] =l['nickname']
                item['image_url'] = l['vertical_src']

                yield item
        self.offect += 20
        yield scrapy.Request(self.url + str(self.offect)+'/20/android?client_sys=android', callback=self.parse)



