# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class CodingChallengePipeline:
    def process_item(self, item, spider):

    	adapter = ItemAdapter(item)

    	# Convert price to float
    	if adapter.get('price'):
    		adapter['price'] = float(adapter['price'].replace('\u00a3', ''))
    	
    	return item