import tkinter as tk
import datetime
import random
import socket
from tkinter import *

class Application():
    def __init__(self):
        window = tk.Tk()
        window.geometry("400x400")
        window.title("Zephyrus Database Saver")
        self.Login_main(window)
        window.mainloop()
        Custom_Font = tk.Font()
        

    def Login_main(self, window):
         USER_NAME_TEXT = Label(window, text='UserName')
         USER_NAME_TEXT.place(x=200, y=125, anchor='center')
         USER_NAME_ENTRY = Entry(window, bd=3)
         USER_NAME_ENTRY.place(x=200, y=150, anchor="center")
         
         PASSWORD_TEXT = Label(window, text='Password')
         PASSWORD_TEXT.place(x=200, y=180, anchor='center')
         PASSWORD_ENTRY = Entry(window, bd=3)
         PASSWORD_ENTRY.place(x=200, y=205, anchor='center')

         LOGIN_BUTTON = Button(window, text='LOGIN')
         LOGIN_BUTTON.place(x=200, y=250, anchor='center')
        
       
obj = Application()
obj.main()