import tkinter as tk
import datetime
import random
import socket
import sqlite3

from tkinter import Menu, Message, font, messagebox


class Application_LOGIN():

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("400x400")
        self.window.title("Zephyrus Database Saver")
        self.Custom_Font = tk.font.Font(family='cambria', size=10)

        USER_NAME_TEXT = tk.Label(
            self.window, text='Username', font=self.Custom_Font)
        USER_NAME_TEXT.place(x=200, y=125, anchor='center')
        self.USER_NAME_ENTRY = tk.Entry(self.window, bd=3)
        self.USER_NAME_ENTRY.place(x=200, y=150, anchor="center")

        self.PASSWORD_ENTRY = tk.Entry(self.window, bd=3)
        self.PASSWORD_ENTRY.place(x=200, y=205, anchor='center')
        LOGIN_BUTTON = tk.Button(self.window, text='LOGIN', font=self.Custom_Font,
                                 command=self.Check_Login_details)
        LOGIN_BUTTON.place(x=200, y=250, anchor='center')

        """IF LOGIN DETAILS ARE CORRECT THIS WILL RUN:OPTION_MENU_FRAME"""
        self.OPTION_MENU_FRAME()
        self.window.mainloop()

    def generate_and_save(self):
        for widgets in self.MENU_FRAME.winfo_children():
            widgets.destroy()
        self.add_Credentials_Frame = tk.LabelFrame(
            self.MENU_FRAME)
        self.add_Credentials_Frame.pack(padx=10, pady=10)

        USER_NAME_TEXT = tk.Label(
            self.window, text='Username', font=self.Custom_Font)
        USER_NAME_TEXT.place(x=200, y=125, anchor='center')
        PASSWORD_TEXT = tk.Label(
            self.window, text='Password', font=self.Custom_Font)
        PASSWORD_TEXT.place(x=200, y=180, anchor='center')

        self.save_username = tk.Entry(self.window)
        self.save_password = tk.Entry(self.window)
        self.save_username.place(x=200, y=150, anchor='center')
        self.save_password.place(x=200, y=205, anchor='center')

        Save_bttn = tk.Button(self.window, text='Save', font=self.Custom_Font)
        Save_bttn.place(x=200, y=250, anchor='center')

    def OPTION_MENU_FRAME(self):
        MENU_ITEMS = [self.generate_and_save]
        self.MENU_FRAME = tk.LabelFrame(self.window)
        self.MENU_FRAME.pack(padx=10, pady=10)
        ADD_LOGINS_BUTTON = tk.Button(
            self.MENU_FRAME, text="ADD LOGIN CREDENTIALS", font=self.Custom_Font, command=lambda: MENU_ITEMS[0]())
        ADD_LOGINS_BUTTON.place(x=110, y=80)

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


if __name__ == "__main__":
    obj = Application_LOGIN()
