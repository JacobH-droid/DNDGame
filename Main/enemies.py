# ENEMIES.PY CONTENT
# Original Imports:
# (none)
# ---------------------------
enemies = {
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
        "loot_table": ["Mana Potion"]
    }
}

def get_enemy(enemy_name):
    return enemies.get(enemy_name)