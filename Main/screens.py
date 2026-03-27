import tkinter as tk
from player import create_player, add_item, equip_item, show_player # Import player functions
from items import get_item # Import get_item to get item details for equipping


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
        self.race_option = tk.OptionMenu(self, self.race_var, "Human", "Elf", "Dwarf")
        self.race_option.pack()

        tk.Label(self, text="Class:").pack()
        self.class_var = tk.StringVar(self)
        self.class_var.set("Warrior") # Default value
        self.class_option = tk.OptionMenu(self, self.class_var, "Warrior", "Mage", "Rogue")
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
        print("Starting Inventory:", self.controller.current_player['inventory'])
        print("Starting Equipped:", self.controller.current_player['equipment'])
        show_player(self.controller.current_player) # Show player status to confirm initial gear

        self.controller.show_frame(GameIntroScreen)

# ---------------------------
# GAME INTRODUCTION SCREEN (New narrative intro)
# ---------------------------
class GameIntroScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller # Store controller to access player

        tk.Label(self, text="The Adventure Begins!", font=("Arial", 20)).pack(pady=20)
        self.intro_text = tk.Label(self, text="\nYou wake up inside of your house, your new gear already feels comfortable on your body. The world outside beckons!",
                 font=("Arial", 14), wraplength=400)
        self.intro_text.pack(pady=10)

        # Removed the 'Receive Your Starting Gear' button as gear is now assigned at character creation.

        self.continue_btn = tk.Button(self, text="Enter the World",
                                 command=lambda: controller.show_frame(QuestScreen), state=tk.NORMAL) # Now always enabled
        self.continue_btn.pack(pady=20)

    # The _receive_starting_gear method is no longer needed and has been removed.

# ---------------------------
# QUEST SCREEN
# ---------------------------
class QuestScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        tk.Label(self, text="Choose a Quest", font=("Arial", 20)).pack(pady=20)

        quest_btn = tk.Button(self, text="Darkwood Forest",
                              command=self.start_quest)
        quest_btn.pack(pady=10)

        back_btn = tk.Button(self, text="Back",
                             command=lambda: controller.show_frame(MainMenu))
        back_btn.pack()

    def start_quest(self):
        print("Quest started!")


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