import tkinter as tk
from pathlib import Path

class LayoutMixin:
    def setup_layout(self):
        self.title("startxpy")
        self.geometry("1024x768")
        # self.content_frame = tk.Frame(self)
        # self.content_frame.pack(fill=tk.BOTH, expand=True)

        # path to logo
        base_dir = Path(__file__).resolve().parent.parent.parent  # аналог dirname(abspath(__file__))
        icon_path = base_dir / "assets" / "icons" / "startxpy-logo-64.gif"
        #icon_path = base_dir / "assets" / "icons" / "startxpy-logo-32.gif"
        if icon_path.exists():
            self.iconphoto(False, tk.PhotoImage(file=str(icon_path)))
        else:
            print("Not logo!")

        # self.fullscreen_var = tk.BooleanVar(value=True)
        # self.is_fullscreen = True
