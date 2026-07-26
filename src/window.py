import os
from tkinter import *
from tkinter import Menu
from tkinter import messagebox
import tkinter as tk
import subprocess
from tkinter import simpledialog

# import time
# import datetime
# import sys
# import psutil

def clicked():
    messagebox.showinfo('Заголовок', 'Текст')

def exec_calc():
    subprocess.Popen('/usr/bin/galculator')

def exec_doc():
    subprocess.Popen('/usr/bin/writer')

def exec_xfe():
    subprocess.Popen('/usr/bin/xfe')

def exec_run():
    cmd = simpledialog.askstring("Enter cmd", "Enter CMD:")
    subprocess.Popen(cmd)

def exec_term():
    subprocess.Popen('/usr/bin/lxterminal')

def exec_ad():
    subprocess.Popen('/usr/bin/galculator')

def ded():
    messagebox.showinfo('ded', 'DED')     

def exec_ktimer():
    subprocess.Popen('/usr/bin/ktimer')

def exec_poweroff():
    subprocess.Popen('/usr/bin/sudo', '/usr/sbin/shutdown')

# window.option_add("*tearOff", FALSE)

#"""Возвращает абсолютный нормализованный путь к картинке в папке data"""
def get_image_path(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, "..", "data", filename)
    return os.path.normpath(path)

# Словарь: ключ — имя переменной/логическое имя, значение — объект PhotoImage
images = {}

# Загружаем сразу несколько GIF
for name, filename in [
    ("ai", "ai.gif"),
    ("calc", "calc.gif"),
    ("ded", "ded.gif"),
    ("dev", "dev.gif"),
    ("doc", "doc.gif"),
    ("exit", "exit.gif"),
    ("ktimer", "ktimer.gif"),
    ("mail", "mail.gif"),
    ("poweroff", "poweroff.gif"),
    ("run", "run.gif"),
    ("web", "web.gif"),
    ("xfe", "xfe.gif")
]:
    path = get_image_path(filename)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Картинка не найдена: {path}")
    images[name] = PhotoImage(file=path)

# Теперь можно использовать картинки по ключу:
# photo_mail = images["mail"]
# photo_settings = images["settings"]

# Получаем директорию, где лежит текущий файл (__init__.py)
#base_dir = os.path.dirname(os.path.abspath(__file__))
# Строим абсолютный путь к картинке
#image_path = os.path.join(base_dir, "..", "data", "mail.gif")
#image_path = os.path.normpath(image_path)  # убирает лишние точки, делает путь чистым
#photo_mail = PhotoImage(file =r"../data/mail.gif")

# photo_mail = PhotoImage(file =image_path)
# photo_web = PhotoImage(file =r"../data/web.gif")
# photo_doc = PhotoImage(file =r"../data/doc.gif")
# photo_xfe = PhotoImage(file =r"../data/xfe.gif")
# photo_calc = PhotoImage(file =r"../data/calc.gif")
# photo_dev = PhotoImage(file =r"../data/dev.gif")
# photo_run = PhotoImage(file =r"../data/run.gif")
# photo_ded = PhotoImage(file =r"../data/ded.gif")
# photo_ai = PhotoImage(file =r"../data/ai.gif")
# photo_exit = PhotoImage(file =r"../data/exit.gif")
# photo_ktimer = PhotoImage(file =r"../data/ktimer.gif")
# photo_poweroff = PhotoImage(file =r"../data/poweroff.gif")

photo_ai = images["ai"]
photo_calc = images["calc"]
photo_ded = images["ded"]
photo_dev = images["dev"]
photo_doc = images["doc"]
photo_exit = images["exit"]
photo_ktimer = images["ktimer"]
photo_mail = images["mail"]
photo_poweroff = images["poweroff"]
photo_run = images["run"]
photo_web = images["web"]
photo_xfe = images["xfe"]

menu = Menu(window)

item_0 = Menu(menu)
#item_0.add_command(label='mail', command=clicked)
menu.add_command(label='mail', command=clicked, image = photo_mail, compound=TOP)

item_1 = Menu(menu)
#item_1.add_command(label='doc', command=clicked)
menu.add_command(label='doc',command=clicked, image = photo_doc, compound=TOP)

item_21 = Menu(menu)
#item_21.add_command(label='web', command=clicked)
menu.add_command(label='files',command=exec_xfe, image = photo_xfe, compound=TOP)

item_22 = Menu(menu)
#item_22.add_command(label='web', command=clicked)
menu.add_command(label='calc',command=exec_calc, image = photo_calc, compound=TOP)

item_2 = Menu(menu)
#item_2.add_command(label='web', command=clicked)
menu.add_command(label='web',command=clicked, image = photo_web, compound=TOP)

item_23 = Menu(menu)
#item_23.add_command(label='web', command=clicked)
item_23.add_command(label='menu-find', command=clicked)
item_23.add_command(label='terminal', command=exec_term)
item_23.add_command(label='run', command=exec_run)
menu.add_cascade(label='run', menu=item_23, image = photo_run, compound=TOP)

item_3 = Menu(menu)
item_3.add_command(label='VSCODE', command=clicked)
item_3.add_command(label='pycharm', command=clicked)
item_3.add_command(label='ERIC', command=clicked)
item_3.add_command(label='QTcreator', command=clicked)
item_3.add_command(label='geany', command=clicked)
item_3.add_command(label='git', command=clicked)
item_3.add_command(label='fm', command=clicked)
item_3.add_command(label='term', command=clicked)
#menu.add_command(label='dev', command=clicked)
menu.add_cascade(label='dev', menu=item_3, image = photo_dev, compound=TOP)

item_4 = Menu(menu)
#item_4.add_command(label='DED', command=ded)
menu.add_command(label='DED', command=ded, image = photo_ded, compound=TOP)

item_5 = Menu(menu)
item_5.add_command(label="Cursor", command=clicked)
item_5.add_command(label="Claude code", command=clicked)
item_5.add_command(label="Perplexity", command=clicked)
item_5.add_command(label="Cluely", command=clicked)
item_5.add_command(label="LangChain", command=clicked)
item_5.add_command(label="Gemini Veo", command=clicked)
item_5.add_command(label="Firefly", command=clicked)
item_5.add_command(label="Reve Jmage", command=clicked)
item_5.add_command(label="Notebook LM", command=clicked)
item_5.add_command(label="GPT yandex", command=clicked) 
item_5.add_command(label="Chat GPT", command=clicked) 
item_5.add_command(label="Yupyter", command=clicked) 
item_5.add_command(label="Easy Diffusion", command=clicked) 
#menu.add_cascade(label="File", menu=item_5)
#item_5.add_command(label='DED', command=ded)
#menu.add_command(label='DED', command=ded)
menu.add_cascade(label='AI', menu=item_5, image = photo_ai, compound=TOP)

item_6 = Menu(menu)
#item_6.add_command(label='exit', command=clicked)
menu.add_command(label='exit', command=lambda: window.destroy(), image = photo_exit, compound=TOP)
item_7 = Menu(menu)
#item_7.add_command(label='exit', command=clicked)
menu.add_command(label='ktimer', command=exec_ktimer, image = photo_ktimer, compound=TOP)
item_8 = Menu(menu)
#item_8.add_command(label='exit', command=clicked)
menu.add_command(label='poweroff', command=exec_poweroff, image = photo_poweroff, compound=TOP)
