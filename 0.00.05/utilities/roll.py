import random

def parse_dice_effect(dice_effect):
    dice_effect = dice_effect.strip().upper()

    if dice_effect[0] == 'D':
        advantage = False
        dice_parts = dice_effect[1:].split('D')
    elif dice_effect[0] == 'A':
        advantage = True
        dice_parts = dice_effect[1:].split('D')
    else:
        advantage = None
        dice_parts = dice_effect.split('D')

    if len(dice_parts) != 2:
        raise ValueError("Invalid dice format. Expected '1d6' format.")

    die = dice_parts[0].strip()
    sided = dice_parts[1].strip()

    if not die.isdigit() or not sided.isdigit():
        raise ValueError("Invalid dice format. Expected numeric values for die and sides.")

    return die, sided, advantage

def apply_advantage(rolls, advantage):
    if advantage is True:
        return max(rolls)
    elif advantage is False:
        return min(rolls)
    else:
        return sum(rolls)

def roll(die=None, sided=None, dice_effect=None, display_result=True, advantage=None):
    if die is None and sided is None and dice_effect is None:
        raise ValueError("No input provided. Please specify die and sided values or dice_effect.")

    if dice_effect:
        die, sided, advantage = parse_dice_effect(dice_effect)
    else:
        advantage = advantage

    if not die or not sided:
        raise ValueError("Missing die or sided value.")

    rolls = []
    for _ in range(int(die)):
        rolls.append(random.randint(1, int(sided)))

    result = apply_advantage(rolls, advantage)

    if display_result:
        print(result)

    return result
