# items.py

from weapons import weapons_data
from armor import armor_data
from consumables import consumables_data

items = {}
items.update(weapons_data)
items.update(armor_data)
items.update(consumables_data)

def get_item(name):
    item = items.get(name)
    if item:
        return item.copy()
    return None