import tkinter as tk

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
                             command=lambda: controller.show_frame(QuestScreen))
        next_btn.pack(pady=10)

        back_btn = tk.Button(self, text="Back",
                             command=lambda: controller.show_frame(MainMenu))
        back_btn.pack()


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
        print("Quest started!")  # later this triggers combat
