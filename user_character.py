import math
from character_class import *
from api_calls import API


class CharacterGen:

    def generate_character(self, username):
        new_character = CharacterClass()

        hit_die = []
        speed = []
        size = []
        proficiency = []
        new_character.ab_bon = []
        classes = []
        races = []
        new_character.skills = []
        new_character.ab_mod = [1, 4, 3, 0, 5, 3, 4, 5, 3, 4, 3, 4, 5, 5, 3, 1, 1, 4] #stats based on index str=0, dex=1, con=2 etc #for skills mods
        new_character.skills_mod = []
        alignment = {"Dwarf": "Lawful Good",
                     "Elf": "Chaotic Good",
                     "Halfling": "Lawful Good",
                     "Human": "Neutral",
                     "Dragenborn": "Neutral Good",
                     "Gnome": "Chaotic Good",
                     "Half-Elf": "Chaotic Good",
                     "Half-Orc": "Chaotic Evil",
                     "Tieflieng": "Chaotic Neutral"}
        lm_armor = {"Padded": 11,
                       "Leather": 11,
                       "Studded leather": 12,
                       "Hide": 12,
                       "Chain Shirt": 13,
                       "Scale Mail": 14,
                       "Breastplate": 14,
                       "Half Plate": 15}
        heavy_armor = {"Ring Mail": 14,
                       "Chain Mail": 16,
                        "Splint": 17,
                        "Plate": 18}
        shield = {"Shield": 2}
        equipment = []
        weapons = ["",""]
        arm = []
        misc = []

        web_data = API()


        for c in web_data.classes:
            hit_die = c['hit_die']
            classes.append(c['name'])
        for c in web_data.races:
            races.append(c['name'])
            speed = c['speed']
            size = c['size']
            new_character.ab_bon = c['ability_bonuses']
            size = c['size']
        for c in web_data.skills:
            new_character.skills.append(c['name'])
        for c in web_data.equipment:
            equipment.append(c)

        new_character.name_player = username

        lines = open('Names.txt').read().splitlines()
        new_character.name_character = random.choice(lines)

        #generate class
        new_character.class_type = random.choice(classes)
        while new_character.class_type == 'Monk':
            new_character.class_type = random.choice(classes)

        #get proficiencies based in class
        i = 0
        for c in web_data.classes:
            if new_character.class_type == c['name']:
                class_index = i
                new_character.hit_die = c['hit_die']
                for p in c['proficiency_choices'][0]['from']:
                    prof = p['name']
                    prof = prof[7:]
                    proficiency.append(prof)
            i += 1

        #equipment
        for i in range(0, 37):
            weapons.append(equipment[i])
        for i in range(38,50):
            arm.append(equipment[i])


        new_character.weapon[0] = random.choice(weapons)
        new_character.weapon[1] = random.choice(weapons)
        while new_character.weapon[0] == new_character.weapon[1]:
            new_character.weapon[1] = random.choice(weapons)
        new_character.armor = random.choice(arm)
        for key, value in lm_armor.items():
            if new_character.armor == key:
                new_character.armor_class = value + new_character.stats[1].modifier
        for key, value in heavy_armor.items():
            if new_character.armor == key:
                new_character.armor_class = value

        new_character.prof1 = random.choice(proficiency)
        new_character.prof2 = random.choice(proficiency)
        while new_character.prof2 == new_character.prof1:
            new_character.prof2 = random.choice(proficiency)

        #select race
        new_character.race = random.choice(races)
        for c in web_data.races:
            if new_character.race == c['name']:
                new_character.speed = c['speed']
                new_character.size = c['size']
                new_character.ab_bon = c['ability_bonuses']
                size = c['size']

        #stats
        for index,s in enumerate(new_character.stats):
            s.ability_score = new_character.generate_stats()
            s.ability_score += new_character.ab_bon[index]
            s.modifier = math.trunc((s.ability_score - 10)/2)
            s.modifier = s.modifier + new_character.ab_bon[index]
            if new_character.ab_bon != 0:
                s.saving_throw = s.modifier + 2
            else:
                s.saving_throw = s.modifier

            if s.name == "CON":
                new_character.hit_point = new_character.hit_die + s.ability_score

        #skills
        for index,s in enumerate(new_character.ab_mod):
            new_character.skills_mod.append(new_character.stats[s].modifier)
            if new_character.skills[index] == new_character.prof1 or new_character.skills[index] == new_character.prof2:
                new_character.skills_mod[index] += 2

        #alignment
        for key, value in alignment.items():
            if key == new_character.race:
                new_character.alignment = value
                break

        #appearance
        skin = ["Olive", "Pail", "Dark"]
        eye = ["Blue", "Brown", "Red", "Stormy", "Frightened", "Troubled", "Amazed", "Naive", "Green", "Dark", "Deep Blue", "Yellow", "Black", "Gold", "See-Green", "Cosmic", "Dead", "Purple", "Tuirquoise"]
        hair_color = ["Red", "Dark Brown", "Blond", "Grey", "Black", "Light Brown", "Olive", "Orange"]
        hair_style = ["Short", "Long", "Wild", "Messy", "Braided", "Dirty", "Shaved", "Mohawk", "Bowl-cut"]
        new_character.skin = random.choice(skin)
        new_character.eyes = random.choice(eye)
        new_character.hair = random.choice(hair_style) + ' ' + random.choice(hair_color)
        new_character.age = random.randint(16,100)
        #print character sheet
        print(new_character.print_character_sheet())

        return new_character