import getpass
import json


def os_get_name():
    os_name = getpass.getuser()
    os_name_ask = input('Do you want ' + os_name + ' as your name? (y/n): ').upper()
    if os_name_ask == 'Y' or os_name_ask == 'YES':
        name_confrom1 = input('Are you sure you want ' + os_name + ' as your name? (y/n): ').upper()
        if name_confrom1 == 'Y' or name_confrom1 == 'YES':
            player_name = os_name
            return player_name
        elif name_confrom1 == 'N' or name_confrom1 == 'NO':
            os_get_name()
        else:
            print('Invalid input. Please enter "y" or "n".')
        os_get_name()
    elif os_name_ask == 'N' or os_name_ask == 'NO':
        get_name()
    
    else:
        print('Invalid input. Please enter "y" or "n".')
        os_get_name()

def get_name():
    input_name = input('what is name :')
    name_ask = input('Do you want ' + input_name + ' as your name? (y/n): ').upper()
    if name_ask == 'Y' or name_ask == 'YES':
        name_confrom1 = input('Are you sure you want ' + input_name + ' as your name? (y/n): ').upper()
        if name_confrom1 == 'Y' or name_confrom1 == 'YES':
            player_name = input_name
            return player_name
        elif name_confrom1 == 'N' or name_confrom1 == 'NO':
            os_get_name()
        else:
            print('Invalid input. Please enter "y" or "n".')
        os_get_name()
    elif name_ask == 'N' or name_ask == 'NO':
        os_get_name()
    
    else:
        print('Invalid input. Please enter "y" or "n".')
        os_get_name()



def age(player_name):
    input1 = input('How old are you? ')
    if input1.isdigit():
        age1 = int(input1)
        input2 = input('You entered ' + str(age1) + '. Is that correct? (y/n): ').upper()
        if input2 == 'Y' or input2 == 'YES':
            gender(player_name, age1)
        elif input2 == 'N' or input2 == 'NO':
            age(player_name)
        else:
            print('Invalid input. Please enter "y" or "n".')
            age(player_name)
    else:
        print('Invalid input. Please enter a valid age (numeric value).')
        age(player_name)


def gender(player_name, age1):
    input1 = input("What is your gender?['male', 'female', 'other'] ")
    if input1.lower() in ['male', 'female', 'other']:
        player_gender = input1.lower()
        input2 = input('You entered ' + player_gender + '. Is that correct? (y/n): ').upper()
        if input2 == 'Y' or input2 == 'YES':
            tutorial_F(player_name, age1,player_gender)
        elif input2 == 'N' or input2 == 'NO':
            gender(player_name, age1)
        else:
            print('Invalid input. Please enter "y" or "n".')
            gender(player_name, age1)
    else:
        print('Invalid input. Please enter a valid gender (male, female, or other).')
        gender(player_name, age1)


def tutorial_F (player_name, age1,player_gender):
    input1 = input('Do you need a tutorial[y/n]').upper()
    if input1 == 'Y' or input1 == 'YES':
        input2 = input ('are you shore about this[y/n]').upper()
        if input2 == 'Y' or input2 == 'Yes':
            tutorial = True
            data_gen(player_name, age1,player_gender,tutorial)
        else:
            tutorial_F(player_name, age1,player_gender)   
    elif input1 == 'N' or input1 == 'No':
        input2 = input ('are you shore about this[y/n]').upper()
        if input2 == 'Y' or input2 == 'Yes':
            tutorial = False
            data_gen(player_name, age1,player_gender,tutorial)
        else:
            tutorial_F(player_name, age1,player_gender)    


def data_gen(player_name, age1,player_gender,tutorial):
    data = {
        'player_info': {
            'player_name': player_name,
            'player_age': age1,
            'player_gender': player_gender,
            'Player_location':None
        },'player_stats':{

        },'player_invtory':{

        },'player_spals':{
            'spals_unlock':{},'spals_equped':{}
        },'check_ponts':{
            'tutorial': tutorial
        }
    }
    data_dump(data)


def data_dump(data):
    print ('saving')
    file_path = '0.00.05/data/' + 'player_' + data['player_info']['player_name'] + '_save.json'
    with open(file_path, 'w') as file:
        json.dump(data, file)
    print ('saving conpleat')
    import chapter_1 as chapter_1
    selected_Save = '0.00.05/data/' + 'player_' + data['player_info']['player_name'] + '_save.json'
    chapter_1.load_json(selected_Save)

    
os_get_name()