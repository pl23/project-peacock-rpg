from Characters.characters import Player, Enemy, NPC, Boss
from Maps.Map_1 import Map
from GameManager import GameManager
from settings import Settings

class Main:

    def __init__(self):
        self.player = Player()
        self.map = Map()
        self.settings = Settings()
        self.GameManager = GameManager()
        self.GameManager.run()   
        pass


if __name__ == "__main__":
    main = Main()

