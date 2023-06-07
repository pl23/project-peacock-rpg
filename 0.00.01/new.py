import os
def new_player():
    def info_get ():
        def name ():
            pc_user_name = os.getlogin() 
            def name_chek_os ():
                input1 = input ('do you whant ' + pc_user_name + ' as your name y/n:').upper
                if input1 == 'Y' or input1 == 'YES':
                    player_name = pc_user_name
 
                elif input1 == 'N' or input1 == 'NO':
                    player_name = input ('what is your name?')
                    name_chek()
            def name_chek ():
                input1 = input ('do you whant ' + pc_user_name + ' as your name y/n:').upper
                if input1 == 'Y' or input1 == 'YES':
                    player_name = pc_user_name
 
                elif input1 == 'N' or input1 == 'NO':
                    player_name = input ('what is your name?')
                    name_chek()

                else:
                    print ('error')
                    player_name = input ('what is your name?')
                    name_chek()
                print ('hello ' + player_name + ' !')    
        def age():    
            input1 = input ('how old are you :')
            math1 = input1.isdigit()   
            if math1 == False:
                print('error not a digit')

                conform =True
                while conform :
                    input1 = input ('a :')
                    math1 = input1.isdigit()   
                    if math1 == False:
                        print('error not a digit')
            else:

        name()
    info_get()