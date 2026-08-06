# modules/window.py
import os
import tkinter as tk
from .menu_bar import MenuBar
from .toolbar import Toolbar
from .icons import load_icons

from pathlib import Path
from tkinter import ttk
from tkinter import PhotoImage
import subprocess

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("startxpy")
        self.geometry("1024x768")

        # path to logo
        base_dir = Path(__file__).resolve().parent  # аналог dirname(abspath(__file__))
        icon_path = base_dir / "assets" / "icons" / "startxpy-logo-64.gif"
        #icon_path = base_dir / "assets" / "icons" / "startxpy-logo-32.gif"
        if icon_path.exists():
            self.iconphoto(False, tk.PhotoImage(file=str(icon_path)))
        else:
            print("Not logo!")

        self.fullscreen_var = tk.BooleanVar(value=True)
        self.is_fullscreen = True

        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.icons = load_icons(base_dir)

        # Получаем путь к папке с изображениями
        self.image_path = self.get_image_path()
        # Загружаем изображения
        self.images = self.load_images()
        self.create_widgets()

        # Создаём компоненты
        self.menu_bar = MenuBar(
            parent=self,
            base_dir=base_dir,
            icons=self.icons,
            toggle_fullscreen_from_menu=self.toggle_fullscreen_from_menu,
            reset_size=self.reset_size,
        )

        self.toolbar = Toolbar(
            parent=self,
            icons=self.icons,
            toggle_fullscreen=self.toggle_fullscreen_from_menu,  # можно передать тот же метод
        )

        # Упаковываем в одну строку (сначала меню, потом панель)
        # Но так как у обоих есть свой frame с pack(side=TOP), нужно немного хитрее:
        # сделаем общий контейнер и вручную упакуем их side=LEFT
        top_container = tk.Frame(self)
        top_container.pack(side=tk.TOP, fill=tk.X)

        # Хак: забираем frame из компонентов и кладём в общий контейнер
        # self.menu_bar.frame.pack_forget()
        # self.toolbar.frame.pack_forget()
        #
        # self.menu_bar.frame.pack(in_=top_container, side=tk.LEFT, fill=tk.X, expand=True)
        # self.toolbar.frame.pack(in_=top_container, side=tk.LEFT)
        #
        # # Основная область
        # main_area = tk.Frame(self)
        # main_area.pack(fill=tk.BOTH, expand=True)
        # tk.Label(main_area, text="Рабочая область startxpy").pack(pady=20)

    def toggle_fullscreen_from_menu(self):
        # Этот метод вызывается из меню (checkbutton)
        is_on = not self.is_fullscreen
        self.is_fullscreen = is_on
        self.fullscreen_var.set(is_on)

        if is_on:
            self.attributes("-fullscreen", True)
            # Нужно обновить кнопку в toolbar — но у нас нет прямой ссылки на неё
            # Решение: либо хранить ссылку, либо сделать публичный метод в Toolbar
            self.toolbar.set_fullscreen(is_on)
        else:
            self.attributes("-fullscreen", False)
            self.geometry("1024x768")
            self.toolbar.set_fullscreen(is_on)

        print(f"[Меню] Полноэкранный: {'ВКЛ' if is_on else 'ВЫКЛ'}")

    def reset_size(self):
        self.attributes("-fullscreen", False)
        self.geometry("1024x768")
        self.is_fullscreen = False
        self.fullscreen_var.set(False)
        self.toolbar.set_fullscreen(False)


    def get_image_path(self):
        # Получаем путь к папке assets/icons
        base_dir = os.path.dirname(os.path.abspath(__file__))
        # return os.path.join(base_dir, "assets", "icons")
        path = os.path.join(base_dir, "assets", "icons")
        print(f"Пытаюсь загрузить: {path}")
        return path

    def load_images(self):
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

    def toggle_fullscreen(self):
        is_on = self.fullscreen_var.get()
        if is_on:
            self.attributes("-fullscreen", True)
            self.is_fullscreen = True
            self.fullscreen_btn.config(relief=tk.SUNKEN)
        else:
            self.attributes("-fullscreen", False)
            self.is_fullscreen = False
            self.geometry("1024x768")
            self.fullscreen_btn.config(relief=tk.RAISED)

    def create_widgets(self):
        # Создаем панель инструментов
        toolbar = tk.Frame(self, bg='lightgray')
        toolbar.pack(side=tk.TOP, fill=tk.X)

        # Добавляем кнопки с изображениями
        for name in ["doc", "mail", "calc", "xfe", "run", "web", "dev", "ai", "ded", "ktimer", "poweroff", "exit"]:
            if name in self.images:
                btn = tk.Button(
                    toolbar,
                    image=self.images[name],
                    compound=tk.TOP,
                    text=name.capitalize(),
                    command=lambda n=name: self.button_click(n)
                )
                btn.image = self.images[name]  # Сохраняем ссылку на изображение
                btn.pack(side=tk.LEFT, padx=2, pady=2)

        # control_frame = ttk.Frame(self)
        # control_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=8, pady=4)
        checkb = ttk.Checkbutton(
            toolbar,
            image=self.images["fullscreen"],
            compound=tk.TOP,
            text="fullscreen",
            variable=self.fullscreen_var,
            command=self.toggle_fullscreen
        )
        checkb.image = self.images["fullscreen"]  # Сохраняем ссылку на изображение
        checkb.pack(side=tk.LEFT, padx=2, pady=2)

    def button_click(self, button_name):
        print(f"Нажата кнопка: {button_name}")
        # Обработчик нажатий
        if button_name == "exit":
            self.destroy()
        elif button_name == "calc":
            subprocess.Popen('/usr/bin/galculator')
        elif button_name == "doc":
            subprocess.Popen('libreoffice')
        # Добавьте остальные обработчики
