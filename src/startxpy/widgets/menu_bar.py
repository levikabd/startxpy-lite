from PyQt6.QtWidgets import QMenuBar, QWidget, QToolButton, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QIcon, QAction  # <-- QAction теперь из QtGui
from PyQt6.QtCore import Qt

import os
import sys

def get_resource_path(relative_path: str) -> str:
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
        base_path = os.path.join(base_path, "..", "..")
    return os.path.normpath(os.path.join(base_path, relative_path))

class MenuBar(QMenuBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent_window = parent

        # Контейнер для кнопок (в той же строке, что и меню)
        toolbar_widget = QWidget()
        toolbar_layout = QHBoxLayout()
        toolbar_layout.setContentsMargins(0, 0, 0, 0)
        toolbar_layout.setSpacing(2)

        # --- Меню «Файл» ---
        file_menu = self.addMenu("&Файл")
        act_exit = QAction("&Выход", self)
        act_exit.triggered.connect(self.parent_window.close)
        file_menu.addAction(act_exit)

        # Спейсер: меню слева, кнопки справа
        spacer = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        toolbar_layout.addSpacerItem(spacer)

        # --- Кнопки-иконки ---
        buttons_config = [
            ("AI", "ai.gif"),
            ("Calc", "calc.gif"),
            ("DED", "ded.gif"),
            ("Dev", "dev.gif"),
            ("Doc", "doc.gif"),
            ("Mail", "mail.gif"),
            ("Timer", "ktimer.gif"),
            ("Web", "web.gif"),
            ("Exit", "exit.gif"),
        ]

        for label, icon_name in buttons_config:
            btn = QToolButton()
            btn.setText(label)
            icon_path = get_resource_path(f"data/icons/{icon_name}")
            if os.path.isfile(icon_path):
                btn.setIcon(QIcon(icon_path))
            btn.setFixedSize(50, 40)
            btn.clicked.connect(lambda checked, lbl=label: self.parent_window.on_taskbar_click(lbl))
            toolbar_layout.addWidget(btn)

        toolbar_widget.setLayout(toolbar_layout)
        self.addWidget(toolbar_widget)

        # --- Меню «Вид» ---
        view_menu = self.addMenu("&Вид")
        self.act_toggle_ded = QAction("&Режим DED", self)
        self.act_toggle_ded.setCheckable(True)
        self.act_toggle_ded.triggered.connect(self.parent_window.toggle_ded_mode)
        view_menu.addAction(self.act_toggle_ded)

        act_fullscreen = QAction("&Полноэкранный режим", self)
        act_fullscreen.setShortcut("F11")
        act_fullscreen.triggered.connect(self.parent_window.toggle_fullscreen)
        view_menu.addAction(act_fullscreen)
