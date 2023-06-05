def display_main_menu():
    print("=== Main Menu ===")
    print("1. Load Game")
    print("2. New Game")
    print("3. Exit")


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


def load_game():
    # Implement load game functionality
    pass


def new_game():
    # Implement new game functionality
    pass


if __name__ == "__main__":
    main()
