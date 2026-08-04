# modules/chat/chat.py
import tkinter as tk
from tkinter import scrolledtext


class ChatPanel(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # Создаем виджеты чата
        self.text_area = scrolledtext.ScrolledText(self, wrap=tk.WORD)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        # Добавляем панель ввода
        self.entry = tk.Entry(self)
        self.entry.pack(fill=tk.X)

        # Привязываем события
        self.entry.bind("<Return>", self.send_message)

    def send_message(self, event=None):
        message = self.entry.get()
        self.text_area.insert(tk.END, f"Вы: {message}\n")
        self.entry.delete(0, tk.END)
