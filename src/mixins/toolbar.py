# modules/toolbar.py
import tkinter as tk

class Toolbar:
    def __init__(self, parent, icons, toggle_fullscreen):
        self.parent = parent
        self.icons = icons
        self.toggle_fullscreen_fn = toggle_fullscreen

        self.frame = tk.Frame(parent, bd=1, relief=tk.RAISED, bg="#f0f0f0")

        # Кнопка «Полноэкран»
        btn = tk.Button(
            self.frame,
            text="Полноэкран",
            image=self.icons.get("fullscreen"),
            compound=tk.LEFT,
            command=self._on_click,
            relief=tk.RAISED,
            bd=2,
            bg="#f0f0f0",
        )
        btn.pack(side=tk.LEFT, padx=2, pady=2)
        self.fullscreen_btn = btn

        # Разделитель
        sep = tk.Label(self.frame, text="|", fg="#aaa", bg="#f0f0f0")
        sep.pack(side=tk.LEFT, padx=6, pady=2)

        # Сюда можно добавить другие кнопки-режимы

    def _on_click(self):
        is_on = not self.parent.is_fullscreen
        self.parent.is_fullscreen = is_on
        self.parent.fullscreen_var.set(is_on)

        if is_on:
            self.parent.attributes("-fullscreen", True)
            self.fullscreen_btn.config(relief=tk.SUNKEN)
        else:
            self.parent.attributes("-fullscreen", False)
            self.parent.geometry("1024x768")
            self.fullscreen_btn.config(relief=tk.RAISED)

        print(f"[Панель] Полноэкранный: {'ВКЛ' if is_on else 'ВЫКЛ'}")

    def pack(self, **kwargs):
        self.frame.pack(side=tk.TOP, fill=tk.X, **kwargs)

# в modules/toolbar.py, добавь в класс Toolbar:
    def set_fullscreen(self, is_on):
        if is_on:
            self.fullscreen_btn.config(relief=tk.SUNKEN)
        else:
            self.fullscreen_btn.config(relief=tk.RAISED)
