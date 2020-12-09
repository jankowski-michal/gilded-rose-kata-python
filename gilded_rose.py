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


def handle_aged_brie(item):
    if quality_less_than_50(item):
        increase_quality(item)
    item.sell_in = item.sell_in - 1
    if item.sell_in < 0:
        if quality_less_than_50(item):
            increase_quality(item)


def handle_generic(item):
    if item.quality > 0:
        decrease_quality(item)
    item.sell_in = item.sell_in - 1
    if item.sell_in < 0:
        if item.quality > 0:
            decrease_quality(item)


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
    if item.sell_in < 0:
        item.quality = item.quality - item.quality


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if is_sulfuras(item):
                pass
            elif is_aged_brie(item):
                handle_aged_brie(item)
            elif is_backstage_pass(item):
                handle_backstage_pass(item)
            else:
                handle_generic(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
