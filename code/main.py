from figthers_class import Figthers as fc
import random

infantry = fc(40, 6, 4)
calvary = fc(60, 8, 6)
catapult = fc(80, 10, 8)

types_fighters = [infantry, calvary, catapult]


def created_army(list_figthers):
    army_1 = []
    army_2 = []
    for i in range(10):
        fighter = random.choice(types_fighters)
        army_1.append(fighter)
        fighter = random.choice(types_fighters)
        army_2.append(fighter)
    return select_fighters(army_1, army_2)

def select_fighters(army_1, army_2):
    # take first element of array as fighters
    figther_1 = army_1.pop(0)
    figther_2 = army_2.pop(0)
    

