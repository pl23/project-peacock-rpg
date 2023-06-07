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
        print ('not coded yet')

def new_game():
    import new
    new.get_name()
    
    import chapter_1
    chapter_1.load_json()


