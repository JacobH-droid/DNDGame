# save_load_manager.py
import json

SAVE_FILE = "savegame.json"

def save_game(player):
    try:
        with open(SAVE_FILE, "w") as f:
            json.dump(player, f, indent=4)
        print("Game saved successfully!")
    except Exception as e:
        print(f"Error saving game: {e}")

def load_game():
    try:
        with open(SAVE_FILE, "r") as f:
            player_data = json.load(f)
        print("Game loaded successfully!")
        return player_data
    except FileNotFoundError:
        print("No save game found.")
        return None
    except Exception as e:
        print(f"Error loading game: {e}")
        return None