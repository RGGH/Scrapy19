# -*- coding: utf-8 -*-
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import os

import scrapy
from scrapy import Request
from scrapy.crawler import CrawlerProcess 
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup

#import sys
#sys.path.insert(0,'..')
from ..items import JobzItem

# class to scrape jooble and visit 3rd part links
class Jobz(scrapy.Spider):			

    name = 'jobzspider' 
    start_urls = ['https://uk.jooble.org/SearchResult?date=8&loc=2&p=2&rgns=Remote&ukw=\
    python%20engineer']
    
    headers = {'sec-fetch-user': '?1', 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8', \
    'accept-encoding': 'gzip,', 'sec-fetch-site': 'same-origin', 'accept': 'text/html,\
    application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,\
    application/signed-exchange;v=b3;q=0.9', 'upgrade-insecure-requests': '1',\
     'referer': 'https://www.jooble.org/', 'sec-fetch-mode': 'navigate', \
     'cache-control': 'max-age=0', 'user-agent': \
     ' Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
     Chrome/87.0.4280.88 Safari/537.36', 'sec-fetch-dest': 'document'}

    def parse(self, response):
        
        links = response.xpath('//h2/a/@href').getall()
        #print(links)
        for link in links:        
            yield response.follow(url=link, headers=self.headers, callback=self.parse_detail)
            print(response.url)

    def parse_detail(self, response):

        # Use items and pipelines for SQL

        items = JobzItem()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        items['description'] = soup.get_text()[:400]
        items['url'] = response.url[:180]
        items['posted'] = '2000-12-11'
        yield items


# main driver
#if __name__ =='__main__':
#    process = CrawlerProcess()
#    process.crawl(Jobz)
#    process.start()
