armor_data = {
    "Rusted Warrior Helmet": {
        "type": "armor",
        "defense": 1,
        "slot": "head",
        "rarity": "common",
        "value": 3,
        "set": "Warrior starter"
    },
    "Rusted Warrior chainmail": {
        "type": "armor",
        "defense": 2,
        "slot": "body",
        "rarity": "common",
        "value": 5,
        "set": "Warrior starter"
    },
    "Rusted Warrior Gauntlets": {
        "type": "armor",
        "defense": 1,
        "slot": "hands",
        "rarity": "common",
        "value": 3,
        "set": "Warrior starter"
    },
    "Rusted Warrior greaves": {
        "type": "armor",
        "defense": 1,
        "slot": "legs",
        "rarity": "common",
        "value": 7,
        "set": "Warrior starter"
    },
    "Cracked Wooden Shield": {
        "type": "shield",
        "defense": 2,
        "slot": "offhand",
        "rarity": "common",
        "value": 5,
        "set": "Warrior starter"
    },
    "Torn Wizard hat": {
        "type": "armor",
        "defense": 0,
        "slot": "head",
        "rarity": "common",
        "value": 1,
        "set": "Wizard starter"
    },
    "Torn Wizard Robes": {
        "type": "armor",
        "defense": 2,
        "slot": "body",
        "rarity": "common",
        "value": 5,
        "set": "Wizard starter"
    },
    "Torn Wizard sleeves": {
        "type": "armor",
        "defense": 0,
        "slot": "hands",
        "rarity": "common",
        "value": 1,
        "set": "Wizard starter"
    },
    "Torn Wizard lower robe": {
        "type": "armor",
        "defense": 2,
        "slot": "legs",
        "rarity": "common",
        "value": 5,
        "set": "Wizard starter"
    },
    "Torn Rogue's mask": {
        "type": "armor",
        "defense": 1,
        "slot": "head",
        "rarity": "common",
        "value": 2,
        "set": "Rogue starter"
    },
    "Torn Rogue's cloak": {
        "type": "armor",
        "defense": 2,
        "slot": "body",
        "rarity": "common",
        "value": 2,
        "set": "Rogue starter"
    },
    "Rusted Rogue's bracer": {
        "type": "armor",
        "defense": 2,
        "slot": "hands",
        "rarity": "common",
        "value": 5,
        "set": "Rogue starter"
    },
    "Torn Rogue's leggings": {
        "type": "armor",
        "defense": 2,
        "slot": "legs",
        "rarity": "common",
        "value": 5,
        "set": "Rogue starter"
    },
    "Barbarian's Weathered War-Mask": {
        "type": "armor",
        "defense": 2,
        "slot": "head",
        "rarity": "common",
        "value": 5,
        "set": "Barbarian starter"
    }
}

def armor(name):
    item = armor_data.get(name)
    if item:
        return item.copy()
    return None
