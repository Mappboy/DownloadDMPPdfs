# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DownloaddmppdfsItem(scrapy.Item):
    name = scrapy.Field()
    file_urls = scrapy.Field()
    summary = scrapy.Field()
    date_delivered = scrapy.Field()
    parties = scrapy.Field()
    tenement = scrapy.Field()
    files = scrapy.Field()