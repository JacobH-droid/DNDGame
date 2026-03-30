# _weapons.py

weapons_data = {
    "Rusty Iron Sword": {
        "type": "weapon",
        "attack": 3,
        "range": "melee",
        "rarity": "common",
        "value": 5
    },
    "Rusty Longbow": {
        "type": "weapon",
        "attack": 2,
        "range": "ranged",
        "rarity": "common",
        "value": 6
    },
    "Rusty Dagger": {
        "type": "weapon",
        "attack": 1,
        "range": "melee",
        "rarity": "common",
        "value": 2
    },
    "Iron Sword": {
        "type": "weapon",
        "attack": 5,
        "range": "melee",
        "rarity": "common",
        "value": 10
    },
    "Longbow": {
        "type": "weapon",
        "attack": 4,
        "range": "ranged",
        "rarity": "common",
        "value": 12
    },
    "Battle Axe": {
        "type": "weapon",
        "attack": 7,
        "range": "melee",
        "rarity": "uncommon",
        "value": 15
    },
    "Magic Staff": {
        "type": "weapon",
        "attack": 6,
        "range": "ranged",
        "rarity": "uncommon",
        "value": 20
    },
    "Dagger": {
        "type": "weapon",
        "attack": 3,
        "range": "melee",
        "rarity": "common",
        "value": 5
    },
    "Crossbow": {
        "type": "weapon",
        "attack": 6,
        "range": "ranged",
        "rarity": "uncommon",
        "value": 18
    },
    "Warhammer": {
        "type": "weapon",
        "attack": 8,
        "range": "melee",
        "rarity": "rare",
        "value": 30
    },
    "Shortsword": {
        "type": "weapon",
        "attack": 4,
        "range": "melee",
        "rarity": "common",
        "value": 8
    },
    "Greatsword": {
        "type": "weapon",
        "attack": 10,
        "range": "melee",
        "rarity": "epic",
        "value": 50
    },
    "Shortbow": {
        "type": "weapon",
        "attack": 3,
        "range": "ranged",
        "rarity": "common",
        "value": 9
    },
    "Handaxe": {
        "type": "weapon",
        "attack": 5,
        "range": "melee",
        "rarity": "common",
        "value": 7
    },
    "Greataxe": {
        "type": "weapon",
        "attack": 11,
        "range": "melee",
        "rarity": "epic",
        "value": 55
    },
    "Mace": {
        "type": "weapon",
        "attack": 6,
        "range": "melee",
        "rarity": "uncommon",
        "value": 14
    },
    "Spear": {
        "type": "weapon",
        "attack": 6,
        "range": "melee",
        "rarity": "common",
        "value": 10
    },
    "Wand": {
        "type": "weapon",
        "attack": 5,
        "range": "ranged",
        "rarity": "rare",
        "value": 25
    },
    "Sling": {
        "type": "weapon",
        "attack": 2,
        "range": "ranged",
        "rarity": "common",
        "value": 4
    },
    "Light Crossbow": {
        "type": "weapon",
        "attack": 5,
        "range": "ranged",
        "rarity": "uncommon",
        "value": 15
    },
    "Scimitar": {
        "type": "weapon",
        "attack": 4,
        "range": "melee",
        "rarity": "uncommon",
        "value": 10
    },
    "Quarterstaff": {
        "type": "weapon",
        "attack": 4,
        "range": "melee",
        "rarity": "common",
        "value": 7
    },
    "Halberd": {
        "type": "weapon",
        "attack": 9,
        "range": "melee",
        "rarity": "rare",
        "value": 40
    },
    "Morning Star": {
        "type": "weapon",
        "attack": 7,
        "range": "melee",
        "rarity": "uncommon",
        "value": 20
    },
    "Throwing Axe": {
        "type": "weapon",
        "attack": 4,
        "range": "ranged",
        "rarity": "common",
        "value": 8
    },
    "Composite Bow": {
        "type": "weapon",
        "attack": 6,
        "range": "ranged",
        "rarity": "rare",
        "value": 25
    }
} 


def weapon(name):
    item = weapons_data.get(name)
    if item:
        return item.copy()
    return None
