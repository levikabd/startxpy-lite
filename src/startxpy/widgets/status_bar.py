from PyQt6.QtWidgets import QStatusBar, QLabel
from PyQt6.QtCore import QTimer, QDateTime

class StatusBar(QStatusBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet("font-family:sans-serif; font-size:11px; background:#f0f0f4;")

        # Слева: сообщения
        self.message_label = QLabel("StartXPy: готов к работе")
        self.message_label.setStyleSheet("color:#333; padding-left:10px;")
        # В QStatusBar сообщения выводятся встроенным виджетом, но мы можем держать свой label
        self.addWidget(self.message_label)

        # Посередине: часы (дата + время без секунд)
        self.time_label = QLabel()
        self.time_label.setStyleSheet("color:#555; font-weight:bold;")
        self.addPermanentWidget(self.time_label)

        # Справа: список запущенных программ
        self.running_label = QLabel("Запущено: —")
        self.running_label.setStyleSheet("color:#666; padding-right:10px; font-style:italic;")
        self.addPermanentWidget(self.running_label)

        self._update_time()

        timer = QTimer(self)
        timer.timeout.connect(self._update_time)
        timer.start(60000)  # раз в минуту

    def _update_time(self):
        now = QDateTime.currentDateTime().toString("dd.MM.yyyy HH:mm")
        self.time_label.setText(f"Дата/время: {now}")

    # Публичный метод для внешнего вызова: используем showMessage (стандарт PyQt)
    def showMessage(self, text: str, timeout: int = 0):
        # timeout=0 — сообщение висит, пока не сменится
        super().showMessage(text, timeout)
        # Плюс обновляем наш label слева, чтобы было видно всегда
        self.message_label.setText(text)

    def set_running_programs(self, programs: list[str]):
        if not programs:
            self.running_label.setText("Запущено: —")
            return
        joined = ", ".join(programs)
        if len(joined) > 60:
            joined = joined[:57] + "..."
        self.running_label.setText(f"Запущено: {joined}")

