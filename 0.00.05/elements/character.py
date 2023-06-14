class Character:
    def __init__(self, name, race, character_class, experience_points):
        self.name = name
        self.race = race
        self.character_class = character_class
        self.experience_points = experience_points
        self.ability_scores = {
            'Strength': 0,
            'Dexterity': 0,
            'Constitution': 0,
            'Intelligence': 0,
            'Wisdom': 0,
            'Charisma': 0
        }
        self.hit_points = {'current': 0, 'maximum': 0}
        self.skills = {
            'Acrobatics': 0,
            'Animal Handling': 0,
            'Arcana': 0,
            'Athletics': 0,
            'Deception': 0,
            'History': 0,
            'Insight': 0,
            'Intimidation': 0,
            'Investigation': 0,
            'Medicine': 0,
            'Nature': 0,
            'Perception': 0,
            'Performance': 0,
            'Persuasion': 0,
            'Religion': 0,
            'Sleight of Hand': 0,
            'Stealth': 0,
            'Survival': 0
        }
        self.features_traits = []
        self.alignment = ''
        self.proficiency_bonus = 0


class Player(Character):
    def __init__(self, name, race, character_class, experience_points):
        super().__init__(name, race, character_class, experience_points)
        self.background = ''


class NPC(Character):
    def __init__(self, name, race, character_class, experience_points, npc_type):
        super().__init__(name, race, character_class, experience_points)
        self.npc_type = npc_type
        self.shopkeeper = False
        self.manager = False
        # Add more attributes specific to NPCs
        # For example:
        # self.occupation = ''
        # self.dialogue = ''
        # self.inventory = []
        # self.quest = ''
        # ...

class ObjectCharacter:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def interact(self):
        # Implement interaction logic for the object character
        pass

    def examine(self):
        # Implement examination logic for the object character
        pass
