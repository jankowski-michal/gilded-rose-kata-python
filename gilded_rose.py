# -*- coding: utf-8 -*-
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
AGED_BRIE = "Aged Brie"


def decrease_quality(item):
    item.quality = item.quality - 1


def increase_quality(item):
    item.quality = item.quality + 1


def quality_less_than_50(item):
    return item.quality < 50


def is_aged_brie(item):
    return item.name == AGED_BRIE


def is_backstage_pass(item):
    return item.name == BACKSTAGE_PASS


def is_sulfuras(item):
    return item.name == SULFURAS


def is_generic(item):
    return not (is_sulfuras(item) or is_backstage_pass(item) or is_aged_brie(item))


def handle_backstage_pass(item):
    if quality_less_than_50(item):
        increase_quality(item)
        if item.sell_in < 11:
            if quality_less_than_50(item):
                increase_quality(item)
        if item.sell_in < 6:
            if quality_less_than_50(item):
                increase_quality(item)
    item.sell_in = item.sell_in - 1


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if is_sulfuras(item):
                pass
            elif is_generic(item):
                if item.quality > 0:
                    decrease_quality(item)
                item.sell_in = item.sell_in - 1
            elif is_aged_brie(item):
                if quality_less_than_50(item):
                    increase_quality(item)
                item.sell_in = item.sell_in - 1
            elif is_backstage_pass(item):
                handle_backstage_pass(item)

            if item.sell_in < 0:
                if is_aged_brie(item):
                    if quality_less_than_50(item):
                        increase_quality(item)
                else:
                    if not is_backstage_pass(item):
                        if item.quality > 0:
                            if not is_sulfuras(item):
                                decrease_quality(item)
                    else:
                        item.quality = item.quality - item.quality


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
