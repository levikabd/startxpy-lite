import tkinter as tk
from ..utils.launcher import launch_ide

class DevToolbarMixin:
    def setup_dev_toolbar(self, parent):
        toolbar = tk.Frame(parent, relief=tk.RAISED, bd=1)
        toolbar.pack(side=tk.TOP, fill=tk.X, padx=4, pady=4)

        dev_menu = tk.Menu(self, tearoff=0)
        dev_menu.add_command(label="PyCharm", command=lambda: self.on_ide_select("pycharm"))
        dev_menu.add_command(label="VSCode", command=lambda: self.on_ide_select("vscode"))
        dev_menu.add_command(label="Cursor", command=lambda: self.on_ide_select("cursor"))
        dev_menu.add_command(label="Geany", command=lambda: self.on_ide_select("geany"))
        dev_menu.add_command(label="QtCreator", command=lambda: self.on_ide_select("qtcreator"))

        mb = tk.Menubutton(
            toolbar,
            text="Dev ▼",
            menu=dev_menu,
            relief=tk.RAISED,
            padx=10,
            pady=4,
            cursor="hand2"
        )
        mb.pack(side=tk.LEFT, padx=2)

        return toolbar

    def on_ide_select(self, ide_name: str):
        # Если хочешь открывать конкретный проект — подставь путь сюда
        project_path = None  # например: "/home/lev/yadi/DEVEL/startxpy"
        success = launch_ide(ide_name, project_path=project_path)
        if not success:
            # Тут можно добавить всплывающее окно с ошибкой, если нужно
            pass
