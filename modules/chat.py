import tkinter as tk
from tkinter import scrolledtext, messagebox


class ChatPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Создаем виджеты чата
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        # Область для сообщений
        self.messages = scrolledtext.ScrolledText(
            self,
            width=50,
            height=10,
            state=tk.DISABLED,
            font=("Arial", 12)
        )
        self.messages.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Поле ввода сообщения
        self.entry = tk.Entry(
            self,
            width=50,
            font=("Arial", 12)
        )
        self.entry.pack(fill=tk.X, padx=5, pady=2)

        # Кнопка отправки
        self.send_button = tk.Button(
            self,
            text="Отправить",
            command=self.send_message
        )
        self.send_button.pack(pady=2)

        # Привязываем Enter
        self.entry.bind("<Return>", self.send_message)

    def send_message(self, event=None):
        message = self.entry.get().strip()
        if message:
            self.add_message(f"Вы: {message}")
            self.entry.delete(0, tk.END)

    def add_message(self, message):
        # Включаем редактирование
        self.messages.config(state=tk.NORMAL)
        # Добавляем сообщение
        self.messages.insert(tk.END, message + "\n")
        # Прокручиваем до конца
        self.messages.see(tk.END)
        # Отключаем редактирование
        self.messages.config(state=tk.DISABLED)

    def clear_chat(self):
        self.messages.config(state=tk.NORMAL)
        self.messages.delete(1.0, tk.END)
        self.messages.config(state=tk.DISABLED)

    def show_error(self, message):
        messagebox.showerror("Ошибка", message)
