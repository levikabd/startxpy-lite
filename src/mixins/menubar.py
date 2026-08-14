import os
from pathlib import Path
from tkinter import PhotoImage
import tkinter as tk
from tkinter import ttk
# from .icons import load_icons

class MenubarMixin:
    # def __init__(self, parent, base_dir, icons, toggle_fullscreen_from_menu, reset_size):
        # self.image_path = self.get_image_path()
        # self.icons = self.load_icons()

    def setup_menu(self):
        self.base_dir = Path(__file__).resolve().parent.parent.parent  # аналог dirname(abspath(__file__))
        self.image_path = self.get_image_path()
        self.icons = self.load_icons()
        self.create_widgets()


    # def load_icons(self, base_dir):
    #     """Загружает иконки в словарь, возвращает dict[name] -> PhotoImage или None"""
    #     icon_dir = os.path.join(base_dir, "assets", "icons")
    #     icons = {}
    #     names = ["fullscreen", "doc", "mail", "settings"]  # добавь свои
    #
    #     print("base_dir:", base_dir)
    #     print("icon_dir:", icon_dir)
    #
    #     for name in names:
    #         path = os.path.join(icon_dir, f"{name}.gif")
    #         try:
    #             icons[name] = tk.PhotoImage(file=path)
    #         except tk.TclError as e:
    #             print(f"Icon {name} not loaded: {e}")
    #             icons[name] = None
    #     return icons

    def get_image_path(self):
        # Получаем путь к папке assets/icons
        # return os.path.join(base_dir, "assets", "icons")
        icon_path = self.base_dir / "assets" / "icons"
        # print(f"Пытаюсь загрузить: {icon_path}")
        return icon_path

    def load_icons(self):
        images = {}
        image_files = [
            ("ai", "ai.gif"),
            ("calc", "calc.gif"),
            ("ded", "ded.gif"),
            ("dev", "dev.gif"),
            ("doc", "doc.gif"),
            ("exit", "exit.gif"),
            ("ktimer", "ktimer.gif"),
            ("mail", "mail.gif"),
            ("poweroff", "poweroff.gif"),
            ("run", "run.gif"),
            ("web", "web.gif"),
            ("fullscreen", "fullscreen.gif"),
            ("xfe", "xfe.gif")
        ]

        for name, filename in image_files:
            path = os.path.join(self.image_path, filename)
            if os.path.exists(path):
                try:
                    images[name] = PhotoImage(file=path)
                except Exception as e:
                    print(f"Ошибка загрузки {filename}: {str(e)}")
            else:
                print(f"Предупреждение: изображение {filename} не найдено")

        return images

    def create_widgets(self):
        # Создаем панель инструментов
        toolbar = tk.Frame(self, bg='lightgray')
        toolbar.pack(side=tk.TOP, fill=tk.X)

        # Добавляем кнопки с изображениями
        for name in ["doc", "mail", "calc", "xfe", "run", "web", "dev", "ai", "ded", "ktimer", "poweroff", "exit"]:
            if name in self.icons:
                btn = tk.Button(
                    toolbar,
                    image=self.icons[name],
                    compound=tk.TOP,
                    text=name.capitalize(),
                    command=lambda n=name: self.button_click(n)
                )
                btn.image = self.icons[name]  # Сохраняем ссылку на изображение
                btn.pack(side=tk.LEFT, padx=2, pady=2)
                # print('button ', name, 'add')

        # control_frame = ttk.Frame(self)
        # control_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=8, pady=4)
        check_button = ttk.Checkbutton(
            toolbar,
            image=self.icons["fullscreen"],
            compound=tk.TOP,
            text="fullscreen",
            # variable=self.fullscreen_var,
            # command=self.toggle_fullscreen
        )
        check_button.image = self.icons["fullscreen"]  # Сохраняем ссылку на изображение
        check_button.pack(side=tk.LEFT, padx=2, pady=2)
