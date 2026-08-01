<<<<<<< HEAD
import sys
from PyQt6.QtWidgets import QApplication
from src.startxpy.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
=======
# main.py
import tkinter as tk
from modules.window import Application
from browser_module import BrowserWidget

class MainApp(Application):
    def __init__(self):
        super().__init__()
        self.browser = BrowserWidget()
        
        # Добавляем браузер в основное окно
        self.browser_frame = tk.Frame(self.content_frame)
        self.browser_frame.pack(fill=tk.BOTH, expand=True)
        
        # Встраиваем PyQt виджет в Tkinter окно
        self.browser.setParent(self.browser_frame)
        self.browser.setGeometry(0, 0, 800, 600)
        
        # Пример использования
        self.browser.load_url("https://ya.ru")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
>>>>>>> py_only
