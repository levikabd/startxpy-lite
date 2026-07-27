import os
import time
import subprocess
import tkinter as tk
from tkinter import Menu, messagebox, simpledialog, PhotoImage

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("STARTXPY")
        # Раскомментируй строку ниже, если нужен полный экран. 
        # Для отладки лучше сначала запустить без него, чтобы видеть ошибки.
        self.attributes("-fullscreen", True) 
        #self.geometry("800x600")  # Размер для отладки, потом можно убрать
        
        self.option_add("*tearOff", False)

        # --- НАДЁЖНЫЙ РАСЧЁТ ПУТИ К ИКОНКАМ ---
        # Мы находимся в: ~/yadi/DEVEL/startxpy/src/startxpy/main_window.py
        # Нам надо попасть в: ~/yadi/DEVEL/startxpy/data/icons
        current_file = os.path.abspath(__file__)
        base_dir = os.path.dirname(current_file)           # .../src/startxpy
        project_root = os.path.dirname(os.path.dirname(base_dir))  # .../startxpy (корень проекта)
        data_path = os.path.join(project_root, "data", "icons")
        
        #print(f"[DEBUG] Ищем иконки в: {data_path}") # Это поможет увидеть в терминале, куда смотрит скрипт

        def get_image_path(filename):
            return os.path.join(data_path, filename)

        # --- ЗАГРУЗКА ИКОНОК ---
        self.images = {}
        icons_list = [
            ("ai", "ai.gif"), ("calc", "calc.gif"), ("ded", "ded.gif"),
            ("dev", "dev.gif"), ("doc", "doc.gif"), ("exit", "exit.gif"),
            ("ktimer", "ktimer.gif"), ("mail", "mail.gif"),
            ("poweroff", "poweroff.gif"), ("run", "run.gif"),
            ("web", "web.gif"), ("xfe", "xfe.gif")
        ]

        for name, filename in icons_list:
            path = get_image_path(filename)
            if not os.path.exists(path):
                print(f"[WARNING] Картинка не найдена: {path}")
                self.images[name] = None
                continue
            try:
                self.images[name] = PhotoImage(file=path)
                #print(f"[OK] Загружена: {filename}")
            except Exception as e:
                print(f"[ERROR] Не удалось загрузить {filename}: {e}")
                self.images[name] = None

        # --- МЕНЮ ---
        menu = Menu(self)
        self.config(menu=menu)

        def clicked():
            messagebox.showinfo('Заголовок', 'Текст')

        def exec_calc():
            run_safe(['galculator'])

        def exec_doc():
            # ИСПРАВЛЕНО: вместо /usr/bin/writer -> libreoffice --writer
            run_safe(['libreoffice', '--writer'])

        def exec_xfe():
            run_safe(['xfe'])

        def exec_run():
            cmd = simpledialog.askstring("Enter cmd", "Enter CMD:")
            if cmd:
                try:
                    subprocess.Popen(cmd.split())
                except Exception as e:
                    messagebox.showerror("Ошибка запуска", str(e))

        def exec_term():
            run_safe(['lxterminal'])

        def ded():
            messagebox.showinfo('ded', 'DED')

        def exec_ktimer():
            run_safe(['ktimer'])

        def exec_poweroff():
            # Внимание: sudo требует настройки visudo
            try:
                subprocess.Popen(['sudo', '/usr/sbin/shutdown', 'now'])
            except Exception as e:
                messagebox.showerror("Ошибка выключения", str(e))

        # Вспомогательная функция для безопасного запуска программ
        def run_safe(cmd_list):
            try:
                subprocess.Popen(cmd_list)
            except FileNotFoundError:
                msg = f"Программа не найдена: {' '.join(cmd_list)}\nУстановите её через apt."
                messagebox.showwarning("Программа не установлена", msg)
            except Exception as e:
                messagebox.showerror("Ошибка", str(e))

        # Вспомогательная функция для добавления пункта с иконкой
        def add_cmd(label, command, image_name=None):
            img = self.images.get(image_name)
            menu.add_command(label=label, command=command, image=img, compound=tk.TOP)

        add_cmd('mail', clicked, 'mail')
        add_cmd('doc', exec_doc, 'doc')
        add_cmd('files', exec_xfe, 'xfe')
        add_cmd('calc', exec_calc, 'calc')
        add_cmd('web', clicked, 'web')

        # Подменю run
        item_run = Menu(menu, tearoff=False)
        item_run.add_command(label='menu-find', command=clicked)
        item_run.add_command(label='terminal', command=exec_term)
        item_run.add_command(label='run', command=exec_run)
        menu.add_cascade(label='run', menu=item_run, image=self.images.get('run'), compound=tk.TOP)

        # Подменю dev
        item_dev = Menu(menu, tearoff=False)
        dev_items = ['VSCODE', 'pycharm', 'ERIC', 'QTcreator', 'geany', 'git', 'fm', 'term']
        for item in dev_items:
            item_dev.add_command(label=item, command=clicked)
        menu.add_cascade(label='dev', menu=item_dev, image=self.images.get('dev'), compound=tk.TOP)

        # Пункт DED
        add_cmd('DED', ded, 'ded')

        # Подменю AI
        item_ai = Menu(menu, tearoff=False)
        ai_items = [
            "Cursor", "Claude code", "Perplexity", "Cluely", "LangChain",
            "Gemini Veo", "Firefly", "Reve Jmage", "Notebook LM",
            "GPT yandex", "Chat GPT", "Yupyter", "Easy Diffusion"
        ]
        for item in ai_items:
            item_ai.add_command(label=item, command=clicked)
        menu.add_cascade(label='AI', menu=item_ai, image=self.images.get('ai'), compound=tk.TOP)

        # Остальные пункты
        add_cmd('exit', lambda: self.destroy(), 'exit')
        add_cmd('ktimer', exec_ktimer, 'ktimer')
        add_cmd('poweroff', exec_poweroff, 'poweroff')

        # Статусбар
        self.statusbar = tk.Label(self, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.statusbar.pack(side=tk.BOTTOM, fill=tk.X)

        self.update_time()

    def update_time(self):
        current_time = time.strftime('%A, %d.%m.%Y, %H:%M')
        self.statusbar.config(text=current_time)
        self.after(1000, self.update_time)
