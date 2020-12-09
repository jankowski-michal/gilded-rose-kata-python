from dataclasses import dataclass


@dataclass
class Quality:
    amount: int

    def decrease(self):
        if self.amount > 0:
            self.amount -= 1

    def increase(self):
        if self.amount < 50:
            self.amount += 1

    def reset(self):
        self.amount = 0


@dataclass
class Generic:
    sell_in: int
    _quality: Quality

    def __init__(self, quality: int, sell_in: int) -> None:
        super().__init__()
        self._quality = Quality(quality)
        self.sell_in = sell_in

    @property
    def quality(self):
        return self._quality.amount

    @quality.setter
    def quality(self, amount: int):
        self._quality = Quality(amount)

    def update(self):
        self._quality.decrease()
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            self._quality.decrease()


@dataclass
class BackstagePass:
    sell_in: int
    _quality: Quality

    def __init__(self, quality: int, sell_in: int) -> None:
        super().__init__()
        self._quality = Quality(quality)
        self.sell_in = sell_in

    @property
    def quality(self):
        return self._quality.amount

    @quality.setter
    def quality(self, amount: int):
        self._quality = Quality(amount)

    def update(self):
        self._quality.increase()
        if self.sell_in < 11:
            self._quality.increase()
        if self.sell_in < 6:
            self._quality.increase()
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            self._quality.reset()


@dataclass
class AgedBree:
    sell_in: int
    _quality: Quality

    def __init__(self, quality: int, sell_in: int) -> None:
        super().__init__()
        self._quality = Quality(quality)
        self.sell_in = sell_in

    @property
    def quality(self):
        return self._quality.amount

    @quality.setter
    def quality(self, amount: int):
        self._quality = Quality(amount)

    def update(self):
        self._quality.increase()
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            self._quality.increase()


@dataclass
class Sulfuras:
    sell_in: int
    quality: int

    def update(self):
        pass
