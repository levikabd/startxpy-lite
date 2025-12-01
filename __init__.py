from tkinter import *
from tkinter import Menu
from tkinter import messagebox

window = Tk()  
window.title("STARTXPY")  
window.geometry('400x250')  

def clicked():
    messagebox.showinfo('Заголовок', 'Текст')     

def ded():
    messagebox.showinfo('ded', 'DED')     

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
#item_3.add_command(label='dev', command=clicked)
menu.add_command(label='dev', command=clicked)

item_4 = Menu(menu)
#item_4.add_command(label='DED', command=ded)
menu.add_command(label='DED', command=ded)

item_5 = Menu(menu)
#item_5.add_command(label='exit', command=clicked)
menu.add_command(label='exit', command=clicked)

window.config(menu=menu)  

window.mainloop()
