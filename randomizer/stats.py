import math
import random
import sqlite3

from character_sheet import character_sheet

"""
Sets or updates most numerical portions of the typical DnD character sheet including
level, ability scores, saving throws, skill modifiers, armor class, initiative, speed, and hit points
Pulls from necessary databases to update stats properly such as ability score increases based on race
"""

def ability_increase_level_up():
    """Ability score increase for leveling up, depending on class
    Generally includes +1 to any ability at level 4, 8, 12, and 16
    +2 to any ability score or +1 to any two ability scores at level 19
    Can't go above 20 due to ability increase"""
    pass

def armor_class():
    """Sets AC based on dex modifier and equipment"""
    pass

def get_ability_modifier(ability):
    modifier = math.floor((character_sheet["stats"][ability] - 10)/2)
    return modifier

def modern_racial_ability_increase():
    """+2 to any stat and +1 to another, or +1 to three stats
    Can't go above 20 due to ability increase"""
    pass

def modify_initiative():
    """Updates initiative modifier depending on class, feats, race, etc."""
    pass

def racial_plus_one_increase():
    """Some races get a defined +2 and then allow for +1 to any other stat."""
    pass

def roll_hit_points():
    """Max hit points for level 1
    Roll per level (class die + con modifier)"""
    pass

def roll_stats():
    """Roll 4d6 take the highest 3"""
    #TODO: Make results selectable per stat instead of assigning in order
    for stat in character_sheet["stats"]:
        rolls = []
        roll_1 = random.randint(1,6)
        roll_2 = random.randint(1,6)
        roll_3 = random.randint(1,6)
        roll_4 = random.randint(1,6)
        rolls.extend((roll_1, roll_2, roll_3, roll_4))
        rolls.sort()
        rolls.pop(0)
        total = sum(rolls)
        character_sheet["stats"][stat] = total

def set_alignment():
    """Not a stat but easier to include here. Sets alignment based on classic alignment square chart"""
    alignments = ["Lawful Good", "Lawful Neutral", "Lawful Evil", "Neutral Good", "True Neutral", "Neutral Evil", "Chaotic Good", "Chaotic Neutral", "Chaotic Evil"]
    character_sheet["alignment"] = random.choice(alignments)

def set_initiative():
    """Sets base initiative using dex modifier"""
    character_sheet["initiative"] = get_ability_modifier("dexterity")

def set_level():
    """Set random character level from 1 to 20"""
    level = random.randint(1,20)
    character_sheet["level"] = [level]
    character_sheet["hit dice"] = level

def set_multiclass_level():
    level_cap = 20 - character_sheet["level"][0]
    character_sheet["level"].append(random.randint(1, level_cap))
    character_sheet["hit dice"] = character_sheet["level"][0] + character_sheet["level"][1]

def set_proficiency_bonus():
    """Proficiency bonus determined by level
    Divide by 4, round up, add 1"""
    total = 0
    for level in character_sheet["level"]:
        total += level
    bonus = math.ceil(total/4) + 1
    character_sheet["proficiency bonus"] = bonus

def set_saving_throws():
    """Determined by ability modifiers and class proficiency"""
    pass

def set_skill_modifiers():
    """Sets skill modifiers based on ability scores and class proficiencies"""
    pass

def set_speed():
    """Determined by selected race"""
    pass
