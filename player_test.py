from player import Player

class TestPlayer:
    def test_name(self):
        backpack = ["pen", "laptop"]
        player = Player('Emily', backpack)
        assert player.get_name() == 'Emily'
    def test_items(self):
        backpack = ["pen", "laptop"]
        backpack_should_contain = ["pen", "laptop"]
        player = Player('Emily', backpack)
        assert backpack_should_contain == player.list_items()
    def test_add_items(self):
        backpack = ["pen", "laptop"]
        backpack_should_contain = ["pen", "laptop", "hammer"]
        player = Player('Emily', backpack)
        player.add_item("hammer")
        assert backpack_should_contain == player.list_items()
    def test_has_check_item(self):
        item = 'pen'
        backpack = ["pen", "laptop"]
        player = Player('Emily', backpack)
        if player.check_item(item):
            assert True
    def test_doesnt_have_check_item(self):
        item = 'pen'
        backpack = ["pen", "laptop"]
        player = Player('Emily', backpack)
        if not player.check_item(item):
            assert True

