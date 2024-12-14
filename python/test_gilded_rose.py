# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    @staticmethod
    def updater(gilded_rose, days):
        for _ in range(days):
            gilded_rose.update_quality()
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("fixme", items[0].name)

    def test_aged_brie(self):
        # Set up the item
        item = Item("Aged Brie", 10, 20)
        gilded_rose = GildedRose([item])

        # One day after
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 21)

        # Sell by date passed
        GildedRoseTest.updater(gilded_rose, item.sell_in + 1)
        self.assertEqual(item.sell_in, -1)

        # Quality increases twice as fast now
        self.assertEqual(item.quality, 32)
        GildedRoseTest.updater(gilded_rose, 10)
        self.assertEqual(item.sell_in, -11)
        self.assertEqual(item.quality, 50)

        
if __name__ == '__main__':
    unittest.main()
