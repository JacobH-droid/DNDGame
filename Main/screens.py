import tkinter as tk
from player import create_player, add_item, equip_item, show_player # Import player functions
from items import get_item # Import get_item to get item details for equipping
from locations import get_location # Import get_location
from game_manager import move_player, get_current_location_details # Import game manager functions
from save_load_manager import save_game # Import save_game


# ---------------------------
# CHARACTER CREATION SCREEN
# ---------------------------
class CharacterScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller # Store controller for player access

        tk.Label(self, text="Create Character", font=("Arial", 20)).pack(pady=20)

        tk.Label(self, text="Name:").pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        # Add race and class selection
        tk.Label(self, text="Race:").pack()
        self.race_var = tk.StringVar(self)
        self.race_var.set("Human") # Default value
        self.race_option = tk.OptionMenu(self, self.race_var, "Human", "Elf", "Dwarf", "Dragonborn", "Tiefling", "Halfling")
        self.race_option.pack()

        tk.Label(self, text="Class:").pack()
        self.class_var = tk.StringVar(self)
        self.class_var.set("Warrior") # Default value
        self.class_option = tk.OptionMenu(self, self.class_var, "Warrior", "Wizard", "Rogue", "Barbarian", "Cleric", "Ranger", "Paladin")
        self.class_option.pack()

        next_btn = tk.Button(self, text="Continue",
                             command=self._create_character_and_proceed)
        next_btn.pack(pady=10)

        back_btn = tk.Button(self, text="Back",
                             command=lambda: controller.show_frame(MainMenu))
        back_btn.pack()

    def _create_character_and_proceed(self):
        player_name = self.name_entry.get()
        player_race = self.race_var.get()
        player_class = self.class_var.get()

        if not player_name:
            player_name = "Hero" # Default name if none entered

        # Create player and store it in the controller
        self.controller.current_player = create_player(player_name, player_race, player_class)
        print(f"Player created: {self.controller.current_player['name']} the {player_race} {player_class}!")
   # Initial gear and stats will be shown when 'Receive Your Starting Gear' is clicked
        show_player(self.controller.current_player) # Show player status to confirm initial gear

        self.controller.show_frame(GameIntroScreen)

# ---------------------------
# GAME INTRODUCTION SCREEN 
# ---------------------------
class GameIntroScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller # Store controller to access player

        tk.Label(self, text="The Adventure Begins!", font=("Arial", 20)).pack(pady=20)
        self.intro_text = tk.Label(self, text="\nYou wake up inside of your house, your new gear already feels comfortable on your body. The world outside beckons!",
                 font=("Arial", 14), wraplength=400)
        self.intro_text.pack(pady=10)

        self.gear_btn = tk.Button(self, text="Receive Your Starting Gear",
                                  command=self._receive_starting_gear)
        self.gear_btn.pack(pady=10)

        self.continue_btn = tk.Button(self, text="Enter the World",
                                     command=lambda: self.enter_game(), state=tk.DISABLED)
        self.continue_btn.pack(pady=20)

    def _receive_starting_gear(self):
        # This method now just prints the already assigned starting gear
        player = self.controller.current_player
        if player:
            print("\n--- Your Starting Gear ---")
            print("Inventory:", player['inventory'])
            print("Equipped:", player['equipment'])
            show_player(player) # Show player status again with gear
            self.continue_btn.config(state=tk.NORMAL) # Enable 'Enter the World' button

        else:
            print("No player created yet!")

    def enter_game(self):
        # Show initial location description
        print(f"You are currently in: {self.controller.current_player['current_location']}")
        current_loc_data = get_current_location_details(self.controller.current_player)
        print(f"Description: {current_loc_data['description']}")
        self.controller.show_frame(GameScreen)

# ---------------------------
# GAME SCREEN (New)
# ---------------------------
class GameScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.location_label = tk.Label(self, text="", font=("Arial", 16))
        self.location_label.pack(pady=20)

        self.description_label = tk.Label(self, text="", wraplength=500, font=("Arial", 12))
        self.description_label.pack(pady=10)

        self.connections_frame = tk.Frame(self)
        self.connections_frame.pack(pady=10)

        # New buttons for game actions
        self.action_buttons_frame = tk.Frame(self)
        self.action_buttons_frame.pack(pady=10)

        tk.Button(self.action_buttons_frame, text="Inventory", command=self._open_inventory).pack(side=tk.LEFT, padx=5)
        tk.Button(self.action_buttons_frame, text="Map", command=self._open_map).pack(side=tk.LEFT, padx=5)
        tk.Button(self.action_buttons_frame, text="Settings", command=self._open_settings).pack(side=tk.LEFT, padx=5)

        self.update_game_screen() # Initial update

    def update_game_screen(self):
        player = self.controller.current_player
        if player:
            current_loc_name = player["current_location"]
            current_loc_data = get_current_location_details(player)

            self.location_label.config(text=f"Current Location: {current_loc_name}")
            self.description_label.config(text=current_loc_data["description"])

            # Clear previous connection buttons
            for widget in self.connections_frame.winfo_children():
                widget.destroy()

            tk.Label(self.connections_frame, text="Available Paths:").pack()
            for connection in current_loc_data["connections"]:
                btn = tk.Button(self.connections_frame, text=f"Go to {connection}",
                                command=lambda dest=connection: self.travel(dest))
                btn.pack(pady=5)
        else:
            self.location_label.config(text="No player data.")
            self.description_label.config(text="")

    def travel(self, destination):
        if move_player(self.controller.current_player, destination):
            self.update_game_screen() # Refresh screen after successful travel

    def _open_inventory(self):
        print("Inventory button clicked.")
        # Future: Implement a separate inventory screen or popup
        # For now, just show player stats which includes current inventory status.
        show_player(self.controller.current_player)

    def _open_map(self):
        print("Map button clicked.")
        # The current GameScreen already displays connections, serving as a basic map.
        # Future: Could implement a more visual map here.
        print("You are viewing the map. Available paths are listed below.")

    def _open_settings(self):
        print("Settings button clicked.")
        save_game(self.controller.current_player)
        # Future: Implement a settings menu with more options

# ---------------------------
# MAIN MENU
# ---------------------------
class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = tk.Label(self, text="DND RPG", font=("Arial", 24))
        label.pack(pady=20)

        start_btn = tk.Button(self, text="Start Game",
                              command=lambda: controller.show_frame(CharacterScreen))
        start_btn.pack(pady=10)

        quit_btn = tk.Button(self, text="Quit", command=controller.quit)
        quit_btn.pack(pady=10)
