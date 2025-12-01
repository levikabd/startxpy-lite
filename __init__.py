from tkinter import *
from tkinter import ttk

root = Tk()
root.title("startxpy")
root.geometry("250x200")


def click():
    window = Tk()
    window.title("Новое окно")
    window.geometry("400x250")


button = ttk.Button(text="Создать окно", command=click)
button.pack(anchor=CENTER, expand=1)

root.mainloop()
