import tkinter as tk
import datetime
import random
import socket
from tkinter import font

class Application():
    def __init__(self):
        window = tk.Tk()
        window.geometry("400x400")
        window.title("Zephyrus Database Saver")
        Custom_Font = tk.font.Font(family='cambria', size=10)
        self.Login_main(window, Custom_Font)
        window.mainloop()
        
        

    def Login_main(self, window, Custom_Font):
         USER_NAME_TEXT = tk.Label(window, text='UserName', font=Custom_Font)
         USER_NAME_TEXT.place(x=200, y=125, anchor='center')
         USER_NAME_ENTRY = tk.Entry(window, bd=3)
         USER_NAME_ENTRY.place(x=200, y=150, anchor="center")
         
         PASSWORD_TEXT = tk.Label(window, text='Password', font=Custom_Font)
         PASSWORD_TEXT.place(x=200, y=180, anchor='center')
         PASSWORD_ENTRY = tk.Entry(window, bd=3)
         PASSWORD_ENTRY.place(x=200, y=205, anchor='center')

         LOGIN_BUTTON = tk.Button(window, text='LOGIN', font=Custom_Font)
         LOGIN_BUTTON.place(x=200, y=250, anchor='center')
        
       
obj = Application()
obj.main()