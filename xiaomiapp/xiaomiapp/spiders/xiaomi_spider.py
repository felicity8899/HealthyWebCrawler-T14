import scrapy
from scrapy.spiders import Spider
from scrapy import Request
import re
from scrapy.selector import Selector
from xiaomiapp.items import XiaomiAppItem

class XiaomiSpider(Spider):
    name = "xiaomi"
    allowed_domain = ["app.mi.com"]
    start_urls = [
        "http://app.mi.com/topList?page=1"
    ]


    def parse(self, response):
        page = Selector(response)
        page_list = page.xpath('//div[@class="pages"]/a')
        page_max = int(page_list[-2].xpath('text()').extract_first())

        for page_id in xrange(1, 2):
            url = '{0}{1}'.format('http://app.mi.com/topList?page=', str(page_id))
            yield scrapy.Request(url, callback=self.parse_page)

        # print page_list[-2]
        # print type(page_list[-2].xpath('text()').extract_first())

    def parse_page(self, response):
        page = Selector(response)
        page_list = page.xpath('//ul[@class="applist"]/li')

        if page_list == None:
            return

        url_base = 'http://app.mi.com'

        for l in page_list:
            item = XiaomiAppItem()
            item['title'] = l.xpath('./h5/a/text()').extract_first().encode('utf-8')
            url = l.xpath('./h5/a/@href').extract_first()
            appid = re.match(r'/detail/(\d+)', url).group(1)
            item['appid'] = appid

            item['category'] = l.xpath('./p/a/text()').extract_first().encode('utf-8')
            url_c = l.xpath('./p/a/@href').extract_first()
            groupid = re.match(r'/category/(.*)', url_c).group(1)
            item['groupid'] = groupid

            req = scrapy.Request(url_base + url, callback=self.parse_details)
            req.meta["item"] = item
            yield req

            #print url
            #print appid
            #print groupid
    def parse_details(self, response):
        item = response.meta["item"]
        page = Selector(response)
        page_list = page.xpath('//div[@class="second-imgbox"]/ul/li')

        recommended = []

        for l in page_list:
            url = l.xpath('./a/@href').extract_first()
            appid = re.match(r'/detail/(\d+)', url).group(1)
            recommended.append(appid)
            #print appid

        item["recommended"] = recommended

        yield item
