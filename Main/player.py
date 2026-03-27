# player.py

from items import get_item
from weapons import weapons_data
from armor import armor_data
from consumables import consumables_data
from starting_gear import starting_gear_data
# ---------------------------
# PLAYER CREATION
# ---------------------------
def create_player(name, race, char_class):
    # Get starting gear based on class and race
    gear = starting_gear_data.get(char_class, {}).get(race, {})

    player = {
        "name": name,
        "race": race,
        "class": char_class,

        # Base stats
        "max_HP": 30,
        "HP": 30,
        "Strength": 5,
        "Dexterity": 5,
        "Intelligence": 5,

        # Progression
        "XP": 0,
        "Gold": 0,

        # Inventory & Equipment
        "inventory": list(gear.get("inventory", [])),
        "equipment": {
            "weapon": gear.get("equipped", {}).get("weapon"),
            "offhand": gear.get("equipped", {}).get("offhand"),
            "body": gear.get("equipped", {}).get("body")
        }
    }

    return player

# ---------------------------
# INVENTORY FUNCTIONS
# ---------------------------
def show_inventory(player):
    print("\n--- Inventory ---")
    if not player["inventory"]:
        print("Empty")
        return

    for i, item in enumerate(player["inventory"]):
        print(f"{i+1}. {item}")

def add_item(player, item_name):
    player["inventory"].append(item_name)

def remove_item(player, item_name):
    if item_name in player["inventory"]:
        player["inventory"].remove(item_name)

# ---------------------------
# EQUIPMENT SYSTEM
# ---------------------------
def equip_item(player, item_name):
    item = get_item(item_name)

    if not item:
        print("Item does not exist.")
        return

    if item_name not in player["inventory"]:
        print("You don't have that item.")
        return

    if item["type"] not in ["weapon", "armor"]:
        print("You cannot equip this item.")
        return

    slot = item.get("slot", "weapon") if item["type"] == "armor" else "weapon"

    # Unequip existing item in slot
    if player["equipment"][slot]:
        old_item = player["equipment"][slot]
        player["inventory"].append(old_item)
        print(f"Unequipped {old_item}")

    # Equip new item
    player["equipment"][slot] = item_name
    player["inventory"].remove(item_name)

    print(f"Equipped {item_name} in {slot} slot.")

def unequip_item(player, slot):
    if slot not in player["equipment"]:
        print("Invalid slot.")
        return

    item = player["equipment"][slot]

    if not item:
        print("Nothing equipped in that slot.")
        return

    player["inventory"].append(item)
    player["equipment"][slot] = None

    print(f"Unequipped {item}")

def show_equipment(player):
    print("\n--- Equipment ---")
    for slot, item in player["equipment"].items():
        print(f"{slot.capitalize()}: {item if item else 'None'}")

# ---------------------------
# USING ITEMS
# ---------------------------
def use_item(player, item_name):
    item = get_item(item_name)

    if not item:
        print("Item does not exist.")
        return

    if item_name not in player["inventory"]:
        print("You don't have that item.")
        return

    if item["type"] != "consumable":
        print("You cannot use that item.")
        return

    effect = item.get("effect")

    if effect == "heal":
        heal_amount = item["value"]
        player["HP"] = min(player["HP"] + heal_amount, player["max_HP"])
        print(f"You used {item_name} and healed {heal_amount} HP!")

    elif effect == "mana":
        print("Mana system not implemented yet.")

    else:
        print("Unknown item effect.")

    # Remove item after use
    player["inventory"].remove(item_name)

# ---------------------------
# STAT CALCULATIONS
# ---------------------------
def get_total_attack(player):
    base = player["Strength"]

    weapon_name = player["equipment"]["weapon"]
    if weapon_name:
        weapon = get_item(weapon_name)
        base += weapon.get("attack", 0)

    return base

def get_total_defense(player):
    base = 0

    for slot in player["equipment"]:
        item_name = player["equipment"][slot]
        if item_name:
            item = get_item(item_name)
            base += item.get("defense", 0)

    return base

# ---------------------------
# PLAYER STATUS
# ---------------------------
def show_player(player):
    print(f"""
=========================
{player['name']} the {player['race']} {player['class']}
HP: {player['HP']}/{player['max_HP']}
STR: {player['Strength']} | DEX: {player['Dexterity']} | INT: {player['Intelligence']}
Gold: {player['Gold']} | XP: {player['XP']}

Attack: {get_total_attack(player)}
Defense: {get_total_defense(player)}
=========================
""")