class Player:
    def __init__(self, name, backpack):
        self.name = name
        self.backpack = backpack
        items = 0
    def add_item(self, new_item):
        self.backpack.append(new_item)
    def list_items(self):
        for i in self.backpack:
            print(i)
