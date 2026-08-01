import tkinter as tk


class StatusBar(tk.Label):
    def __init__(self, parent):
        super().__init__(
            parent,
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W,
            text="Готов к работе"
        )

    def set_text(self, text):
        self.config(text=text)

    def clear(self):
        self.config(text="Готов к работе")
