# locations.py

locations_data = {
    "Town Square": {
        "description": "The bustling heart of the town, filled with merchants and townsfolk.",
        "connections": ["Town Gates", "Marketplace"]
    },
    "Town Gates": {
        "description": "The main entrance to the town, leading to the outside world.",
        "connections": ["Town Square", "Darkwood Forest"]
    },
    "Darkwood Forest": {
        "description": "A dense, ancient forest shrouded in mystery.",
        "connections": ["Town Gates"]
    },
    "Marketplace": {
        "description": "A vibrant market where goods are bought and sold.",
        "connections": ["Town Square"]
    },
    "Inside Home": {
        "description": "This is your home and where your adventure started.",
        "connections": ["Town/Home Road"]
    },
    "Town/Home Road": {
        "description": "A quiet dirt road leading from your home to the town.",
        "connections": ["Inside Home", "Town Gates"]
    }
}

def get_location(name):
    location = locations_data.get(name)
    if location:
        return location.copy()
    return None

print("locations.py created with locations_data and get_location function.")