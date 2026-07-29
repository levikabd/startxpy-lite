import os
import sys
from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout, QTextEdit, QFrame
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView

def get_resource_path(relative_path: str) -> str:
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
        base_path = os.path.join(base_path, "..", "..")
    return os.path.normpath(os.path.join(base_path, relative_path))

class ChatPanel(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Чат: сообщения появятся здесь...")
        self.setReadOnly(True)
        self.setStyleSheet("background:#f7f9fc; border:1px solid #ccc; font-family:sans-serif; padding:8px;")

    def append_message(self, text: str):
        self.append(text)
        self.verticalScrollBar().setValue(self.verticalScrollBar().maximum())

class BrowserPanel(QWebEngineView):
    def __init__(self):
        super().__init__()
        # Стартовая страница — ya.ru
        self.setUrl(QUrl("https://ya.ru"))

class SplitterLayout(QWidget):
    """
    Центральная область:
      - DED выкл: только main_content
      - DED вкл: main_content | chat_panel | browser_panel
    Виджеты добавляются один раз, дальше только show/hide.
    """
    def __init__(self, main_content, chat_panel, browser_panel):
        super().__init__()
        self.main_content = main_content
        self.chat_panel = chat_panel
        self.browser_panel = browser_panel

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)
        self._ded_active = False

        # Добавляем все виджеты сразу
        self.layout.addWidget(self.main_content, stretch=2)
        self.layout.addWidget(self.chat_panel, stretch=1)
        self.layout.addWidget(self.browser_panel, stretch=1)

        # По умолчанию скрываем чат и браузер
        self.chat_panel.hide()
        self.browser_panel.hide()

    def set_ded_active(self, active: bool):
        self._ded_active = active
        if active:
            self.chat_panel.show()
            self.browser_panel.show()
        else:
            self.chat_panel.hide()
            self.browser_panel.hide()
