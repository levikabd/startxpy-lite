import tkinter as tk
import os
from mixins.layout import LayoutMixin
from mixins.menubar import MenubarMixin
from mixins.click import ClickMixin
from mixins.statusbar import StatusbarMixin
# from mixins.chat import ChatMixin

#class MainWindow(tk.Tk, LayoutMixin, MenubarMixin, ToolbarMixin):
class MainWindow(tk.Tk, LayoutMixin, MenubarMixin, ClickMixin, StatusbarMixin):
        def __init__(self):
                super().__init__()
                self.base_dir = os.path.dirname(os.path.abspath(__file__))
                self.is_fullscreen = True
                self.fullscreen_var = tk.BooleanVar()
                self.fullscreen_var.set(self.is_fullscreen)

                self.icons = {}

                self.setup_layout()
                self.setup_menu()
                self.setup_statusbar()

