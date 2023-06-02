def new_player():
    def info_get ():
        def name ():
            import os
            pc_user_name = os.login() 
            input1 = input ('do you whant ' + pc_user_name + ' as your name y/n:').upper
            if input1 == 'Y' or input1 == 'YES':

            elif input1 == 'N' or input1 == 'NO':
                
            else:
                print ('error')
            def get_input ():
                
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

        age()
    info_get()
new_player()