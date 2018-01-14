import math
import random
from CharacterClass import *

hit_die = []
speed = []
size = []
proficiency = []
ab_bon = []
classes = []
races = []
skills = []
ab_mod = [1, 4, 3, 0, 5, 3, 4, 5, 3, 4, 3, 4, 5, 5, 3, 1, 1, 4] #stats based on index str=0, dex=1, con=2 etc #for skills mods
alignment = {"Dwarf": "Lawfully Good",
             "Elf": "Chaotic Good",
             "Halfling": "Lawfully Good",
             "Human": "Neutral",
             "Dragenborn": "Neutral Good",
             "Gnome": "Chaotic Good",
             "Half-Elf": "Chaotic Good",
             "Half-Orc": "Chaotic Evil",
             "Tieflieng": "Chaotic Neutral"}

new_character = CharacterClass()
from APICalls import API
API = API()
API.get_classes()
API.get_races()
API.get_skills()

for c in API.classes:
    hit_die = c['hit_die']
    classes.append(c['name'])
for c in API.races:
    races.append(c['name'])
    speed = c['speed']
    size = c['size']
    ab_bon = c['ability_bonuses']
    size = c['size']
for c in API.skills:
    new_character.skills.append(c['name'])

new_character.name_player = input("What is your Name? (the real one)")
lines = open('Names.txt').read().splitlines()
new_character.name_character = random.choice(lines)


"""new_character.name_player = input("What is your Name? (the real one)")
new_character.name_character = input("What is your Character Name?")
new_character.sex = input("Specify your sex:")"""

#select class

"""print("Select your class from:")
for c in API.classes:
    if c['name'] != 'Monk':
        print(c['name'])"""
#new_character.class_type = input("What is your Class?")

#generate class
new_character.class_type = random.choice(classes)
while new_character.class_type == 'Monk':
    new_character.class_type = random.choice(classes)

#get proficiencies based in class
for c in API.classes:
    if new_character.class_type == c['name']:
        new_character.hit_die = c['hit_die']
        for p in c['proficiency_choices'][0]['from']:
            prof = p['name']
            prof = prof[7:]
            proficiency.append(prof)

new_character.prof1 = random.choice(proficiency)
new_character.prof2 = random.choice(proficiency)
while new_character.prof2 == new_character.prof1:
    new_character.prof2 = random.choice(proficiency)

#select race
"""print("Select your race from:")
for c in API.races:
    print(c['name'])
new_character.race = input("What is your Race?")"""

new_character.race = random.choice(races)
for c in API.races:
    if new_character.race == c['name']:
        new_character.speed = c['speed']
        new_character.size = c['size']
        new_character.ab_bon = c['ability_bonuses']
        size = c['size']

#new_character.background = input("What is your Background?")

for index, s in enumerate(new_character.stats):
    s.ability_score = new_character.generate_stats()
    s.ability_score += ab_bon[index]
    s.modifier = math.trunc((s.ability_score - 10)/2)
    s.saving_throw = s.modifier + ab_bon[index]
    if s.name == "CON":
        new_character.hit_point = new_character.hit_die + s.ability_score

for index,s in enumerate(ab_mod):
    new_character.skills_mod.append(new_character.stats[s].modifier)
    if new_character.skills[index] == new_character.prof1 or new_character.skills[index] == new_character.prof2:
        new_character.skills_mod[index] += 2

new_character.age = random.randint(16,100)

for key, value in alignment.items():
    if key == new_character.race:
        new_character.alignment = value
        break

#print character sheet
print(new_character.print_character_sheet())


run(new_character)