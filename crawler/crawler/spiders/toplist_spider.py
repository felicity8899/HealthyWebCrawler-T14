import re
import scrapy
from scrapy.spiders import Spider
from bs4 import BeautifulSoup

class TopListSpider(scrapy.Spider):
    name = "toplist"
    allowed_domains = ["app.mi.com"]
    start_urls = ["http://app.mi.com/topList?page=1"]

    def parse(self, response):
        #print response.body
        common_url = "app.mi.com"
        html_doc = BeautifulSoup(response.body, "lxml")
        
        for link in html_doc.find_all('h5'):
        	app_tag = link.find('a')
        	name = app_tag.contents
        	url = app_tag["href"]
        	print ', '.join(name)
        	print common_url + url
 
