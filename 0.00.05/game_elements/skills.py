

class Skill:
    def __init__(self, name, modifier, proficiency):
        self.name = name
        self.modifier = modifier
        self.proficiency = proficiency
        self.bonus = proficiency + modifier


class Spell:
    def __init__(self, name, range, hit, effect, slot_cost):
        self.name = name
        self.range = range
        self.hit = hit
        self.effect = effect
        self.slot_cost = slot_cost
