import random
import sqlite3

from character_sheet import character_sheet
import stats


"""Set class related features, proficiencies, etc."""

def get_class_skills():
    """Gets the list of skills a class can have proficiency in"""
    pass

def get_class_saving_throw():
    """Gets the class proficiency for saving throws"""
    pass

def multiclass():
    """Determines if a character is able to multiclass and sets the second class"""
    #TODO: Make multiclassing toggleable
    #TODO: Set limit to multiclassing
    #TODO: Make multiclassing limit toggleable
    set_class()
    if character_sheet["level"][0] > 1 and character_sheet["level"][0] < 20:
        heads_or_tails = random.randint(1,2)
        if heads_or_tails == 1:
            set_class()
            stats.set_multiclass_level()

def set_class():
    """Randomly selects a class from the list of available classes"""
    classes = ["Artificer", "Barbarian", "Bard", "Blood Hunter", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
    if character_sheet["class"]:
        classes.remove(character_sheet["class"][0])
        character_sheet["class"] += [random.choice(classes)]
    else:
        character_sheet["class"] = [random.choice(classes)]

def set_class_skills():
    """Randomly chooses from the list of class skills which ones they are proficient in"""
    pass