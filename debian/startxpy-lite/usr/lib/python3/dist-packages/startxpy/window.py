import tkinter as tk
import os

from startxpy.mixins.layout import LayoutMixin
from startxpy.mixins.menubar import MenubarMixin
from startxpy.mixins.click import ClickMixin
from startxpy.mixins.statusbar import StatusbarMixin
from startxpy.mixins.dev_toolbar import DevToolbarMixin
from startxpy.utils.run import CommandRunnerMixin
from startxpy.utils.shutdown import CommandShutdownMixin

class MainWindow(
    tk.Tk,
    LayoutMixin,
    MenubarMixin,
    ClickMixin,
    StatusbarMixin,
    DevToolbarMixin,
    CommandRunnerMixin,
    CommandShutdownMixin
):
    def __init__(self):
        super().__init__()
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.is_fullscreen = False
        self.fullscreen_var = tk.BooleanVar(value=self.is_fullscreen)
        self.icons = {}
        self.run_with_output = True
        self._init_ui()

    def _init_ui(self):
        self.setup_layout()
        self.setup_menu()
        self.setup_dev_toolbar()
        self.setup_run_button()
        # self.setup_pwr_button()
        self.setup_statusbar()
