# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# https://stackoverflow.com/questions/33290876/how-to-create-custom-scrapy-item-exporter
from RGCrawler.ReferenceItemExporter import ReferenceItemExporter


class RgcrawlerPipeline(object):
    def __init__(self):
        self.file = open('output/result.json', 'wb')
        self.exporter = ReferenceItemExporter(self.file)

    def open_spider(self, spider):
        # Creating a FanItemExporter object and initiating export
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        # passing the item to FanItemExporter object for expoting to file
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        # Ending the export to file from FanItemExport object
        self.exporter.finish_exporting()

        # Closing the opened output file
        self.file.close()
