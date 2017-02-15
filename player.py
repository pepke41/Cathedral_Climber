class Player:
    def __init__(self, name, backpack):
        self.name = name
        self.backpack = backpack
    def add_item(self, new_item):
        self.backpack.append(new_item)
    def list_items(self):
        return self.backpack;
    def get_name(self):
        return self.name
    def check_item(self, item):
        if item in self.backpack:
            return True
        else:
            return False
