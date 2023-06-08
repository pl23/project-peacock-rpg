

class Item:
    def __init__(self, name, main_type, sub_type, effect, count, weight):
        self.main_type = main_type
        self.name = name
        self.sub_type = sub_type
        self.effect = effect
        self.count = count
        self.weight = weight


class Weapon(Item):
    def __init__(self, name, main_type, sub_type, effect, range, hit, damage):
        super().__init__(name, main_type, sub_type, effect)
        self.range = range
        self.hit = hit
        self.damage = damage
