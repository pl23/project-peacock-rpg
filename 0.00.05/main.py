

def get_input ():
    input ('project-peacock-rpg \n press enter:')
    input1 = input ('1)new game \n2)lode game \netc:')
    check = input1.isdigit()
    if check == False:
        print ('invald input')
        get_input()
    else:
        input1 = int(input1)
    if input1 == 1:
        new_game()
    elif input1 == 2:
        lode_game()


def new_game():
    import new_player
    new_player.main()

def lode_game():
    import old_player
    old_player.main()


get_input()