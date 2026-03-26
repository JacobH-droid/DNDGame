import tkinter as tk
from screens import MainMenu, CharacterScreen, IntroScreen, AdventureScreen

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("DND RPG")
        self.geometry("800x600")

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        # Register all screens here
        for F in (MainMenu, CharacterScreen, IntroScreen, AdventureScreen):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Start at Main Menu
        self.show_frame(MainMenu)

    def show_frame(self, screen):
        frame = self.frames[screen]
        frame.tkraise()
        # If it's the IntroScreen, call its start_intro method
        if screen == IntroScreen:
            frame.start_intro()


if __name__ == "__main__":
    app = App()
    app.mainloop()