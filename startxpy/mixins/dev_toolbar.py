import tkinter as tk
import tkinter.messagebox as mb
from startxpy.utils.launcher import launch_ide

class DevToolbarMixin:
    def setup_dev_toolbar(self, parent):
        # Панель с кнопками (твой текущий стиль)
        # toolbar = tk.Frame(parent, relief=tk.RAISED, bd=1)
        # toolbar.pack(side=tk.TOP, fill=tk.X, padx=4, pady=4)
        # btn = tk.Button(
        #     toolbar,
        #     text="Dev ▼",
        #     relief=tk.RAISED,
        #     padx=10,
        #     pady=4,
        #     cursor="hand2"
        # )
        # btn.pack(side=tk.LEFT, padx=2)
        # btn = self.btn_dev

        # Меню действий (выпадает по кнопке)
        self.dev_menu = tk.Menu(parent, tearoff=0)

        ides = [
            ("PyCharm", "pycharm"),
            ("VSCode", "code"),
            ("Cursor", "cursor"),
            ("Geany", "geany"),
            ("QtCreator", "qtcreator"),
        ]

        for label, ide_name in ides:
            # Фиксируем ide_name в лямбде, чтобы не было «последнего значения»
            self.dev_menu.add_command(
                label=label,
                command=lambda name=ide_name: self.on_ide_select(name)
            )
            # if label =="Cancel":
            #     self.dev_menu.config(command=self.dev_menu.unpost())

        # Разделитель перед «Отменой» (опционально, для красоты)
        self.dev_menu.add_separator()
        self.dev_menu.add_command(
            label="Cancel",
            command=lambda: self.dev_menu.unpost()
        )

        def show_menu():
            x = self.btn_dev.winfo_rootx()
            y = self.btn_dev.winfo_rooty() + self.btn_dev.winfo_height()
            self.dev_menu.post(x, y)
            parent.bind("<Escape>", lambda e: self.dev_menu.unpost())

        self.btn_dev.config(command=show_menu)
        # return toolbar

    def on_ide_select(self, ide_name: str):
        # project_path = "/home/lev/yadi/DEVEL/startxpy"  # подставь свой путь или сделай динамическим
        # success = launch_ide(ide_name, project_path=project_path)
        success = launch_ide(ide_name)

        if not success:
            mb.showerror(
                "Не удалось запустить IDE",
                f"Не получилось запустить {ide_name}.\n"
                "Проверьте:\n"
                "- Установлена ли эта IDE в системе\n"
                "- Есть ли команда в PATH (например, 'code', 'pycharm')\n"
                "Смотрите консоль для подробностей."
            )

