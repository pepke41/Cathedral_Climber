import yaml
from player import Player
from level import Level
from level import PlayerChoice

print("Hello adventurer, welcome to Cathedral Climber")
player_name = raw_input("What is your name?\n")
backpack = ["textbook", "pens"]
levels = []
level_index = 0

with open("text.yaml", 'r') as stream:
    try:
        level_data = yaml.load(stream)
        for i in level_data["levels"]:
            levels.append(Level(i))
    except yaml.YAMLError as exc:
        print(exc)
print(levels[level_index].level_description)

