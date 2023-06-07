import json

def load_json(selected_Save):
    with open(selected_Save, 'r') as file:
        data = json.load(file)
    return data

def seen_T(data):
    if data["check_ponts"]["tutorial"] == True:
        print ('not coded yet ')


    seen_1(data)
    
def seen_1(data):

#Dictionary location tracker code goes here

    input('???: character dialogue goes here[press [enter]]')
    input('???: character dialogue goes here[press [enter]]')
    input('???: character dialogue goes here[press [enter]]')
    input('???: character dialogue goes here[press [enter]]')
    input('???: character dialogue goes here[press [enter]]')
