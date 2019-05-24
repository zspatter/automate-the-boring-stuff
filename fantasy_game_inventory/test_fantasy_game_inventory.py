from collections import Counter
import copy

from fantasy_game_inventory import fantasy_game_inventory

inventory = {'a': 1, 'b': 2, 'c': 3, 'd': 4}


def test_display_inventory():
    formatted_inventory = fantasy_game_inventory.display_inventory(inventory)
    total_items = 0

    for k, v in inventory.items():
        assert '{} {}\n'.format(v, k) in formatted_inventory
        total_items += int(v)

    counter = Counter(formatted_inventory)
    assert counter['\n'] == len(inventory) + 3
    assert 'Total number of items: {}'.format(total_items) in formatted_inventory


def test_add_to_inventory():
    loot = ['a', 'gold', 'gold', 'a']
    new_inv = copy.deepcopy(inventory)
    fantasy_game_inventory.add_to_inventory(new_inv, loot)

    for item in new_inv:
        if item in inventory:
            assert inventory[item] <= new_inv[item]

    assert new_inv['a'] == 3
    assert new_inv['gold'] == 2
    assert len(new_inv) == len(inventory) + 1


