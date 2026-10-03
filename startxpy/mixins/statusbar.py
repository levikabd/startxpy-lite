import tkinter as tk
import os
from tkinter import PhotoImage
from datetime import datetime

class StatusbarMixin:
    def setup_statusbar(self):
        self.statusbar_frame = tk.Frame(self, borderwidth=2, relief=tk.RAISED)
        self.statusbar_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.status_icon = None
        # pathOnline = None
        # path = os.path.join(self.image_path, 'online12.gif')
        path = os.path.join(self.image_path, 'online24.gif')
        if os.path.exists(path):
            try:
                # pathOnline = PhotoImage(file=path)
                self.status_icon = PhotoImage(file=path)
                #print(f"Path to status icon: {path} - OK.")
            except Exception as e:
                print(f"Ошибка загрузки {path}: {str(e)}")
        else:
            print(f"Предупреждение: изображение {path} не найдено")

        # --- Left part: status text + color + border ---
        self.status_label = tk.Label(
            self.statusbar_frame,
            text="Online",
            # image=pathOnline,
            image=self.status_icon,
            compound=tk.LEFT,
            anchor=tk.W,
            bg="#e0f7fa",
            fg="#0277bd",
            relief=tk.SUNKEN,
            bd=1,
            padx=5,
            pady=2
        )
        self.status_label.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # --- Right part: version ---
        # self.status_right = ttk.Label(
        #     self.statusbar_frame,
        #     text="v1.0.0",
        #     anchor=tk.E,
        #     padding=(5, 2)
        # )
        # self.status_right.pack(side=tk.RIGHT, padx=(0, 5))

        # --- Time and date ---
        # We just set a fixed background color instead of trying to take it from ttk.Frame.
        # clock_bg = "#f0f0f0"  # edit it to fit your theme
        clock_bg = "#e0f7fa"  #
        self.status_clock = tk.Label(
            self.statusbar_frame,
            text="",
            anchor=tk.E,
            bg=clock_bg,
            fg="#0277bd",
            #     fg="#0277bd",
            #     relief=tk.SUNKEN,
            #     bd=1,
            padx=5,
            pady=2
        )
        self.status_clock.pack(side=tk.RIGHT)
        self._update_clock()

    def _update_clock(self):
        now = datetime.now()
        time_str = now.strftime("%H:%M")
        date_str = now.strftime("%d.%m.%Y")
        self.status_clock.config(text=f"{time_str} | {date_str}")
        self.after(15000, self._update_clock)

    def set_status(self, message: str):
        if hasattr(self, "status_label"):
            self.status_label.config(text=message)

    def clear_status(self):
        self.set_status("Online")
