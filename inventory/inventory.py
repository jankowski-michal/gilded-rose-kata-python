from dataclasses import dataclass


@dataclass
class Generic:
    sell_in: int
    quality: int

    def update(self):
        if self.quality > 0:
            self.quality = self.quality - 1
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            if self.quality > 0:
                self.quality = self.quality - 1


@dataclass
class BackstagePass:
    sell_in: int
    quality: int

    def update(self):
        if self.quality < 50:
            self.quality = self.quality + 1
            if self.sell_in < 11:
                if self.quality < 50:
                    self.quality = self.quality + 1
            if self.sell_in < 6:
                if self.quality < 50:
                    self.quality = self.quality + 1
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            self.quality = self.quality - self.quality


@dataclass
class AgedBree:
    sell_in: int
    quality: int

    def update(self):
        if self.quality < 50:
            self.quality = self.quality + 1
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            if self.quality < 50:
                self.quality = self.quality + 1


@dataclass
class Sulfuras:
    sell_in: int
    quality: int

    def update(self):
        pass
