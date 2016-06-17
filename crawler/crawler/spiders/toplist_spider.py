import re
import scrapy
from scrapy.spiders import Spider
from bs4 import BeautifulSoup

class TopListSpider(scrapy.Spider):
    name = "toplist"
    allowed_domains = ["app.mi.com"]
    start_urls = ["http://app.mi.com/topList?page=1"]


    def parse(self, response):
        for page_id in range(1,2):
            url = '{0}{1}'.format('http://app.mi.com/topList?page=', str(page_id)) 
            yield scrapy.Request(url, callback=self.parse_page)
        
            
    def parse_page(self, response):
        common_url = 'http://app.mi.com'
        item = {}

        html_doc = BeautifulSoup(response.body, "lxml")
        
        for link in html_doc.find_all('h5'):
            app_tag = link.find('a')
            if not app_tag:
                continue
            name = app_tag.contents
            url = app_tag["href"]
            req = scrapy.Request(common_url + url, callback=self.parse_details)
            req.meta["item"] = item
            yield req
        
        '''category_names = html_doc.find_all("p", "app-desc")'''


    def parse_details(self, response):
        item = response.meta["item"]
        detail_doc = BeautifulSoup(response.body, "lxml")

        # get name, developer, category, rating, number of scores
        ret = detail_doc.find("div", "intro-titles")
        app_name = ret.find("h3").contents[0]
        p_tag_list = ret.find_all("p")
        div_tag_list = ret.find_all("div")
        app_developer = p_tag_list[0].contents[0]
        app_category = p_tag_list[1].contents[1]
        app_rating_counts = (re.search(r'\d+', ret.find("span", "app-intro-comment").contents[0])).group()
        app_rating = div_tag_list[1]["class"][1]
        app_rating = re.match(r'star1-(\d+)', app_rating).group(1)
        #print name, developer, category, rating_counts, rating

        #  get version and update time
        ret = detail_doc.find("ul", " cf")
        li_tag_list = ret.find_all("li")
        app_version = li_tag_list[3].contents[0]
        app_update_time = li_tag_list[5].contents[0]

        #get recommend app and developers application 
        ret = detail_doc.find("div", "second-imgbox")
        for i in xrange(len(ret)):
            li_list = ret.find_all("li")
            for j in li_list:
                link = j.find("a")["href"]
                app_id = re.match(r'/detail/(\d+)', link)
                #print app_id.group(1)
                rating = j.find("div")
                rating = (re.match(r'star-(\d+)', rating.div["class"][1])).group(1)

            #if i == 0:

            #else:


        yield item  