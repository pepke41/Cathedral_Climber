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
valid_match = True
while level_index != -1 and level_index != 'end' and valid_match:
    level_index = int(level_index)
    print(levels[level_index].level_description)
    choice = raw_input()
    valid_match = False
    for i in levels[level_index].decisions:
        if choice.lower() == i.choice_descript:
            level_index = i.next_level
            valid_match = True

if valid_match == false or level_index == -1:
    print('GAME OVER')
else:
    #if envelope give hint
    print('This is it. The final battle. You see a jail cell, inside are all the defencers. \"Help us!!\" You wander over to the cage and see that there is a screen with a final riddle. If you answer correctly, you will release the defenders and save the day, but if you fail, the cell will self destruct. No pressure')
    print('It is in the rock, but not in the stone; It is in the marrow, but not in the bone; It is in the bolster, but not in the bed; It is not in the living, nor yet in the dead. Answer with one word only')
    choice = raw_input()
    if choice.lower() == 'r':
        print('The door unlocks, you\'ve saved the day!!!')
    else:
        print('GAME OVER')
