import yaml
from level import Level, PlayerChoice
class TestLevels:
    def test_valid_description(self):
        levels = []
        with open("test.yaml", 'r') as stream:
            try:
                level_data = yaml.load(stream)
                for i in level_data["levels"]:
                    levels.append(Level(i))
            except yaml.YAMLError as exc:
                print(exc)
        assert levels[0].level_description == "this is a test"

    def test_items(self):
        levels = []
        with open("test.yaml", 'r') as stream:
            try:
                level_data = yaml.load(stream)
                for i in level_data["levels"]:
                    levels.append(Level(i))
            except yaml.YAMLError as exc:
                print(exc)
        assert levels[0].level_item == "suitcase"
    def test_item_needs_added(self):
        levels = []
        with open("test.yaml", 'r') as stream:
            try:
                level_data = yaml.load(stream)
                for i in level_data["levels"]:
                    levels.append(Level(i))
            except yaml.YAMLError as exc:
                print(exc)
        if levels[0].check_item():
            assert True
        else:
            assert False
    def test_item_not_added(self):
        levels = []
        with open("test.yaml", 'r') as stream:
            try:
                level_data = yaml.load(stream)
                for i in level_data["levels"]:
                    levels.append(Level(i))
            except yaml.YAMLError as exc:
                print(exc)
        if levels[1].check_item():
            assert False
        else:
            assert True

    def test_required_items(self):
        levels = []
        with open("test.yaml", 'r') as stream:
            try:
                level_data = yaml.load(stream)
                for i in level_data["levels"]:
                    levels.append(Level(i))
            except yaml.YAMLError as exc:
                print(exc)
        assert levels[1].required_item == "hammer"

    def test_required_items_result(self):
        levels = []
        with open("test.yaml", 'r') as stream:
            try:
                level_data = yaml.load(stream)
                for i in level_data["levels"]:
                    levels.append(Level(i))
            except yaml.YAMLError as exc:
                print(exc)
        if levels[1].required_item == "hammer":
            assert levels[1].result == "test"


