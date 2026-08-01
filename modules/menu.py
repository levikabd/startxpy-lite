import tkinter as tk


class MenuBar(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)

        # Файл
        file_menu = tk.Menu(self, tearoff=0)
        file_menu.add_command(label="Открыть", command=parent.open_file)
        file_menu.add_command(label="Сохранить", command=parent.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=parent.quit)
        self.add_cascade(label="Файл", menu=file_menu)

        # Правка
        edit_menu = tk.Menu(self, tearoff=0)
        edit_menu.add_command(label="Отменить", command=parent.undo)
        edit_menu.add_command(label="Повторить", command=parent.redo)
        self.add_cascade(label="Правка", menu=edit_menu)

        # Вид
        view_menu = tk.Menu(self, tearoff=0)
        view_menu.add_checkbutton(label="Панель инструментов", command=parent.toggle_toolbar)
        view_menu.add_checkbutton(label="Статусная строка", command=parent.toggle_statusbar)
        self.add_cascade(label="Вид", menu=view_menu)

        # Справка
        help_menu = tk.Menu(self, tearoff=0)
        help_menu.add_command(label="О программе", command=parent.show_about)
        self.add_cascade(label="Справка", menu=help_menu)
