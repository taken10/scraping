# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 不要なクラス
# class MyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass

# データ格納用オブジェクト
class Headline(scrapy.Item):
    title = scrapy.Field()
    body = scrapy.Field()