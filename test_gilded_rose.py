# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_fixture(self):
        report_lines = []
        items = [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
        ]

        days = 2
        import sys
        if len(sys.argv) > 1:
            days = int(sys.argv[1]) + 1
        for day in range(days):
            report_lines.append("-------- day %s --------" % day)
            report_lines.append("name, sellIn, quality")
            for item in items:
                report_lines.append(str(item))
            report_lines.append("")
            GildedRose(items).update_quality()
        self.assertEqual(
            ["-------- day 0 --------",
             "name, sellIn, quality",
             "+5 Dexterity Vest, 10, 20",
             "Aged Brie, 2, 0",
             "Elixir of the Mongoose, 5, 7",
             "Sulfuras, Hand of Ragnaros, 0, 80",
             "Sulfuras, Hand of Ragnaros, -1, 80",
             "Backstage passes to a TAFKAL80ETC concert, 15, 20",
             "Backstage passes to a TAFKAL80ETC concert, 10, 49",
             "Backstage passes to a TAFKAL80ETC concert, 5, 49",
             "Conjured Mana Cake, 3, 6",
             "",
             "-------- day 1 --------",
             "name, sellIn, quality",
             "+5 Dexterity Vest, 9, 19",
             "Aged Brie, 1, 1",
             "Elixir of the Mongoose, 4, 6",
             "Sulfuras, Hand of Ragnaros, 0, 80",
             "Sulfuras, Hand of Ragnaros, -1, 80",
             "Backstage passes to a TAFKAL80ETC concert, 14, 21",
             "Backstage passes to a TAFKAL80ETC concert, 9, 50",
             "Backstage passes to a TAFKAL80ETC concert, 4, 50",
             "Conjured Mana Cake, 2, 5",
             ""],
            report_lines)


if __name__ == '__main__':
    unittest.main()
