import os
import tkinter as tk
from tkinter import PhotoImage, messagebox
import subprocess
from pathlib import Path
from tkinter import ttk

# Импортируем локальные модули
from modules import chat
from modules import menu
from modules import statusbar
from modules import taskbar
# from modules import toolbar

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("StartXpy")
        self.geometry("1024x768")
        # self.geometry("1200x800")

        # Путь к логотипу
        # #base_dir = Path(__file__).resolve().parent.parent
        # base_dir = os.path.dirname(os.path.abspath(__file__))
        # icon_path = os.path.join(base_dir, "assets", "icons", "startxpy-logo-32.gif")
        base_dir = Path(__file__).resolve().parent  # аналог dirname(abspath(__file__))
        icon_path = base_dir / "assets" / "icons" / "startxpy-logo-64.gif"

        if icon_path.exists():
            self.iconphoto(False, tk.PhotoImage(file=str(icon_path)))
        else:
            print("Not logo!")

        self.attributes('-fullscreen', True)

        # Выход по Escape
        self.bind('<Escape>', self.exit_fullscreen)

        # Получаем путь к папке с изображениями
        self.image_path = self.get_image_path()

        # Загружаем изображения
        self.images = self.load_images()

        # Флаг и переменная для чекбокса
        self.is_fullscreen = True
        self.fullscreen_var = tk.BooleanVar(value=True)
        # Выход по Esc (удобно, когда чекбокс включён)
        self.bind("<Escape>", self.exit_fullscreen)

        # Создаем интерфейс
        self.create_widgets()

        # Добавляем компоненты приложения
        self.chat_panel = chat.ChatPanel(self)
        self.menu_bar = menu.MenuBar(self)
        self.status_bar = statusbar.StatusBar(self)
        self.task_bar = taskbar.TaskBar(self)
        # self.tool_bar = toolbar.ToolBar(self)

        # Привязываем события
        #self.menu_bar.pack(side=tk.TOP, fill=tk.X) # так неправильно
        self.config(menu=self.menu_bar)  # ✅ так нужно прикреплять меню к окну

        # self.tool_bar.pack(side=tk.TOP, fill=tk.X)
        self.chat_panel.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.task_bar.pack(side=tk.LEFT, fill=tk.Y)

        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def toggle_fullscreen(self):
        is_on = self.fullscreen_var.get()
        if is_on:
            self.attributes("-fullscreen", True)
            self.is_fullscreen = True
        else:
            self.attributes("-fullscreen", False)
            self.is_fullscreen = False
            self.geometry("1024x768")

    def exit_fullscreen(self, event=None):
        self.attributes('-fullscreen', False)
        self.geometry("1024x768")  # вернуть прежний размер
        self.fullscreen_var.set(False)
        self.toggle_fullscreen()


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
        # checkb.pack(side=tk.LEFT, padx=2, pady=2)
        # self.fullscreen_cb.pack(side=tk.LEFT)
        # btn = tk.Button(
        #     toolbar,
        #     image=self.images["fullscreen"],
        #     compound=tk.TOP,
        #     text='fullscreen',
        #     command= self.toggle_fullscreen()
        # )

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

    def open_file(self):
        print('File is open:-)')

    def save_file(self):
        print("File is saved :-)")

    def quit(self):
        self.destroy()

    def undo(self):
        print('undo...')

    def redo(self):
        print('redo...')

    def toggle_toolbar(self):
        print('toggle_toolbar...')

    def toggle_statusbar(self):
        print('toggle_statusbar...')

    def show_about(self):
        print("show_about...")


if __name__ == "__main__":
    app = Application()
    app.mainloop()
