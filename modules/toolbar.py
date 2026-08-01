import tkinter as tk


class Toolbar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Создаем кнопки панели инструментов
        self.create_buttons()

    def create_buttons(self):
        # Пример создания кнопок
        buttons = [
            ("Новый", "new.gif", parent.new_file),
            ("Открыть", "open.gif", parent.open_file),
            ("Сохранить", "save.gif", parent.save_file),
            ("Печать", "print.gif", parent.print_file)
        ]

        for text, image, command in buttons:
            btn = tk.Button(
                self,
                text=text,
                image=parent.images[image],
                compound=tk.TOP,
                command=command
            )
            btn.image = parent.images[image]  # Сохраняем ссылку на изображение
            btn.pack(side=tk.LEFT, padx=2, pady=2)
