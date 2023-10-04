# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(0, items[0].quality)
        assert 0 <= items[0].quality <= 50

    
    def test_AgedBrie(self):
        items = [Item("Aged Brie", 3, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Aged Brie", items[0].name)
        self.assertEquals(2, items[0].sell_in)
        self.assertEquals(4, items[0].quality)
        assert 0 <= items[0].quality <= 50

    def test_BackstagePasses(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 3, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEquals(2, items[0].sell_in)
        self.assertEquals(6, items[0].quality)
        assert 0 <= items[0].quality <= 50

    def test_Sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 3, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEquals(3, items[0].sell_in)
        self.assertEquals(3, items[0].quality)
        assert 0 <= items[0].quality <= 50
    
    def test_Conjured(self):
        items = [Item("Conjured Mana Cake", 3, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Conjured Mana Cake", items[0].name)
        self.assertEquals(2, items[0].sell_in)
        self.assertEquals(1, items[0].quality)
        assert 0 <= items[0].quality <= 50

    


if __name__ == '__main__':
    unittest.main()
