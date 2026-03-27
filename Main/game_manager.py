# game_manager.py

from locations import get_location

def move_player(player, destination):
    current_location_data = get_location(player["current_location"])
    if destination in current_location_data["connections"]:
        player["current_location"] = destination
        print(f"You have moved to {destination}.")
        print(f"Description: {get_location(destination)['description']}")
        return True
    else:
        print(f"You cannot go to {destination} from {player['current_location']}.")
        return False

def get_current_location_details(player):
    return get_location(player["current_location"])