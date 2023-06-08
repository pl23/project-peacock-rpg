import sys
from menu import Menu
class GameManager():
    def __init__(self):
        self.menu = Menu()
        pass
    def run(self):
        self.onMenuSelect(self.menu.main_menu())

        pass
    def new_game(self):
        pass
    def load_game(self):
        pass
    def settings(self):
        pass
    def exit(self):
        #end game
        sys.exit()



    def onMenuSelect(self, menu):
        if menu == 'New Game':
            self.new_game()
        elif menu == 'Load Game':
            self.load_game()
        elif menu == 'Settings':
            self.settings()
        elif menu == 'Exit':
            self.exit()
        else:
            print('Invalid Input')
            self.menu.main_menu()
        pass
