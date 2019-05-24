# Fantasy Game Inventory
You are creating a fantasy video game. The data structure to model the player’s inventory will be a dictionary where the keys are string values describing the item in the inventory and the value is an integer value detailing how many of that item the player has. For example, the dictionary value 
`{rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}`
 means the player has 1 rope, 6 torches, 42 gold coins, and so on.
 
 Write a function named `display_inventory() that would take any possible “inventory” and display it like the following:
 ```
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger

Total number of items: 62
 ```
 
 Write a function named `add_to_inventory(inventory, items)`, where the `inventory` parameter is a dictionary representing the player’s inventory and the `items` parameter is a list like `loot`. The `add_to_inventory()` function should update the inventory to include the elements in `items`. Note that the `items` list can contain multiples of the same item. Your code could look something like this:
```python
inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
```
The `display_inventory()` function would output the following:
```
Inventory:
45 gold coin
1 rope
1 ruby
1 dagger

Total number of items: 48
```
