import os

def get_name():
    os_name = os.getlogin()
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
        age = int(input1)
        input2 = input('You entered ' + str(age) + '. Is that correct? (y/n): ').upper()
        if input2 == 'Y' or input2 == 'YES':
            gender(player_name, age)
        elif input2 == 'N' or input2 == 'NO':
            age(player_name)
        else:
            print('Invalid input. Please enter "y" or "n".')
            age(player_name)
    else:
        print('Invalid input. Please enter a valid age (numeric value).')
        age(player_name)

def gender(player_name, age):
    input1 = input('What is your gender? ')
    if input1.lower() in ['male', 'female', 'other']:
        player_gender = input1.lower()
        input2 = input('You entered ' + player_gender + '. Is that correct? (y/n): ').upper()
        if input2 == 'Y' or input2 == 'YES':
            # Proceed with the next steps or data handling based on the player's age, gender, and name
            print('Player name:', player_name)
            print('Player age:', age)
            print('Player gender:', player_gender)
            data_dump(player_name, age, player_gender)
        elif input2 == 'N' or input2 == 'NO':
            gender(player_name, age)
        else:
            print('Invalid input. Please enter "y" or "n".')
            gender(player_name, age)
    else:
        print('Invalid input. Please enter a valid gender (male, female, or other).')
        gender(player_name, age)

def data_dump(player_name, age, gender):
    # Perform the necessary data dump or save the player's information to a file
    print('Data dump completed.')


