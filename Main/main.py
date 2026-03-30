import tkinter as tk
import sys # Import sys module
from screens import MainMenu, CharacterScreen, GameIntroScreen, GameScreen # Import IntroScreen, GameIntroScreen, and GameScreen



# Custom class to redirect stdout to a tkinter Text widget
class TextRedirector:
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert(tk.END, str, (self.tag,))
        self.widget.configure(state="disabled")
        self.widget.see(tk.END) # Auto-scroll to the end

    def flush(self):
        pass # Required for file-like objects

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("DND RPG")
        self.geometry("1920x1080")

        # Create a frame for the console output on the right
        self.console_frame = tk.Frame(self, width=250, bd=2, relief=tk.SUNKEN) # Fixed width
        self.console_frame.pack(side="right", fill="y", expand=False) # Fill vertically, don't expand horizontally

        self.console_text = tk.Text(self.console_frame, wrap="word", state="disabled", bg="black", fg="white")
        self.console_text.pack(fill="both", expand=True) # Text widget fills its parent console_frame

        # Redirect stdout to the console_text widget
        sys.stdout = TextRedirector(self.console_text, "stdout")

        # Create a frame for the main content (screens) on the left, filling the rest of the space
        self.container = tk.Frame(self)
        self.container.pack(side="left", fill="both", expand=True)

        self.frames = {}
        self.current_player = None # Initialize current_player

        for F in (MainMenu, CharacterScreen, GameIntroScreen, GameScreen):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu) # Start with MainMenu

    def show_frame(self, screen):
        frame = self.frames[screen]
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()