# items.py

items = {
    # ---------------------------
    # WEAPONS
    # ---------------------------
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

    # ---------------------------
    # ARMOR
    # ---------------------------
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

    # ---------------------------
    # CONSUMABLES
    # ---------------------------
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
    }
}
