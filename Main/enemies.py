# enemies.py

enemies_data = {
    "Goblin": {
        "HP": 20,
        "Attack": 5,
        "Defense": 2,
        "Speed": 5,
        "XP": 10,
        "Gold": 5,
        "loot_table": ["Health Potion"]
    },

    "Orc Warrior": {
        "HP": 35,
        "Attack": 8,
        "Defense": 4,
        "Speed": 3,
        "XP": 20,
        "Gold": 15,
        "loot_table": ["Iron Sword", "Steel Shield"]
    },

    "Dark Mage": {
        "HP": 25,
        "Attack": 10,
        "Defense": 3,
        "Speed": 4,
        "XP": 30,
        "Gold": 20,
        "loot_table": ["Mana Potion", "Magic Staff"]
    },

    "Forest Spider": {
        "HP": 15,
        "Attack": 4,
        "Defense": 1,
        "Speed": 7,
        "XP": 8,
        "Gold": 3,
        "loot_table": ["Antidote"]
    },

    "Skeleton Knight": {
        "HP": 40,
        "Attack": 9,
        "Defense": 6,
        "Speed": 2,
        "XP": 35,
        "Gold": 25,
        "loot_table": ["Plate Armor", "Battle Axe"]
    },

    "Dragon Hatchling": {
        "HP": 60,
        "Attack": 12,
        "Defense": 7,
        "Speed": 6,
        "XP": 50,
        "Gold": 40,
        "loot_table": ["Greater Health Potion", "Helmet"]
    },

    "Bandit": {
        "HP": 22,
        "Attack": 6,
        "Defense": 3,
        "Speed": 5,
        "XP": 12,
        "Gold": 7,
        "loot_table": ["Leather Vest", "Longbow"]
    },

    "Ghoul": {
        "HP": 30,
        "Attack": 7,
        "Defense": 3,
        "Speed": 4,
        "XP": 18,
        "Gold": 10,
        "loot_table": ["Health Potion"]
    }
}

def get_enemy(name):
    enemy = enemies_data.get(name)
    if enemy:
        return enemy.copy()
    return None