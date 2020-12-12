# -*- coding: utf-8 -*-
import unittest

from src.gilded_rose import Item, GildedRose

SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
AGED_BRIE = "Aged Brie"


def create_item_and_update_quality(name, sell_in, quality):
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    return items[0]


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        item = Item('foo', 0, 0)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual('foo, -1, 0', str(item))

    def assert_item_sell_in(self, expected, name, sell_in, quality):
        item = create_item_and_update_quality(name, sell_in, quality)
        self.assertEqual(expected, item.sell_in)

    def assert_item_quality(self, expected, name, sell_in, quality):
        item = create_item_and_update_quality(name, sell_in, quality)
        self.assertEqual(expected, item.quality)

    def assert_generic_quality(self, expected, sell_in, quality):
        self.assert_item_quality(expected, 'A generic name', sell_in, quality)

    def assert_generic_sell_in(self, expected, sell_in, quality):
        self.assert_item_sell_in(expected, 'A generic name', sell_in, quality)

    def assert_backstage_passes_quality(self, expected, sell_in, quality):
        self.assert_item_quality(expected, BACKSTAGE_PASS, sell_in, quality)

    def assert_backstage_passes_sell_in(self, expected, sell_in, quality):
        self.assert_item_sell_in(expected, BACKSTAGE_PASS, sell_in, quality)

    def assert_brie_quality(self, expected, sell_in, quality):
        self.assert_item_quality(expected, AGED_BRIE, sell_in, quality)

    def assert_brie_sell_in(self, expected, sell_in, quality):
        self.assert_item_sell_in(expected, AGED_BRIE, sell_in, quality)

    def assert_sulfuras_quality(self, expected, sell_in, quality):
        self.assert_item_quality(expected, SULFURAS, sell_in, quality)

    def assert_sulfuras_sell_in(self, expected, sell_in, quality):
        self.assert_item_sell_in(expected, SULFURAS, sell_in, quality)

    def test_backstage_pass(self):
        self.assert_backstage_passes_quality(21, 15, 20)
        self.assert_backstage_passes_quality(50, 10, 49)
        self.assert_backstage_passes_quality(50, 5, 49)
        self.assert_backstage_passes_quality(50, 4, 47)
        self.assert_backstage_passes_quality(0, -1, 47)
        self.assert_backstage_passes_quality(23, 1, 20)  # kills 2 mutants

        self.assert_backstage_passes_sell_in(14, 15, 20)
        self.assert_backstage_passes_sell_in(9, 10, 49)
        self.assert_backstage_passes_sell_in(4, 5, 49)
        self.assert_backstage_passes_sell_in(3, 4, 47)
        self.assert_backstage_passes_sell_in(-2, -1, 47)

    def test_aged_brie(self):
        self.assert_brie_quality(1, 2, 0)
        self.assert_brie_quality(2, -1, 0)

        self.assert_brie_sell_in(1, 2, 0)
        self.assert_brie_sell_in(-2, -1, 0)

    def test_generic(self):
        self.assert_generic_quality(6, 5, 7)
        self.assert_generic_quality(5, -1, 7)
        self.assert_generic_quality(19, 10, 20)
        self.assert_generic_quality(5, 3, 6)
        self.assert_generic_quality(1, 1, 2)  # kills 2 mutants
        self.assert_generic_quality(0, 0, 2)  # kills 1 mutant

        self.assert_generic_sell_in(4, 5, 7)
        self.assert_generic_sell_in(-2, -1, 7)
        self.assert_generic_sell_in(9, 10, 20)
        self.assert_generic_sell_in(2, 3, 6)

    def test_sulfuras(self):
        self.assert_sulfuras_quality(80, 0, 80)
        self.assert_sulfuras_quality(80, -1, 80)

        self.assert_sulfuras_sell_in(0, 0, 80)
        self.assert_sulfuras_sell_in(-1, -1, 80)


if __name__ == '_main_':
    unittest.main()
