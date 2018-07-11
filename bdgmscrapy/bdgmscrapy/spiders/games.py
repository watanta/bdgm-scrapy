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
    		yield Request(absolute_url, callback=self.parse_game)

    	next_page_url = response.xpath('//*[@id="main-content"]//a[@rel="next"]/@href').extract_first()
    	absolute_next_page_url = response.urljoin(next_page_url)
    	yield Request(absolute_next_page_url)


    def parse_game(self, response):

    	title = response.xpath('//*[@id="games-detail"]/div/div[4]/table//td/text()').extract()[0]
    	en_title = response.xpath('//*[@id="games-detail"]/div/div[4]/table//td/text()').extract()[1]
    	players = response.xpath('//*[@id="games-detail"]/div/div[4]/table//td/text()').extract()[2]
    	target_age = response.xpath('//*[@id="games-detail"]/div/div[4]/table//td/text()').extract()[3]
    	published_at = response.xpath('//*[@id="games-detail"]/div/div[4]/table//td/text()').extract()[4]
    	price = response.xpath('//*[@id="games-detail"]/div/div[4]/table//td/text()').extract()[5]
    	yield {'title':title, 'en_title':en_title, 'players':players, 'target_age':target_age, 'published_at':published_at, 'price':price}
