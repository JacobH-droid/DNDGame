#main.py
import tkinter as tk
import sys # Import sys module
from screens import MainMenu, CharacterScreen, GameIntroScreen # Import IntroScreen and GameIntroScreen

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
        self.geometry("800x600")

        # Create a frame for the main content (screens)
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        # Create a frame for the console output
        self.console_frame = tk.Frame(self, height=150, bd=2, relief=tk.SUNKEN)
        self.console_frame.pack(side="bottom", fill="x", expand=False)

        self.console_text = tk.Text(self.console_frame, wrap="word", state="disabled", height=8, bg="black", fg="white")
        self.console_text.pack(fill="both", expand=True)

        # Redirect stdout to the console_text widget
        sys.stdout = TextRedirector(self.console_text, "stdout")

        self.frames = {}
        self.current_player = None # Initialize current_player

        for F in (MainMenu, CharacterScreen, GameIntroScreen): # Add IntroScreen and GameIntroScreen to frames
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