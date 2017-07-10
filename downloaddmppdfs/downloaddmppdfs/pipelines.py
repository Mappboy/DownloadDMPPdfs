# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import tablib

class DownloaddmppdfsPipeline(object):

    def open_spider(self, spider):
        self.data = tablib.Dataset(headers=['name', 'url', 'summary', 'date_delivered', 'parties', 'tenement'])

    def close_spider(self, spider):
        self.file = open('dmp_pdgs.csv', 'w')
        self.file.write(self.data)
        self.file.close()


    def process_item(self, item, spider):
        self.data.append(item.values())
        return item
