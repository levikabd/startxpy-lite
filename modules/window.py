import os
import tkinter as tk
from tkinter import PhotoImage, messagebox
import subprocess


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("StartX")
        self.geometry("1200x800")

        # Получаем путь к папке с изображениями
        self.image_path = self.get_image_path()

        # Загружаем изображения
        self.images = self.load_images()

        # Создаем интерфейс
        self.create_widgets()

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
        for name in ["ai", "calc", "ded", "dev", "doc", "exit", "ktimer", "mail", "poweroff", "run", "web", "xfe"]:
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
