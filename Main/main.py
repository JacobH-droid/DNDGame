import tkinter as tk
from Main.screens import MainMenu, CharacterScreen, QuestScreen

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("DND RPG")
        self.geometry("800x600")

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        for F in (MainMenu, CharacterScreen, QuestScreen):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)

    def show_frame(self, screen):
        frame = self.frames[screen]
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()