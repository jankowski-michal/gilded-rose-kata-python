# -*- coding: utf-8 -*-
from factory.inventory_factory import GoodCategory


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            good = GoodCategory().build_for_item(item)
            good.update()
            item.quality = good.quality
            item.sell_in = good.sell_in


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
