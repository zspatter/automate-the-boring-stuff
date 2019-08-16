#! /usr/bin/env python3
# fantasy_game_inventory.py -


def display_inventory(inventory):
    output = 'Inventory:\n'
    total_items = 0

    for k, v in inventory.items():
        output += '{} {}\n'.format(v, k)
        total_items += int(v)

    return output + '\nTotal number of items: {}\n'.format(total_items)


def add_to_inventory(inventory, items):
    for item in items:
        inventory.setdefault(item, 0)
        inventory[item] += 1


if __name__ == '__main__':
    inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    print(display_inventory(inv), '\n')

    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    add_to_inventory(inv, dragon_loot)
    print(display_inventory(inv), '\n')
