import tkinter as tk

class StatusBar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.label = tk.Label(self, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.label.pack(fill=tk.X)
        
    def set_text(self, text):
        self.label.config(text=text)
