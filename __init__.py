from tkinter import *
from tkinter import Menu
from tkinter import messagebox
import tkinter as tk
import time

window = Tk()  
window.title("STARTXPY")  
#window.geometry('400x250')
window.attributes("-fullscreen", True)


def clicked():
    messagebox.showinfo('Заголовок', 'Текст')     

def ded():
    messagebox.showinfo('ded', 'DED')     

window.option_add("*tearOff", FALSE)
menu = Menu(window)

item_0 = Menu(menu)
#item_0.add_command(label='mail', command=clicked)
menu.add_command(label='mail', command=clicked)  

item_1 = Menu(menu)
#item_1.add_command(label='doc', command=clicked)
menu.add_command(label='doc',command=clicked)

item_2 = Menu(menu)
#item_2.add_command(label='web', command=clicked)
menu.add_command(label='web',command=clicked)

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
menu.add_cascade(label='dev', menu=item_3)

item_4 = Menu(menu)
#item_4.add_command(label='DED', command=ded)
menu.add_command(label='DED', command=ded)

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
menu.add_cascade(label='AI', menu=item_5)
item_6 = Menu(menu)
#item_6.add_command(label='exit', command=clicked)
menu.add_command(label='exit', command=lambda: window.destroy())
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
