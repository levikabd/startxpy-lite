import tkinter as tk
import os
from src.mixins.layout import LayoutMixin
from src.mixins.menubar import MenubarMixin
from src.mixins.click import ClickMixin
from src.mixins.statusbar import StatusbarMixin
from src.mixins.dev_toolbar import DevToolbarMixin
# from mixins.chat import ChatMixin

#class MainWindow(tk.Tk, LayoutMixin, MenubarMixin, ToolbarMixin):
class MainWindow(tk.Tk, LayoutMixin, MenubarMixin, ClickMixin, StatusbarMixin, DevToolbarMixin):
        def __init__(self):
                super().__init__()
                self.base_dir = os.path.dirname(os.path.abspath(__file__))
                self.is_fullscreen = True
                self.fullscreen_var = tk.BooleanVar()
                self.fullscreen_var.set(self.is_fullscreen)

                self.icons = {}

                self.setup_layout()

                # menu=self.setup_menu()
                # self.setup_dev_toolbar(menu)
                self.setup_menu()
                self.setup_dev_toolbar(self)

                self.setup_statusbar()

