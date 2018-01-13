import math
from CharacterClass import *

hit_die = []
speed = []
size = []

new_character = CharacterClass()
from APICalls import API
API = API()
API.get_classes()
API.get_races()
print(API.races)
print(API.classes)
for c in API.classes:
    hit_die = c['hit_die']
    proficiency = []
    for p in c['proficiency_choices'][0]['from']:
        proficiency = p['name']
        proficiency = proficiency[7:]
for c in API.races:
    speed = c['speed']
    size = c['size']

new_character.name_player = input("What is your Name? (the real one)")
new_character.name_character = input("What is your Character Name?")
new_character.sex = input("Specify your sex:")

#select class

print("Select your class from:")
for c in API.classes:
    print(c['name'])

new_character.class_type = input("What is your Class?")
for c in API.classes:
    if new_character.class_type == c['name']:
        new_character.hit_die = c['hit_die']


#select race
print("Select your race from:")
for c in API.races:
    print(c['name'])
new_character.race = input("What is your Race?")
for c in API.races:
    if new_character.race == c['name']:
        new_character.speed = c['speed']
        new_character.size = c['size']

new_character.background = input("What is your Background?")
new_character.alignment = input("What is your Alignment?")


for s in new_character.stats:
    s.ability_score = new_character.generate_stats()
    s.modifier = math.trunc((s.ability_score - 10)/2)
    s.saving_throw = s.modifier + s.proficiency_bonus

#print character sheet
print(new_character.print_character_sheet())
