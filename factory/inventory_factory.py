from inventory.inventory import Sulfuras, AgedBree, BackstagePass, Generic

SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
AGED_BRIE = "Aged Brie"


class GoodCategory:

    @staticmethod
    def build_for_item(item):
        if item.name == SULFURAS:
            return Sulfuras(quality=item.quality, sell_in=item.sell_in)
        elif item.name == AGED_BRIE:
            return AgedBree(quality=item.quality, sell_in=item.sell_in)
        elif item.name == BACKSTAGE_PASS:
            return BackstagePass(quality=item.quality, sell_in=item.sell_in)
        else:
            return Generic(quality=item.quality, sell_in=item.sell_in)
