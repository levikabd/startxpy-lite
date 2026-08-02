import tkinter as tk
from tkinter import PhotoImage, messagebox
import subprocess
import os


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("StartX")
        self.geometry("1200x800")

        # label = tk.Label(self, text="Привет, Tkinter работает!")
        # label.pack(pady=20)

        # Создаем панель инструментов
        self.toolbar = tk.Frame(self, bg='lightgray')
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        # Загружаем изображения
        self.images = self.load_images()

        # Создаем кнопки
        self.create_buttons()

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

        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_dir, "assets", "icons")

        for name, filename in image_files:
            path = os.path.join(image_path, filename)
            try:
                images[name] = PhotoImage(file=path)
            except FileNotFoundError:
                print(f"Ошибка: файл {filename} не найден")
            except Exception as e:
                print(f"Ошибка при загрузке {filename}: {str(e)}")

        return images

    def create_buttons(self):
        buttons = [
            ("AI", "ai"),
            ("Калькулятор", "calc"),
            ("DED", "ded"),
            ("Разработка", "dev"),
            ("Документы", "doc"),
            ("Выход", "exit"),
            ("Таймер", "ktimer"),
            ("Почта", "mail"),
            ("Выключение", "poweroff"),
            ("Запуск", "run"),
            ("Веб", "web"),
            ("Файловый менеджер", "xfe")
        ]

        for text, image_name in buttons:
            if image_name in self.images:
                btn = tk.Button(
                    self.toolbar,
                    image=self.images[image_name],
                    compound=tk.TOP,
                    text=text,
                    command=lambda n=image_name: self.button_click(n)
                )
                btn.image = self.images[image_name]  # Сохраняем ссылку на изображение
                btn.pack(side=tk.LEFT, padx=2, pady=2)

    def button_click(self, button_name):
        print(f"Нажата кнопка: {button_name}")
        if button_name == "exit":
            self.destroy()
        elif button_name == "calc":
            subprocess.Popen('/usr/bin/galculator')
        elif button_name == "doc":
            subprocess.Popen('/usr/bin/writer')


if __name__ == "__main__":
    app = Application()
    app.mainloop()
