# gui.py
import tkinter as tk
from browser import SimpleBrowser

class BrowserGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("HacktivBrowser")
        self.browser = SimpleBrowser(self.root)

    def run(self):
        self.root.mainloop()
