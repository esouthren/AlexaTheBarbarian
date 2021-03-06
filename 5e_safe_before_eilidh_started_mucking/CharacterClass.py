import random
import json
import urllib.request


class Stat:
    def __init__(self, name):
        self.name = name
        self.modifier = 0
        self.ability_score = 0
        self.saving_throw = 0
        self.proficiency_bonus = 2


class CharacterClass:
    def __init__(self):
        self.name_character = ""
        self.name_player = ""
        self.race = "" #assign speed, size
        self.class_type = "" #define hit die
        self.background = ""
        self.alignment = ""
        self.eyes = ""
        self.size = ""
        self.weight = ""
        self.eyes = ""
        self.skin = ""
        self.hair = ""
        self.age = ""
        self.stats = []
        stat_names = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
        for s in stat_names:
            self.stats.append(Stat(s))
        self.hit_die = 0
        self.speed = 0
        self.size = ""
        self.prof1 = ""
        self.prof2 = ""
        self.hit_point = 0
        self.armor = ""
        self.weapon = ["", ""]
        self.armor_class = 0


    def print_character_sheet(self):
        output = ""
        output += "Player Name: {}".format(self.name_player)
        output += "\nCharacter Name: {}".format(self.name_character)
        output += "\nAge: {}".format(self.age)
        output += "\nRace: {}".format(self.race)
        output += "\tSpeed: {} \tSize: {}".format(self.speed, self.size)
        output += "\nClass: {}".format(self.class_type)
        output += "\nHit dice: {}".format(self.hit_die)
        output += "\nMaximum Hit Point: {}".format(self.hit_point)
        output += "\nBackground: {}".format(self.background)
        output += "\nAlignment: {}".format(self.alignment)
        output += "\nEyes: {}".format(self.eyes)
        output += "\nHair: {}".format(self.hair)
        output += "\nSkin: {}".format(self.skin)
        for s in self.stats:
            output += "\n{}:\t{}\tModifier: {}".format(s.name, s.ability_score, s.modifier)
        output += "\nSaving Throws:"
        for s in self.stats:
            output += "\n\t{}:\t{}".format(s.name, s.saving_throw)
        output += "\nSkills: {}, {}".format(self.prof1, self.prof2)
        output += "\nWeapons: {}\t{}".format(self.weapon[0], self.weapon[1])
        output += "\nArmor: {}".format(self.armor)
        output += "\nArmor Class: {}".format(self.armor_class)
        print(output)

    def generate_stats(self):
        roll = [0, 0, 0, 0]
        for i in range(len(roll)):
            roll[i] = random.randint(1, 6)

        min_pos = 0
        for i in range(1, 3):
            if roll[i] < roll[min_pos]:
                min_pos = i

        self.stat = 0
        for i in range(len(roll)):
            if i != min_pos:
                self.stat += roll[i]

        return self.stat





