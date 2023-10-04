# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class AgedBrie(Item):
    def update(self):
        if self.quality < 50:
            self.quality += 1
        self.sell_in -= 1

class Sulfuras(Item):
    def update(self):
        return

class BackstagePasses(Item):
    def update(self):
        self.quality += 1
        if self.sell_in <= 10:
            self.quality += 1
        if self.sell_in <= 5:
            self.quality += 1
        if self.quality > 50:
            self.quality = 50
        self.sell_in -= 1

class NormalItem(Item):
    def update(self):
        self.quality -= 1
        if self.sell_in < 0:
            self.quality -= 1
        if self.quality > 50:
            self.quality = 50
        if self.quality < 0:
            self.quality = 0
        self.sell_in -= 1

class Conjured(Item):
    def update(self):
        self.quality -= 2
        if self.sell_in < 0:
            self.quality -= 2
        if self.quality > 50:
            self.quality = 50
        if self.quality < 0:
            self.quality = 0
        self.sell_in -= 1

class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items
        self.classes = {
            "Aged Brie": AgedBrie,
            "Conjured Mana Cake": Conjured,
            "Sulfuras, Hand of Ragnaros": Sulfuras,
            "Backstage passes to a TAFKAL80ETC concert": BackstagePasses
        }
    
    def update_quality(self):
        for idx, item in enumerate(self.items):
            curClass = self.classes.get(item.name, NormalItem)
            newItem = curClass(item.name, item.sell_in, item.quality)
            newItem.update()
            self.items[idx] = newItem
            

    # def update_quality(self):
    #     for item in self.items:
    #         if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
    #             if item.quality > 0:
    #                 if item.name != "Sulfuras, Hand of Ragnaros":
    #                     item.quality = item.quality - 1
    #         else:
    #             if item.quality < 50:
    #                 item.quality = item.quality + 1
    #                 if item.name == "Backstage passes to a TAFKAL80ETC concert":
    #                     if item.sell_in < 11:
    #                         if item.quality < 50:
    #                             item.quality = item.quality + 1
    #                     if item.sell_in < 6:
    #                         if item.quality < 50:
    #                             item.quality = item.quality + 1
    #         if item.name != "Sulfuras, Hand of Ragnaros":
    #             item.sell_in = item.sell_in - 1
    #         if item.sell_in < 0:
    #             if item.name != "Aged Brie":
    #                 if item.name != "Backstage passes to a TAFKAL80ETC concert":
    #                     if item.quality > 0:
    #                         if item.name != "Sulfuras, Hand of Ragnaros":
    #                             item.quality = item.quality - 1
    #                 else:
    #                     item.quality = item.quality - item.quality
    #             else:
    #                 if item.quality < 50:
    #                     item.quality = item.quality + 1
