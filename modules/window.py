import os
import tkinter as tk
from tkinter import messagebox, simpledialog
import subprocess


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("StartX")
        self.geometry("1200x800")

        # Инициализация компонентов
        self.create_widgets()
        self.load_images()

    def create_widgets(self):
        # Панель меню
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        # Панель инструментов
        self.toolbar = tk.Frame(self, bg='lightgray')
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        # Основной контент
        self.content_frame = tk.Frame(self)
        self.content_frame.pack(fill=tk.BOTH, expand=True)

        # Статусбар
        self.statusbar = tk.Label(self, text="Готов к работе", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.statusbar.pack(side=tk.BOTTOM, fill=tk.X)

    def load_images(self):
        # Функция для загрузки изображений
        def get_image_path(filename):
            base_dir = os.path.dirname(os.path.abspath(__file__))
            path = os.path.join(base_dir, "..", "data", filename)
            return os.path.normpath(path)

        # Словарь для хранения изображений
        self.images = {}

        # Загружаем изображения
        for name, filename in [
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
            ("xfe", "xfe.gif")
        ]:
            path = get_image_path(filename)
            if os.path.exists(path):
                self.images[name] = tk.PhotoImage(file=path)
            else:
                raise FileNotFoundError(f"Картинка не найдена: {path}")

    def create_toolbar(self):
        # Создание кнопок на панели инструментов
        buttons = [
            ("AI", "ai"),
            ("Calc", "calc"),
            ("DED", "ded"),
            ("Dev", "dev"),
            ("Doc", "doc"),
            ("Mail", "mail"),
            ("Timer", "ktimer"),
            ("Web", "web"),
            ("Exit", "exit")
        ]

        for text, image_name in buttons:
            btn = tk.Button(self.toolbar,
                            text=text,
                            image=self.images[image_name],
                            compound=tk.TOP,
                            command=lambda t=text: self.on_button_click(t))
            btn.image = self.images[image_name]  # Сохраняем ссылку на изображение
            btn.pack(side=tk.LEFT, padx=2, pady=2)

    def on_button_click(self, button_text):
        if button_text == "Exit":
            self.quit()
        elif button_text == "Calc":
            subprocess.Popen('/usr/bin/galculator')
        elif button_text == "Doc":
            subprocess.Popen('/usr/bin/writer')
        # Добавить остальные обработчики...

