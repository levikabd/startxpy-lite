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
from modules import toolbar

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
        icon_path = base_dir / "assets" / "icons" / "startxpy-logo-32.gif"

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
        self.fullscreen_var = tk.BooleanVar(value=False)

        # Создаем интерфейс
        self.create_widgets()

        # Панель управления (можно в статусбар или в меню)
        control_frame = ttk.Frame(self)
        control_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=8, pady=4)

        self.fullscreen_cb = ttk.Checkbutton(
            control_frame,
            text="Fullscreen mode",
            variable=self.fullscreen_var,
            command=self.toggle_fullscreen
        )
        self.fullscreen_cb.pack(side=tk.LEFT)

        # # Контент (пример)
        # content = ttk.Label(self, text="Рабочее место StartX", font=("DejaVu Sans", 14))
        # content.pack(fill=tk.BOTH, expand=True)

        # Выход по Esc (удобно, когда чекбокс включён)
        self.bind("<Escape>", self.exit_fullscreen)

    def toggle_fullscreen(self):
        is_on = self.fullscreen_var.get()
        if is_on:
            self.attributes("-fullscreen", True)
            self.is_fullscreen = True
        else:
            self.attributes("-fullscreen", False)
            self.is_fullscreen = False
            # Опционально: вернуть размер, который был до фуллскрина
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

    def button_click(self, button_name):
        print(f"Нажата кнопка: {button_name}")
        # Обработчик нажатий
        if button_name == "exit":
            self.destroy()
        elif button_name == "calc":
            subprocess.Popen('/usr/bin/galculator')
        elif button_name == "doc":
            subprocess.Popen('/usr/bin/writer')
        # Добавьте остальные обработчики


if __name__ == "__main__":
    app = Application()
    app.mainloop()
