# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

CONJURED_MANA_CAKE = 'Conjured Mana Cake'
SULFURAS = 'Sulfuras, Hand of Ragnaros'
ELIXIR_OF_THE_MONGOOSE = 'Elixir of the Mongoose'
DEXTERITY_VEST = '+5 Dexterity Vest'
AGED_BRIE = 'Aged Brie'
BACKSTAGE_PASSES = 'Backstage passes to a TAFKAL80ETC concert'


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item('foo', 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual('foo', items[0].name)

    def create_item_and_update_quality(self, name, sell_in, quality):
        items = [Item(name, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        return items[0]

    def assert_item_sell_in(self, expected, name, sell_in, quality):
        item = self.create_item_and_update_quality(name, sell_in, quality)
        self.assertEqual(expected, item.sell_in)

    def assert_item_quality(self, expected, name, sell_in, quality):
        item = self.create_item_and_update_quality(name, sell_in, quality)
        self.assertEqual(expected, item.quality)

    def assert_backstage_passes_quality(self, expected, sell_in, quality):
        self.assert_item_quality(expected, BACKSTAGE_PASSES, sell_in, quality)

    def assert_backstage_passes_sell_in(self, expected, sell_in, quality):
        self.assert_item_sell_in(expected, BACKSTAGE_PASSES, sell_in, quality)

    def assert_brie_quality(self, expected, sell_in, quality):
        self.assert_item_quality(expected, AGED_BRIE, sell_in, quality)

    def assert_brie_sell_in(self, expected, sell_in, quality):
        self.assert_item_sell_in(expected, AGED_BRIE, sell_in, quality)

    def assert_elixir_quality(self, expected, sell_in, quality):
        self.assert_item_quality(expected, ELIXIR_OF_THE_MONGOOSE, sell_in, quality)

    def assert_elixir_sell_in(self, expected, sell_in, quality):
        self.assert_item_sell_in(expected, ELIXIR_OF_THE_MONGOOSE, sell_in, quality)

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

    def test_elixir(self):
        self.assert_elixir_quality(6, 5, 7)
        self.assert_elixir_quality(5, -1, 7)

        self.assert_elixir_sell_in(4, 5, 7)
        self.assert_elixir_sell_in(-2, -1, 7)

    def test_dexterity_vest(self):
        self.assert_item_quality(19, DEXTERITY_VEST, 10, 20)

        self.assert_item_sell_in(9, DEXTERITY_VEST, 10, 20)

    def test_mana_cake(self):
        self.assert_item_quality(5, CONJURED_MANA_CAKE, 3, 6)

        self.assert_item_sell_in(2, CONJURED_MANA_CAKE, 3, 6)

    def test_sulfuras(self):
        self.assert_sulfuras_quality(80, 0, 80)
        self.assert_sulfuras_quality(80, -1, 80)

        self.assert_sulfuras_sell_in(0, 0, 80)
        self.assert_sulfuras_sell_in(-1, -1, 80)


if __name__ == '_main_':
    unittest.main()
