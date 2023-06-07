import os 
def os_login():
    os_name = os.getlogin()
    input1 = input(' do you want ' + os_name + 'sa you name?[y/n]').upper()
    if input1 == 'Y' or input1 == 'YES':
        input2 = input('are you shore you want ' + os_name + ' as you name ?[y/n]').upper()
        if input2 == 'Y' or input1 == 'YES':
            player_name = os_name
            age(player_name)
        else:
            get_name() 
    else:
        get_name()
def get_name():
    input1 = input('what is you name?')
    
    input2 = input('are you shore you want ' + input1 + ' as you name ?[y/n]').upper()
    if input2 == 'Y' or input2 == 'YES':
        player_name = input1
        age(player_name)
    else:
        get_name() 

def age (player_name):
    print ('not done yet')
