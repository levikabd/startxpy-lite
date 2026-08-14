# modules/icons.py
import os
import tkinter as tk

def load_icons(base_dir):
    """Загружает иконки в словарь, возвращает dict[name] -> PhotoImage или None"""
    icon_dir = os.path.join(base_dir, "assets", "icons")
    icons = {}
    names = ["fullscreen", "doc", "mail", "settings"]  # добавь свои

    print("base_dir:", base_dir)
    print("icon_dir:", icon_dir)

    for name in names:
        path = os.path.join(icon_dir, f"{name}.gif")
        try:
            icons[name] = tk.PhotoImage(file=path)
        except tk.TclError as e:
            print(f"Icon {name} not loaded: {e}")
            icons[name] = None
    return icons
