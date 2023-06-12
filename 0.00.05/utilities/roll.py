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

    return int(die), int(sided), advantage

def roll(die=None, sided=None, dice_effect=None, display_result=True, advantage=None, proficiency_bonus=0):
    if not die and not sided and not dice_effect:
        raise ValueError("No input provided. Please specify die and sided values or dice_effect.")

    if dice_effect:
        die, sided, advantage = split_dice_effect(dice_effect)
    else:
        advantage = advantage

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

# Testing the roll function with direct values and proficiency bonus
roll(2, 6, proficiency_bonus=2)

# Testing the roll function with '1d6' as the dice_effect and proficiency bonus
roll(dice_effect='1d6', proficiency_bonus=-1)

# Testing the roll function with advantage in the string and proficiency bonus
roll(dice_effect='A1d6', proficiency_bonus=3)

# Testing the roll function with disadvantage in the string and proficiency bonus
roll(dice_effect='D1d6', proficiency_bonus=0)

# Testing the roll function with separate die and sided values, advantage, and proficiency bonus
roll(die=1, sided=6, advantage='A', proficiency_bonus=2)

# Testing the roll function with separate die and sided values, disadvantage, and proficiency bonus
roll(die=1, sided=6, advantage='D', proficiency_bonus=0)
