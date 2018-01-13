import random
import json
import urllib.request


class Stat:
    def __init__(self, name):
        self.name = name
        self.modifier = 0
        self.ability_score = 0
        self.savings_throw = 0
        self.proficiency_bonus = 2

class CharacterClass:
    def __init__(self):
        self.name_character = ""
        self.name_player = ""
        self.sex = ""
        self.race = "" #assign speed, size
        self.class_type = "" #define hit die
        self.background = ""
        self.alignment = ""
        self.eyes = ""
        self.height = ""
        self.weight = ""
        self.eyes = ""
        self.skin = ""
        self.hair = ""
        self.age = ""
        self.stats = []
        stat_names = ["STR", "DEX", "CON", "INT", "WIS", "CHAR"]
        for s in stat_names:
            self.stats.append(Stat(s))
        self.hit_die = 0
        self.speed = 0
        self.size = ""

    def print_character_sheet(self):
        output = ""
        if (self.name_player != ""):
            output += "Player Name: {}".format(self.name_player)
        if (self.name_character != ""):
            output += "\nCharacter Name: {}".format(self.name_character)
        if (self.race != ""):
            output += "\nRace: {}".format(self.race)
            output += "\tSpeed: {} \tSize: {}".format(self.speed, self.size)
        if (self.class_type != ""):
            output += "\nClass: {}".format(self.class_type)
            output += "\tHit die: {}".format(self.hit_die)
        if (self.background != ""):
            output += "\nBackground: {}".format(self.background)
        if (self.alignment != ""):
            output += "\nAlignment: {}".format(self.alignment)
        for s in self.stats:
            output += "\n{}:\t{}\tModifier: {}".format(s.name, s.ability_score, s.modifier)
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





    #def get_hit_diece(self):
