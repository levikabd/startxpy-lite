import tkinter as tk
import tkinter.messagebox as mb
from startxpy.utils.launcher import launch_ide

class DevToolbarMixin:
    def setup_dev_toolbar(self):
        self.dev_menu = tk.Menu(self.btn_dev, tearoff=0)

        ides = [
            ("PyCharm", "pycharm"),
            ("VSCode", "code"),
            ("Cursor", "cursor"),
            ("Geany", "geany"),
            ("QtCreator", "qtcreator"),
        ]

        for label, ide_name in ides:
            self.dev_menu.add_command(
                label=label,
                command=lambda name=ide_name: self.on_ide_select(name)
            )

        self.dev_menu.add_separator()
        self.dev_menu.add_command(
            label="Cancel",
            command=lambda: self.dev_menu.unpost()
        )

        def show_menu():
            x = self.btn_dev.winfo_rootx()
            y = self.btn_dev.winfo_rooty() + self.btn_dev.winfo_height()
            self.dev_menu.post(x, y)
            self.bind("<Escape>", lambda e: self.dev_menu.unpost())

        self.btn_dev.config(command=show_menu)
        # return toolbar

    def on_ide_select(self, ide_name: str):
        success = launch_ide(ide_name)
        if not success:
            mb.showerror(
                "Couldn't start IDE",
                f"Couldn't start {ide_name}.\n"
                "Check:\n"
                "- Is this IDE installed on the system\n"
                "- Is there a command in the PATH (for example, 'code', 'pycharm')\n"
                "See the console for details."
            )
