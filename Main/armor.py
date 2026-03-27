# _armor.py

armor_data = {
    "Steel Shield": {
        "type": "armor",
        "defense": 4,
        "slot": "offhand",
        "rarity": "common",
        "value": 15
    },
    "Plate Armor": {
        "type": "armor",
        "defense": 8,
        "slot": "body",
        "rarity": "rare",
        "value": 40
    },
    "Leather Vest": {
        "type": "armor",
        "defense": 2,
        "slot": "body",
        "rarity": "common",
        "value": 8
    },
    "Helmet": {
        "type": "armor",
        "defense": 3,
        "slot": "head",
        "rarity": "uncommon",
        "value": 10
    },
    "Wizard Hat": {
        "type": "armor",
        "defense": 1,
        "slot": "head",
        "rarity": "uncommon",
        "value": 12
    },
    "Gauntlets": {
        "type": "armor",
        "defense": 2,
        "slot": "hands",
        "rarity": "common",
        "value": 7
    },
    "Boots of Swiftness": {
        "type": "armor",
        "defense": 1,
        "slot": "feet",
        "rarity": "rare",
        "value": 20
    },
    "Chainmail": {
        "type": "armor",
        "defense": 5,
        "slot": "body",
        "rarity": "uncommon",
        "value": 25
    },
    "Leather Gloves": {
        "type": "armor",
        "defense": 1,
        "slot": "hands",
        "rarity": "common",
        "value": 5
    },
    "Iron Boots": {
        "type": "armor",
        "defense": 2,
        "slot": "feet",
        "rarity": "common",
        "value": 10
    },
    "Wooden Shield": {
        "type": "armor",
        "defense": 2,
        "slot": "offhand",
        "rarity": "common",
        "value": 8
    },
    "Magic Robe": {
        "type": "armor",
        "defense": 3,
        "slot": "body",
        "rarity": "uncommon",
        "value": 18
    }
}

def armor(name):
    item = armor_data.get(name)
    if item:
        return item.copy()
    return None