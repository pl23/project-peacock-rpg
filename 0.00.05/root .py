

def get_input ():
    input ('project-peacock-rpg \n press enter:')
    input1 = input ('1)new game \netc:')
    check = input1.isdigit()
    if check == False:
        print ('invald input')
        get_input()
    else:
        input1 = int(input1)
    if input1 == 1:
        import new
        new.get_name()
get_input()
