from CharacterClass import *

new_character = CharacterClass()

new_character.name_player = input("What is your Name? (the real one)")
new_character.name_character = input("What is your Character Name?")
new_character.sex = input("Specify your sex:")
new_character.class_type = input("What is your Class?")
new_character.race = input("What is your Race?")
new_character.background = input("What is your Background?")
new_character.alignment = input("What is your Alignment?")
print(new_character.print_character_sheet())






