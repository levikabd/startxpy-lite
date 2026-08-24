import tkinter as tk
from pathlib import Path

class LayoutMixin:
    def setup_layout(self):
        self.title("startxpy")
        # self.geometry("1024x768")
        self.attributes("-fullscreen", True)

        # path to logo
        base_dir = Path(__file__).resolve().parent.parent.parent
        icon_path = base_dir / "assets" / "icons" / "startxpy-logo-64.gif"
        #icon_path = base_dir / "assets" / "icons" / "startxpy-logo-32.gif"
        if icon_path.exists():
            self.iconphoto(False, tk.PhotoImage(file=str(icon_path)))
        else:
            print("Not logo!")

    def toggle_fullscreen(self):
        self.is_fullscreen = self.fullscreen_var.get()
        if self.is_fullscreen:
            self.attributes("-fullscreen", True)
        else:
            self.attributes("-fullscreen", False)
            # self.geometry("1024x768")
            # self.state("zoomed")
            width = self.winfo_screenwidth()
            height = self.winfo_screenheight()
            self.geometry(f"{width}x{height}")
        # print(f"[Меню] Полноэкранный: {'ВКЛ' if self.is_fullscreen else 'ВЫКЛ'}")

    # def reset_size(self):
    #     self.attributes("-fullscreen", False)
    #     self.geometry("1024x768")
    #     self.is_fullscreen = False
    #     # self.fullscreen_var.set(False)
    #     # self.toolbar.set_fullscreen(False)

    def on_escape(self, event=None):
        self.is_fullscreen = not self.is_fullscreen
        self.fullscreen_var.set(self.is_fullscreen)
        self.toggle_fullscreen()

