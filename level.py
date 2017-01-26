class PlayerChoice:
    def __init__(self, configuration_options):
        self.choice_descript = configuration_options['description']
        self.next_level = configuration_options['next_level']

class Level:
    def __init__(self, level_config):
        self.level_description = level_config['description']
        self.decisions = []

        for option in level_config['options']:
            self.decisions.append(PlayerChoice(option))
