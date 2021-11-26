import tkinter as tk
import datetime
import random
import socket
import sqlite3

from tkinter import Message, font, messagebox


class Application():

    def __init__(self):
        window = tk.Tk()
        window.geometry("400x400")
        window.title("Zephyrus Database Saver")
        Custom_Font = tk.font.Font(family='cambria', size=10)

        USER_NAME_TEXT = tk.Label(window, text='Username', font=Custom_Font)
        USER_NAME_TEXT.place(x=200, y=125, anchor='center')
        self.USER_NAME_ENTRY = tk.Entry(window, bd=3)
        self.USER_NAME_ENTRY.place(x=200, y=150, anchor="center")

        PASSWORD_TEXT = tk.Label(window, text='Password', font=Custom_Font)
        PASSWORD_TEXT.place(x=200, y=180, anchor='center')
        self.PASSWORD_ENTRY = tk.Entry(window, bd=3)
        self.PASSWORD_ENTRY.place(x=200, y=205, anchor='center')
        LOGIN_BUTTON = tk.Button(window, text='LOGIN', font=Custom_Font,
                                 command=self.Check_Login_details)
        LOGIN_BUTTON.place(x=200, y=250, anchor='center')
        self.MENU_FRAME = tk.Frame(window)

        window.mainloop()

    def CHANGE_FRAME(MENU_FRAME, status=False):
        if status:
            pass
        else:
            return False

    def _database(Check_Login_details):
        conn = sqlite3.connect('011223054.db')
        conn.execute('''CREATE TABLE IF NOT EXISTS LOGIN_DETAILS
        ( username TEXT, password TEXT);''')
        conn.execute(
            "INSERT INTO LOGIN_DETAILS(username, password) VALUES ('Admin-Zeph', 'Z1')")
        cursor = conn.cursor()

        def check_detail_match(*args, **kwargs):
            username, password, MENU_FRAME = Check_Login_details(
                *args, **kwargs)
            view = cursor.execute(
                'SELECT * FROM LOGIN_DETAILS WHERE username=? AND password=?', (username, password))
            if view.fetchone():
                print(messagebox.showinfo('Success', 'Login Successful'))
                MENU_FRAME.pack(fill='both', expand=True)
            else:
                print(messagebox.showinfo(
                    'Invalid', 'Invalid Login Crendentials'))
        return check_detail_match

    @_database
    def Check_Login_details(self):

        username = self.USER_NAME_ENTRY.get()
        password = self.PASSWORD_ENTRY.get()
        return username, password, self.MENU_FRAME


obj = Application()
obj.main()
