from PyQt6.QtWidgets import (
    QToolBar, QMenu, QToolButton, QWidget, QHBoxLayout, QSizePolicy
)
from PyQt6.QtGui import QIcon, QAction
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

class TopBar(QToolBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent_window = parent
        self.setMovable(False)
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.setStyleSheet("QToolBar { spacing: 2px; padding: 4px; }")

        # Контейнер с горизонтальной компоновкой, в него и будем класть всё
        container = QWidget()
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(4)
        container.setLayout(layout)

        # --- Меню «Файл» (как кнопка с выпадающим меню) ---
        file_menu = QMenu("&Файл", self)
        act_exit = QAction("&Выход", self)
        act_exit.triggered.connect(self.parent_window.close)
        file_menu.addAction(act_exit)

        btn_file = QToolButton()
        btn_file.setText("Файл ▼")
        btn_file.setMenu(file_menu)
        btn_file.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        layout.addWidget(btn_file)

        # Спейсер: прижимает кнопки вправо от «Файл»
        spacer_left = QWidget()
        spacer_left.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        layout.addWidget(spacer_left)

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
            layout.addWidget(btn)

        # Спейсер: прижимает «Вид» к правому краю
        spacer_right = QWidget()
        spacer_right.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        layout.addWidget(spacer_right)

        # --- Меню «Вид» (как кнопка с выпадающим меню) ---
        view_menu = QMenu("&Вид", self)

        self.act_toggle_ded = QAction("&Режим DED", self)
        self.act_toggle_ded.setCheckable(True)
        self.act_toggle_ded.triggered.connect(self.parent_window.toggle_ded_mode)
        view_menu.addAction(self.act_toggle_ded)

        act_fullscreen = QAction("&Полноэкранный режим", self)
        act_fullscreen.setShortcut("F11")
        act_fullscreen.triggered.connect(self.parent_window.toggle_fullscreen)
        view_menu.addAction(act_fullscreen)

        btn_view = QToolButton()
        btn_view.setText("Вид ▼")
        btn_view.setMenu(view_menu)
        btn_view.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        layout.addWidget(btn_view)

        # Добавляем контейнер с layout в тулбар
        self.addWidget(container)

