import random

def apply_advantage(rolls, advantage):
    if advantage == "A":
        return max(rolls)
    elif advantage == "D":
        return min(rolls)
    else:
        return sum(rolls)

def apply_proficiency(result, proficiency):
    return result + proficiency

def split_dice_effect(dice_effect):
    dice_effect = dice_effect.strip()  # Remove leading/trailing whitespace

    if 'A' in dice_effect:
        parts = dice_effect.split('A')
        die, sided = parts[1].strip().split('d')
        advantage = 'A'
    elif 'D' in dice_effect:
        parts = dice_effect.split('D')
        die, sided = parts[1].strip().split('d')
        advantage = 'D'
    else:
        die, sided = dice_effect.strip().split('d')  # Strip whitespace from dice_effect
        advantage = None
    roll(int(die), int(sided), advantage)
    return 

def roll(die=None, sided=None, dice_effect=None, display_result=True, advantage=None, proficiency_bonus=0):
    if not die and not sided and not dice_effect:
        raise ValueError("No input provided. Please specify die and sided values or dice_effect.")  

    #if dice_effect:
        #die, sided, advantage = split_dice_effect(dice_effect)
    #else:
    #    advantage = advantage

    if die is None or sided is None:
        raise ValueError("Missing die or sided value.")

    rolls = []
    for _ in range(int(die)):
        rolls.append(random.randint(1, int(sided)))

    result = apply_advantage(rolls, advantage)
    result_with_proficiency = apply_proficiency(result, proficiency_bonus)

    if display_result:
        print(result_with_proficiency)

    return result_with_proficiency

def a ():
    reply = input("roll dice?(eg:1d6).>")
    split_dice_effect(reply)
        
        
 
while True:
    a()
    reply = input("continue?[Yes/No]>").upper
    if reply in ["Y","YES"]:
        continue
    elif reply in ["N","NO"]:
        break

