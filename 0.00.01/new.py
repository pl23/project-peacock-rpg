def new_player():
    def info_get ():
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