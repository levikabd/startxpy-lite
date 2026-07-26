import os
from tkinter import *
from tkinter import Menu
from tkinter import messagebox
import tkinter as tk
import time
import subprocess
from tkinter import simpledialog

import datetime
import sys
import psutil

import window

window = Tk()  
window.title("STARTXPY")  
#window.geometry('400x250')
window.attributes("-fullscreen", True)

window.option_add("*tearOff", FALSE)
window.config(menu=menu)

def update_time():
    current_time = time.strftime('%A, %d.%m.%Y, %H:%M')
    statusbar.config(text=current_time)
    statusbar.after(1000, update_time)

statusbar = tk.Label(window, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
statusbar.pack(side=tk.BOTTOM, fill=tk.X)

update_time()

window.mainloop()
