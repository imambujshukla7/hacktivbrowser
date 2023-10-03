import tkinter as tk
from tkinter import ttk
import webbrowser

class SimpleBrowser:
    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        self.entry_url = ttk.Entry(self.parent, width=50)
        self.entry_url.pack(pady=10)
        self.button_go = ttk.Button(self.parent, text="Go", command=self.open_url)
        self.button_go.pack()
        self.text_browser = tk.Text(self.parent, wrap="word", height=20, width=80)
        self.text_browser.pack()

    def open_url(self):
        url = self.entry_url.get()
        webbrowser.open(url)

