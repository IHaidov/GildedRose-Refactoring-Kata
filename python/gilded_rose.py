# -*- coding: utf-8 -*-

class GildedRose(object):
    MAX_QUALITY = 50
    MAX_CONJURED_QUALITY = 80

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if "Aged Brie" in item.name:
                self.update_aged_brie(item)
            elif "Backstage passes" in item.name:
                self.update_backstage_passes(item)
            elif "Sulfuras" in item.name:
                self.update_sulfuras(item)
            elif "Conjured" in item.name:
                self.update_conjured(item)
            else:
                self.update_normal_item(item)

    def update_aged_brie(self, item):
        if item.quality < self.MAX_QUALITY:
            item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality < self.MAX_QUALITY:
            item.quality += 1
            
    
    def update_backstage_passes(item):
        return
    
    def update_sulfuras(item):
        return
    
    def update_normal_item(item):
        if item.quality > 0:
            item.quality -= 1
            if item.sell_in <= 0:
                item.quality -= 1
        item.quality = max(0, item.quality)
        item.sell_in -= 1

    def update_conjured(item):
        return
    

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
