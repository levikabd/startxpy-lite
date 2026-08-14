# modules/menu_bar.py
import tkinter as tk

from .icons import load_icons

class MenubarMixin:
    #def __init__(self, parent, base_dir, icons, toggle_fullscreen_from_menu, reset_size):
    def setup_menu(self):
        # self.parent = parent
        # self.icons = icons
        # self.toggle_fullscreen = toggle_fullscreen_from_menu
        # self.reset_size = reset_size

        # Frame для строки меню (без pack — это делает родитель)
        self.frame = tk.Frame(self, bd=1, relief=tk.RAISED, bg="#f0f0f0")

        # self.create_widgets()

        # «Файл»
        file_mb = self._make_menubutton("Файл")
        file_menu = tk.Menu(file_mb, tearoff=0)
        file_mb.config(menu=file_menu)
        file_menu.add_command(label="Открыть", command=lambda: print("Open"))
        file_menu.add_command(label="Сохранить", command=lambda: print("Save"))
        file_menu.add_separator()
        # file_menu.add_command(label="Выход", command=parent.quit)
        print('add menu file')

        # «Вид»
        view_mb = self._make_menubutton("Вид")
        view_menu = tk.Menu(view_mb, tearoff=0)
        view_mb.config(menu=view_menu)

        view_menu.add_checkbutton(
            label="Полноэкранный режим",
            # variable=parent.fullscreen_var,
            #command=self.toggle_fullscreen,
            # image=self.icons.get("fullscreen"),
            compound=tk.LEFT,
        )
        view_menu.add_separator()
        #view_menu.add_command(label="Сбросить размер", command=self.reset_size)
        # print('image', self.icons.get("fullscreen"))

    # def create_widgets(self):
    #     # Создаем панель инструментов
    #     toolbar = tk.Frame(self, bg='lightgray')
    #     toolbar.pack(side=tk.TOP, fill=tk.X)
    #
    #     # Добавляем кнопки с изображениями
    #     for name in ["doc", "mail", "calc", "xfe", "run", "web", "dev", "ai", "ded", "ktimer", "poweroff", "exit"]:
    #         if name in self.images:
    #             btn = tk.Button(
    #                 toolbar,
    #                 image=self.images[name],
    #                 compound=tk.TOP,
    #                 text=name.capitalize(),
    #                 command=lambda n=name: self.button_click(n)
    #             )
    #             btn.image = self.images[name]  # Сохраняем ссылку на изображение
    #             btn.pack(side=tk.LEFT, padx=2, pady=2)
    #
    #     # control_frame = ttk.Frame(self)
    #     # control_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=8, pady=4)
    #     checkb = ttk.Checkbutton(
    #         toolbar,
    #         image=self.images["fullscreen"],
    #         compound=tk.TOP,
    #         text="fullscreen",
    #         variable=self.fullscreen_var,
    #         command=self.toggle_fullscreen
    #     )
    #     checkb.image = self.images["fullscreen"]  # Сохраняем ссылку на изображение
    #     checkb.pack(side=tk.LEFT, padx=2, pady=2)
    #
    def _make_menubutton(self, label_text):
        mb = tk.Menubutton(
            self.frame,
            text=label_text,
            relief=tk.RAISED,
            bd=1,
            indicatoron=True,
            direction="below",
            bg="#f0f0f0",
        )
        mb.pack(side=tk.LEFT, padx=2, pady=2)
        return mb

    def pack(self, **kwargs):
        """Позволяет родителю вызвать pack у фрейма меню"""
        self.frame.pack(side=tk.TOP, fill=tk.X, **kwargs)
        
        
