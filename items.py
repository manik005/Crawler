# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	#name = Field()
    #pass
    model=Field()
    offer=Field()
    image=Field()
    standard_url=Field()
    included_software=Field()
    ram=Field()
    ram_type=Field()
    brand=Field()
    part_number=Field()
    model_id=Field()
 #   processor=Field()
 #   ram=Field()
 #   hdd=Field()