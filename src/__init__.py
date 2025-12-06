from tkinter import *
from tkinter import Menu
from tkinter import messagebox
import tkinter as tk
import time
import subprocess


window = Tk()  
window.title("STARTXPY")  
#window.geometry('400x250')
window.attributes("-fullscreen", True)

def clicked():
    messagebox.showinfo('Заголовок', 'Текст')

def exec_calc():
    subprocess.Popen('/usr/bin/galculator')

def exec_doc():
    subprocess.Popen('/usr/bin/writer')

def exec_xfe():
    subprocess.Popen('/usr/bin/xfe')

def exec_run():
    subprocess.Popen('/usr/bin/xfe')

def exec_term():
    subprocess.Popen('/usr/bin/lxterminal')

def exec_ad():
    subprocess.Popen('/usr/bin/galculator')

def ded():
    messagebox.showinfo('ded', 'DED')     

def exec_ktimer():
    subprocess.Popen('/usr/bin/ktimer')

window.option_add("*tearOff", FALSE)

photo_mail = PhotoImage(file =r"../data/mail.png")
photo_web = PhotoImage(file =r"../data/web.png")
photo_doc = PhotoImage(file =r"../data/doc.png")
photo_xfe = PhotoImage(file =r"../data/xfe.png")
photo_calc = PhotoImage(file =r"../data/calc.png")
photo_dev = PhotoImage(file =r"../data/dev.png")
photo_run = PhotoImage(file =r"../data/run.png")
photo_ded = PhotoImage(file =r"../data/ded.png")
photo_ai = PhotoImage(file =r"../data/ai.png")
photo_exit = PhotoImage(file =r"../data/exit.png")
photo_ktimer = PhotoImage(file =r"../data/ktimer.png")

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

window.option_add("*tearOff", FALSE)
window.config(menu=menu)

#
#
#

def update_time():
    current_time = time.strftime('%A, %d.%m.%Y, %H:%M')
    statusbar.config(text=current_time)
    statusbar.after(1000, update_time)

statusbar = tk.Label(window, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
statusbar.pack(side=tk.BOTTOM, fill=tk.X)

update_time()

window.mainloop()
