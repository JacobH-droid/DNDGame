# _weapons.py

weapons_data = {
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
        "rarity": "rare",
        "value": 15
    },
    "Magic Staff": {
        "type": "weapon",
        "attack": 6,
        "range": "ranged",
        "rarity": "rare",
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
        "rarity": "epic",
        "value": 30
    }
}


def weapon(name):
    item = weapons_data.get(name)
    if item:
        return item.copy()
    return None