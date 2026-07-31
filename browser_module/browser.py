# browser_module/browser.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl

from .utils import check_url, get_user_agent

class BrowserWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.web_view = QWebEngineView()
        self.layout.addWidget(self.web_view)
        self.setLayout(self.layout)
        
    def load_url(self, url):
        self.web_view.setUrl(QUrl(url))
        
    def clear_history(self):
        self.web_view.history().clear()
