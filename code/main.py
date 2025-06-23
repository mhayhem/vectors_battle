from figthers_class import Figthers as fc
import random

types_fighters = [
    lambda: fc("infantry", 40, 6, 4),
    lambda: fc("calvary", 60, 8, 6),
    lambda: fc("catapult", 80, 10, 8),
]


def created_army(types_fighters):
    army_1 = []
    army_2 = []
    for i in range(10):
        fighter_1 = random.choice(types_fighters)() # this creates a different instance
        army_1.append(fighter_1)
        fighter_2 = random.choice(types_fighters)()
        army_2.append(fighter_2)
        
    return select_fighters(army_1, army_2)

def select_fighters(army_1, army_2):
    # take first element of array as fighters
    fighter_1 = army_1.pop(0)
    fighter_2 = army_2.pop(0)
    
    return battle(fighter_1, fighter_2, army_1, army_2)

def battle(fighter_1, fighter_2, army_1, army_2):
    # define each fighter´s damage
    damage_1 = fighter_1.attack - fighter_2.defense
    damage_2 = fighter_2.attack - fighter_1.defense
    winner = None

    while fighter_1.life > 0 and fighter_2.life > 0:
        fighter_1.life -= damage_2
        fighter_2.life -= damage_1
    
    # checking the rest of life and add to him army if winner combat
    if fighter_2.life <= 0:
        army_1.append(fighter_1)
    elif fighter_1.life <= 0:
        army_2.append(fighter_2)
    return checking_len_army(army_1, army_2)

def checking_len_army(army_1, army_2):
    # checking that are not empty list
    if len(army_1) <= 0:
        return f"Winner is Army 2"
    elif len(army_2) <= 0:
        return f"Winner Army 1"
    else:
        # if aren´t empty recursive the battle
        return select_fighters(army_1, army_2)

def main():
    return created_army(types_fighters)

print(main())