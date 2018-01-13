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


    def print_character_sheet(self):
        output = ""
        if (self.name_player != ""):
            output += "Player Name: {}".format(self.name_player)
        if (self.name_character != ""):
            output += "\nCharacter Name: {}".format(self.name_character)
        if (self.race != ""):
            output += "\nRace: {}".format(self.race)
        if (self.class_type != ""):
            output += "\nClass: {}".format(self.class_type)
        if (self.background != ""):
            output += "\nBackground: {}".format(self.background)
        if (self.alignment != ""):
            output += "\nAlignment: {}".format(self.alignment)
        print(output)