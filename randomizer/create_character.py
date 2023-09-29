import character_class
from character_sheet import character_sheet
import stats


"""
Main file to call all other files
Runs through methods throughout the project in a specific order so characters are created properly
#TODO: Add logic here for selecting which aspects of character creation to randomize/auto-generate (i.e. choosing a specific level or class)
#TODO: Add logic here to choose which game rules to follow (i.e. dnd or pathfinder)
"""

stats.roll_stats()
stats.set_level()
character_class.multiclass()
stats.set_alignment()
stats.set_initiative()
stats.set_proficiency_bonus()
print(character_sheet)
