from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from rnt.items import RntItem

class RtnVenues(CrawlSpider):
    name = 'venues'
    allowed_domains = ['rnt.rue.com.co']
        
    #start_urls = ['http://rnt.rue.com.co/index.php/detalle-establecimiento/6555/promotora-inmobiliaria-dann-medellin-s-a']
    start_urls = ['http://rntcartagena.confecamaras.co/detalle-establecimiento/5891/hospedaje-el-paisita-7']
    rules = (
        Rule(SgmlLinkExtractor(allow='index\.php\detalle-establecimiento'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        i = RntItem()
        # COMPANY
        i['social_scope'] = hxs.select('//table[1]//tr[2]/td/text()').extract()
        i['nit'] = hxs.select('//table[1]//tr[3]/td/text()').extract()
        i['ciiu'] = hxs.select('//table[1]//tr[4]/td//ul/li/text()').extract()
        i['legal_rep'] = hxs.select('//table[1]//tr[5]/td//ul/li/text()').extract()
        # VENUE
        i['condition'] = hxs.select('//table[2]//tr[1]/td/span/text()').extract()
        i['update_date'] = hxs.select('//table[2]//tr[2]/td/text()').extract()
        i['category'] = hxs.select('//table[2]//tr[4]/td/text()').extract()
        i['subcategory'] = hxs.select('//table[2]//tr[5]/td/text()').extract()
        i['state'] = hxs.select('//table[2]//tr[6]/td/text()').extract()
        i['city'] = hxs.select('//table[2]//tr[8]/td/text()').extract()
        i['comercial_add'] = hxs.select('//table[2]//tr[9]/td/text()').extract()
        i['name'] = hxs.select('//table[2]//tr[10]/td/text()').extract()
        i['phone'] = hxs.select('//table[2]//tr[11]/td/text()').extract()
        i['fax'] = hxs.select('//table[2]//tr[12]/td/text()').extract()
        i['manager'] = hxs.select('//table[2]//tr[13]/td/text()').extract()
        i['mobile'] = hxs.select('//table[2]//tr[14]/td/text()').extract()
        i['email'] = hxs.select('//table[2]//tr[15]/td/text()').extract()
        i['employees'] = hxs.select('//table[2]//tr[16]/td/text()').extract()
        i['state_legal_not'] = hxs.select('//table[2]//tr[17]/td/text()').extract()
        i['city_legal_not'] = hxs.select('//table[2]//tr[18]/td/text()').extract()
        i['add_legal_not'] = hxs.select('//table[2]//tr[19]/td/text()').extract()
        i['phone_legal_not'] = hxs.select('//table[2]//tr[20]/td/text()').extract()
        # ESPECIALES POR MODELO (si es hotel, restaurante, etc)
        i['rooms'] = hxs.select('//table[3]//tr[1]/td/text()').extract()
        i['beds'] = hxs.select('//table[3]//tr[2]/td/text()').extract()
        return i
