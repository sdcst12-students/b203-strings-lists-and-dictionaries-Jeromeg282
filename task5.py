#!python3
"""
##### Task 5
create a dictionary for an inventory of items in a game.  Ask the user for input, and if the item they choose to 'get item', add that item to their inventory.  If they choose to drop item' remove that item from that invenory.  If they choose 'show inventory' give them a list of the items that they have.

Possible extensions:
* nicer format for displaying inventory
* use shortened/abbreviated names for items (recognizing first few characters or spelling errors)

possible items:
food
water
rope
torch
sack
wood
iron
steel
ginger
garlic
fish
stone
wool

example:
>get food
>get water
>get water
>get iron
>get 3 wood
>inventory
You have:
 1 food
 2 water
 1 iron
 3 wood
 >
"""

inventory={}
items= {
    "food": 0,
    "water": 0,
    "rope": 0,
    "torch": 0,
    "sack": 0,
    "wood": 0,
    "iron": 0,
    "steel": 0,
    "ginger": 0,
    "garlic": 0,
    "fish": 0,
    "stone": 0,
    "wool": 0,

}


def additem(item, count=1):
    if item in inventory:
        inventory[item] += count
    else:
        inventory[item] = count

additem()