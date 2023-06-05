# main.py

def display_main_menu():
    menu = """
=== Main Menu ===
1. Load Game
2. New Game
3. Exit
"""
    print(menu)

def main():
    while True:
        display_main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            load_game()
        elif choice == "2":
            new_game()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

    print("Exiting the game.")

if __name__ == "__main__":
    main()


def initialize_game():
    # Initialize the game here
    print("Game initialized")

def show_main_menu():
    # Display the main menu options and handle user input
    print("Main menu displayed")

def start_game():
    # Start the game and execute the main game loop
    print("Game started")

if __name__ == "__main__":
    initialize_game()
    show_main_menu()
    start_game()
