from game_elements.items import Item


class Character:
    def __init__(self, name, age, gender, stats, inventory, spells, checkpoint, location):

        self.name = name
        self.age = age
        self.gender = gender

        # stats
        self.str = stats['str']  # strength
        self.dex = stats['dex']  # dexterity
        self.con = stats['con']  # constitution
        self.int = stats['int']  # intelligence
        self.wis = stats['wis']  # wisdom
        self.cha = stats['cha']  # charisma

        self.inventory = [Item(**i) for i in inventory]
        self.spells = spells  # TODO imprve this definition
        self.checkpoint = checkpoint
        self.location = location
        self.saving_throw_counter = 0

    def __str__(self):
        return f'{self.name}'
    
    def __repr__(self) -> str:
        return f'{self.name}'

    def list_inventory(self):
        for item in self.inventory:
            print(f'{item.name} - {item.count}')


class NPC(Character):
    def __init__(self, name, age, gender, stats, inventory, spells, checkpoint, location, job, home):
        super().__init__(name, age, gender, stats, inventory, spells, checkpoint, location)
        self.job = job
        self.home = home


class Player(Character):
    def __init__(self, name, age, gender, stats, inventory, spells, checkpoint, location):
        super().__init__(name, age, gender, stats, inventory, spells, checkpoint, location)

        self.total_weight = sum([i.weight*i.count for i in self.inventory])
        self.stats =['exp'] #Experience /  level  # level cap is 20 / exp 3550
