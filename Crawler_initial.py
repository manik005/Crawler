__author__ = 'shruti'

# Crawler to crawl flipkart


from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from tutorial.items import CrawlingItem
import json
import string

class FlipkartSpider(BaseSpider):
    name = "flipkart_spider"
    allow_domains = ["flipkart.com"]


    def start_requests(self):
        x = 1
        lines = [{
            "url": "http://www.flipkart.com/laptops/pr?sid=6bo,b5g&otracker=ch_vn_laptop_filter_Laptop%20Brands_All%20Brands",
            "count": "65"}]
        url = lines[0]['url']
        count = str(lines[0]['count'])
        count = int(count) + 1
        y = 1
        p = str(x)
        while x < count:
            # p=str(x)
            yield self.make_requests_from_url((url).format(p))
            x = x + 1
            p = int(x)
            p = x
            p = str(p)
            if x >= count:
                if y < 3:
                    url = lines[y]['url']
                    count = lines[y]['count']
                    count = int(count) + 1
                    y = y + 1
                    x = 1

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("//div[contains(@class,'product-unit unit-4 browse-product new-design')]")
        items = []
        count1 = 0
        for title in titles:
            count1 = count1 + 1
            item = CrawlingItem()
            item['model'] = title.select(".//div[contains(@class,'pu-title')]/a/text()").extract()
            item['offer'] = title.select(".//div[contains(@class,'pu-final')]/span/text()").extract()
            item['image'] = title.select(".//div[contains(@class,'pu-visual-section')]/a/img/@src").extract()
            item['standard_url'] = title.select(".//div[contains(@class,'pu-title')]/a/@href").extract()
            items.append(item)

        return items
