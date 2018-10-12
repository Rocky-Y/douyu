# -*- coding: utf-8 -*-

import scrapy
import requests
from PIL import Image
from io import BytesIO


class DouyuPipeline(object):

    def process_item(self, item, spider):
        image_url = item['image_url']
        response = requests.get(image_url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'})
        image = Image.open(BytesIO(response.content))
        image.save('D:/python/颜值' + item['nickname'] + '.jpg')
        return item



