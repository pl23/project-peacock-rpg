class Menu():
    def __init__(self):
        pass
    def main_menu(self):
        print('''
        1. New Game
        2. Load Game
        3. Settings
        4. Exit
        ''')
        menu = input('Select an option: ')
        if menu == '1':
            print('New Game')
        elif menu == '2':
            print('Load Game')
        elif menu == '3':
            print('Settings')
        elif menu == '4':
            print('Exit')
        else:
            print('Invalid Input')
            self.main_menu()