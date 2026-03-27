consumables_data = {
    "Health Potion": {
        "type": "consumable",
        "effect": "heal",
        "value": 20,
        "rarity": "common"
    },
    "Mana Potion": {
        "type": "consumable",
        "effect": "mana",
        "value": 15,
        "rarity": "common"
    },
    "Greater Health Potion": {
        "type": "consumable",
        "effect": "heal",
        "value": 50,
        "rarity": "rare"
    },
    "Antidote": {
        "type": "consumable",
        "effect": "cure_poison",
        "value": 10,
        "rarity": "common"
    },
    "Stamina Potion": {
        "type": "consumable",
        "effect": "stamina",
        "value": 25,
        "rarity": "uncommon"
    },
    "Elixir of Strength": {
        "type": "consumable",
        "effect": "stat_boost",
        "stat": "Strength",
        "value": 2,
        "duration": 5,
        "rarity": "rare"
    },
    "Scroll of Wisdom": {
        "type": "consumable",
        "effect": "xp_boost",
        "value": 100,
        "rarity": "rare"
    }
}

def consumable(name):
    item = consumables_data.get(name)
    if item:
        return item.copy()
    return None