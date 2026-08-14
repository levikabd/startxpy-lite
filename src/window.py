import tkinter as tk
import os
from mixins.layout import LayoutMixin
from mixins.menubar import MenubarMixin
# from mixins.menu_and_toolbar import MenuToolbarMixin
# from mixins.menu_and_toolbar import MenuToolbarMixin
# from mixins.menu_and_toolbar import MenuToolbarMixin

#class MainWindow(WindowLayoutMixin, MenuToolbarMixin):
class MainWindow(tk.Tk, LayoutMixin, MenubarMixin):
        def __init__(self):
                super().__init__()
                self.base_dir = os.path.dirname(os.path.abspath(__file__))
                self.icons = {}

                self.setup_layout()
                self.setup_menu()
                #self.setup_toolbar()
