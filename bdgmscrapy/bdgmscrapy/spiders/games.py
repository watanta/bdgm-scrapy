# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import logging

logger = logging.getLogger('mycustomlogger')

class GamesSpider(scrapy.Spider):
    name = 'games'
    allowed_domains = ['bodoge.hoobby.net']
    start_urls = ['https://bodoge.hoobby.net/games']

    def parse(self, response):
    	urls = response.xpath('//*[@id="main-content"]/div/ul/li/a/@href').extract()

    	for url in urls:
    		absolute_url = response.urljoin(url)
    		logger.info(absolute_url)
    		yield Request(absolute_url, callback=self.parse_book)

    def parse_book(self, response):
    	pass
