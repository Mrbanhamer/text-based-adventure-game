import pytest
from rpg.systems.combat import start_combat_in_room

@pytest.mark.parametrize("bag,expected", [
    (["Armor", "Shield"], "none"),                 # saknar Battle Axe → ingen strid
    (["Armor", "Battle Axe", "Shield"], "win"),    # full gear → autovinst
])
def test_dragon(bag, expected):
    assert start_combat_in_room("Dragon's Lair", bag, 10) == expected