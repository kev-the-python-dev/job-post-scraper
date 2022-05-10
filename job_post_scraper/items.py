from scrapy.item import Item, Field

class YCombItem(Item):
    title = Field()
    url = Field()
    applied = Field()




