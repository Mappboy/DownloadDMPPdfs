# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader

from ..items import DownloaddmppdfsItem


class DmpMineralsSpider(scrapy.Spider):
    name = 'dmp_minerals'
    allowed_domains = ['http://www.dmp.wa.gov.au']
    start_urls = [
        'http://www.dmp.wa.gov.au/Minerals/Warden-s-Court-Decisions-12609.aspx?query=!padrenull!&sort=date&facetScope=&start_rank=1']

    def parse(self, response):
        for result in response.css("div.search-results-listing"):
            l = ItemLoader(DownloaddmppdfsItem(), result)
            l.add_css('name', 'a.result-title > strong::text')
            l.add_xpath('file_urls', 'a.result-title::attr(href)')
            l.add_xpath('summary', '//span[@class="result-text"][0]')
            l.add_xpath('date_delivered', '//span[@class="result-text"][1]')
            l.add_xpath('parties', '//span[@class="result-text"][2]')  # you can also use literal values
            l.add_xpath('tenement', '//span[@class="result-text"][3]')  # you can also use literal values
        yield l.load_item()

        # next_page_url = response.css("div.pagination").xpath('//li[contains(.,"Next")]').extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))

