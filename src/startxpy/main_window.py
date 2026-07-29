import os
import sys
import subprocess
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

from .widgets.top_bar import TopBar
from .widgets.status_bar import StatusBar
from .widgets.panels import SplitterLayout, ChatPanel, BrowserPanel


def get_resource_path(relative_path: str) -> str:
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
        base_path = os.path.join(base_path, "..", "..")
    return os.path.normpath(os.path.join(base_path, relative_path))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StartXPy")
        self.resize(1200, 800)

        icon_path = get_resource_path("data/icons/mail.gif")
        if os.path.isfile(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Верхняя панель: меню и кнопки в одной строке
        self.top_bar = TopBar(self)
        self.addToolBar(self.top_bar)

        # Основное содержимое (заглушка)
        self.main_content = QLabel("<h1>StartXPy</h1><p>Основное окно.</p>")
        self.main_content.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_content.setStyleSheet("font-size:18px; padding:40px; color:#333;")

        # Чат и браузер (для DED-режима)
        self.chat = ChatPanel()
        self.browser = BrowserPanel()

        # Сплиттер (переключатель DED)
        self.splitter = SplitterLayout(self.main_content, self.chat, self.browser)
        main_layout.addWidget(self.splitter, stretch=1)

        # Статусбар (внизу: сообщение + часы + запущенные программы)
        self.status = StatusBar(self)
        self.setStatusBar(self.status)

        self._is_fullscreen = True
        self._ded_active = False

        # Сразу включаем полноэкран
        self.showFullScreen()
        self.status.showMessage("Полноэкранный режим (по умолчанию)", 0)

    # --- Обработчик кнопок (теперь они в TopBar) ---
    def on_taskbar_click(self, label: str):
        msg = f"Нажата кнопка: {label}"
        self.status.showMessage(msg, 0)

        if label == "DED":
            self.toggle_ded_mode()
        elif label == "Exit":
            self.close()
        elif label == "Doc":
            self.open_doc()
        elif label == "Web":
            url = "https://ya.ru"
            self.status.showMessage("Запуск внешнего браузера...", 3000)
            try:
                subprocess.Popen(["xdg-open", url])
            except Exception as e:
                self.status.showMessage(f"Ошибка запуска браузера: {e}", 5000)
        else:
            # Сюда можно добавить логику для AI, Dev, Timer и т.п.
            pass

    def open_doc(self):
        path = get_resource_path("data/index.html")
        import os
        if os.path.isfile(path):
            from PyQt6.QtCore import QUrl
            self.browser.setUrl(QUrl.fromLocalFile(path))
            self.status.showMessage("Открыт index.html в панели браузера", 3000)
            if not self._ded_active:
                self.toggle_ded_mode()
        else:
            self.status.showMessage("Файл data/index.html не найден.", 5000)

    def toggle_ded_mode(self):
        self._ded_active = not self._ded_active
        self.splitter.set_ded_active(self._ded_active)
        state_text = "Режим DED: ВКЛ (чат + браузер)" if self._ded_active else "Режим DED: ВЫКЛ"
        self.status.showMessage(state_text, 0)
        self.top_bar.act_toggle_ded.setChecked(self._ded_active)

    def toggle_fullscreen(self):
        self._is_fullscreen = not self._is_fullscreen
        if self._is_fullscreen:
            self.showFullScreen()
            self.status.showMessage("Полноэкранный режим", 3000)
        else:
            self.showNormal()
            self.status.showMessage("Обычный режим", 3000)

    def update_running_list(self, programs: list[str]):
        self.status.set_running_programs(programs)

