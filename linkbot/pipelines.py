# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import urllib, urllib2

class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = []

    def process_item(self, item, spider):
        if item['page_links'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.append(item['page_links'])
            return item
        
class PostPipeline(object):

    def process_item(self, item, spider):
        url = 'http://infinite-fjord-7446.herokuapp.com/link'
        #url = 'http://localhost:3000/link'
        links_string = ','.join(item['page_links'])
        values = {'links':links_string, 'source':'snagajob'}
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        content = response.read()
        print urllib.quote_plus(content)
