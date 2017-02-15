class PlayerChoice:
    def __init__(self, configuration_options):
        self.choice_descript = configuration_options['description']
        self.next_level = configuration_options['next_level']

class Level:
    def __init__(self, level_config):
        self.level_description = level_config['description']
        self.level_item = level_config['item']
        self.required_item = level_config['required_item']
        self.decisions = []
        for option in level_config['options']:
            self.decisions.append(PlayerChoice(option))
    def check_item(self):
        if self.level_item == 'none':
            return False
        else:
            return True
    def get_item(self):
        return self.level_item
