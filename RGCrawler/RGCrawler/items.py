# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ReferenceItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    date = scrapy.Field()
    conference = scrapy.Field()


class PaperItem(scrapy.Item):
    # define the fields for your item here like:
    root_title = scrapy.Field()
    child_title = scrapy.Field()
