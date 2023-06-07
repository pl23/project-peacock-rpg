import os
import json

def get_name():
    #os_name = os.getlogin()
    os_name = "gabe"
    #note this place holder untel i can get os.getlogin to work
    input1 = input('Do you want ' + os_name + ' as your name? (y/n): ').upper()
    if input1 == 'Y' or input1 == 'YES':
        input2 = input('Are you sure you want ' + os_name + ' as your name? (y/n): ').upper()
        if input2 == 'Y' or input2 == 'YES':
            player_name = os_name
            age(player_name)
        elif input2 == 'N' or input2 == 'NO':
            input3 = input('What is your name? ')
            input4 = input('Are you sure you want ' + input3 + ' as your name? (y/n): ').upper()
            if input4 == 'Y' or input4 == 'YES':
                player_name = input3
                age(player_name)
            elif input4 == 'N' or input4 == 'NO':
                get_name()
            else:
                print('Invalid input. Please enter "y" or "n".')
                get_name()
        else:
            print('Invalid input. Please enter "y" or "n".')
            get_name()
    elif input1 == 'N' or input1 == 'NO':
        input5 = input('What is your name? ')
        input6 = input('Are you sure you want ' + input5 + ' as your name? (y/n): ').upper()
        if input6 == 'Y' or input6 == 'YES':
            player_name = input5
            age(player_name)
        elif input6 == 'N' or input6 == 'NO':
            get_name()
        else:
            print('Invalid input. Please enter "y" or "n".')
            get_name()
    else:
        print('Invalid input. Please enter "y" or "n".')
        get_name()

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
            # Proceed with the next steps or data handling based on the player's age, gender, and name
            print('Player name:', player_name)
            print('Player age:', age1)
            print('Player gender:', player_gender)
            data_gen(player_name, age1,player_gender)
        elif input2 == 'N' or input2 == 'NO':
            gender(player_name, age1)
        else:
            print('Invalid input. Please enter "y" or "n".')
            gender(player_name, age1)
    else:
        print('Invalid input. Please enter a valid gender (male, female, or other).')
        gender(player_name, age1)

def data_gen(player_name, age1, player_gender):
    data = {
        'player_info': {
            'player_name': player_name,
            'player_age': age1,
            'player_gender': player_gender
        }
    }
    data_dump(data)

def data_dump(data):
    print ('saving')
    directory = '0.00.05/data/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = directory + 'player_' + data['player_info']['player_name'] + '_save.json'
    with open(file_path, 'w') as file:
        json.dump(data, file)
    print ('saving conpleat')
get_name()