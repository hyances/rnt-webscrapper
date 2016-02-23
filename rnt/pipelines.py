# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import json
import codecs


class RntCartagena(object):
    """
    A pipeline for filtering out items which contain certain words in their
    description.
    TODO: Add conditionals to calls methods by spider used. 
    """

    # put all words in lowercase
    words_to_filter = ['cartagena']
    
    def process_item(self, item, spider):
        for word in self.words_to_filter:
            if word in unicode(item['city']).lower():
                return item
        else:
            raise DropItem("Contains city different to: %s" % word)


class RntEmpty(object):
    """
    A pipeline for filtering out items which contain certain words in their
    description.
    TODO: Add conditionals to calls methods by spider used. 
    """

    # put all words in lowercase
    #words_to_filter = ['']
    
    def process_item(self, item, spider):
        if unicode(item['city']).isspace() or len(unicode(item['city'])) == 0 or unicode(item['city']).find("[]", beg=0, end=3):
            raise DropItem("Contains empty city: %s" % word)
        else:
            return item


class JsonWithEncodingPipeline(object):

    def __init__(self):
        self.file = codecs.open('scraped_data_utf8.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()