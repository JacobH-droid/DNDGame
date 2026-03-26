import tkinter as tk
import random

# Placeholder imports — you can implement these later
# from player import create_player
# from enemies import get_enemy
# from battle import BattleScreen

# ---------------------------
# Character Creation Function
# ---------------------------
def create_character(self, controller):
    name = self.name_entry.get()
    
    # Example player dictionary (replace with your create_player function)
    player = {
        "name": name,
        "race": "Human",
        "class": "Warrior",
        "inventory": []
    }
    controller.player = player

    # Go to the fixed Intro sequence
    controller.show_frame(IntroScreen)


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


# ---------------------------
# CHARACTER CREATION SCREEN
# ---------------------------
class CharacterScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        tk.Label(self, text="Create Character", font=("Arial", 20)).pack(pady=20)

        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        next_btn = tk.Button(self, text="Continue",
                             command=lambda: create_character(self, controller))
        next_btn.pack(pady=10)

        back_btn = tk.Button(self, text="Back",
                             command=lambda: controller.show_frame(MainMenu))
        back_btn.pack()


# ---------------------------
# ADVENTURE SCREEN
# ---------------------------
class AdventureScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        self.output = tk.Label(self, text="You step onto the road...", wraplength=500)
        self.output.pack(pady=20)

        tk.Button(self, text="Go to Forest", command=lambda: self.travel("forest")).pack()
        tk.Button(self, text="Go to Town", command=lambda: self.travel("town")).pack()
        tk.Button(self, text="Go to Mountains", command=lambda: self.travel("mountains")).pack()

        tk.Button(self, text="Inventory",
                  command=lambda: print(controller.player)).pack(pady=5)

    def travel(self, location):
        self.output.config(text=f"You travel toward the {location}...")

        # Example random events
        event = random.choice(["nothing", "loot"])
        if event == "loot":
            self.controller.player["inventory"].append("Health Potion")
            self.output.config(text=f"You travel toward the {location} and find a Health Potion!")

# ---------------------------
# INTRO SCREEN (Fixed Start)
# ---------------------------
class IntroScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller
        self.step = 0  # Track which step of the intro we're on

        # Label to display story text
        self.text = tk.Label(self, wraplength=600, font=("Arial", 14))
        self.text.pack(pady=40)

        # Continue button
        self.button = tk.Button(self, text="Continue", command=self.next_step)
        self.button.pack()

        # ❌ Remove self.update_text() here! Player does not exist yet

    # Called when the screen is shown, after player exists
    def start_intro(self):
        self.step = 0  # Reset each time the screen is entered
        self.update_text()

    # Update the story text
    def update_text(self):
        # Ensure player exists
        player_name = self.controller.player["name"]

        self.story = [
            f"You wake up in your small home, {player_name}. The morning light filters through the window.",
            "Your gear lies where you left it. Today feels... different.",
            "You gather your belongings, preparing for the road ahead.",
            "Stepping outside, the world stretches before you.",
            "Your journey begins now."
        ]

        self.text.config(text=self.story[self.step])

    # Called when Continue button is clicked
    def next_step(self):
        # Give starting gear on step 3 (index 2)
        if self.step == 2:
            self.controller.player["inventory"].extend([
                "Iron Sword",
                "Health Potion"
            ])
            print("You gathered your gear! Inventory:", self.controller.player["inventory"])

        self.step += 1

        # Check if we've finished the story
        if self.step >= len(self.story):
            # Move to AdventureScreen after intro
            self.controller.show_frame(AdventureScreen)
        else:
            self.update_text()