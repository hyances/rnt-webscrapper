# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field
from scrapy import log
from scrapy.utils.python import unicode_to_str
import unicodedata

log.msg("This is a log message", level=log.DEBUG)


def serialize_field(value):
    #return '%s' % str(value)[7:-2].strip()
    #return "%s" % str(''.join(value)).encode('utf-8','strict').strip()
    #value_enc = ''.join(map(str, value))
    #return '%s' % value_enc.strip()
    #return '%s' % unicode_to_str(''.join(str(value)), 'utf-8').strip()

    scrapy_list = map(unicode_to_str, value)
    new_item = ""
    for item in scrapy_list:
        new_item += item
        return '%s' % new_item.strip()

class RntItem(Item):
    
    '''
    National Tourism Register Fields.  Query done to confecamaras portal
    - - - 
    '''

    # COMPANY
    social_scope = Field(serializer=serialize_field)
    nit = Field(serializer=serialize_field)
    ciiu = Field(serializer=serialize_field)
    legal_rep = Field(serializer=serialize_field)
    # VENUE
    condition = Field(serializer=serialize_field)
    update_date = Field(serializer=serialize_field)
    category = Field(serializer=serialize_field)
    subcategory = Field(serializer=serialize_field)
    state = Field(serializer=serialize_field)
    city = Field(serializer=serialize_field)
    comercial_add = Field(serializer=serialize_field)
    name = Field(serializer=serialize_field)
    phone = Field(serializer=serialize_field)
    fax = Field(serializer=serialize_field)
    manager = Field(serializer=serialize_field)
    mobile = Field(serializer=serialize_field)
    email = Field(serializer=serialize_field)
    employees = Field(serializer=serialize_field)
    state_legal_not = Field(serializer=serialize_field)
    city_legal_not = Field(serializer=serialize_field)
    add_legal_not = Field(serializer=serialize_field)
    phone_legal_not = Field(serializer=serialize_field)
    # ESPECIALES POR MODELO (si es hotel, restaurante, etc)
    rooms = Field(serializer=serialize_field)
    beds = Field(serializer=serialize_field)



