import getpass
import json
class main:
    
def main(): 




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
    #  |                   
    # \ /  tempory for testing  
    #  v
    main()            