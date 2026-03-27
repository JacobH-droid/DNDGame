# MAIN.PY CONTENT
# Original Imports:
import tkinter as tk
from screens import MainMenu, CharacterScreen, IntroScreen, AdventureScreen, BattleScreen # Added BattleScreen

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("DND RPG")
        self.geometry("800x600")

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        # Store current battle instance
        self.battle = None

        # Register all screens here
        for F in (MainMenu, CharacterScreen, IntroScreen, AdventureScreen, BattleScreen):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Start at Main Menu
        self.show_frame(MainMenu)

    def show_frame(self, screen_class):
        frame = self.frames[screen_class]
        frame.tkraise()
        self.current_frame = frame # Keep track of the currently displayed frame
        # If it's the IntroScreen, call its start_intro method
        if screen_class == IntroScreen:
            frame.start_intro()
        elif screen_class == BattleScreen:
            frame.update_display() # Initialize battle screen display


if __name__ == "__main__":
    app = App()
    app.mainloop()