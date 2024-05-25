#My emaial yousafwahiwal3@gmail.com
from tkinter import messagebox
import tkinter as tk
import sqlite3 as sq

sc = tk.Tk()
sc.title("Registration and login program")
def register():
    username = entry_un.get()
    password = entry_p.get()

    if username == "" or password == "":
        messagebox.showerror("Eror", "Username and Password cannot be empty")
        return

    c.execute("SELECT * FROM users WHERE username=?", (username,))
    if c.fetchone():
        messagebox.showerror("username problem", "Username already exists")
    else:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("Done", "Account created successfully")


def login():
    username = entry_un.get()
    password = entry_p.get()

    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    if c.fetchone():
        messagebox.showinfo("Done", "You are logged in successfully")
    else:
        messagebox.showerror("Login denied", "Invalid Username or Password")


label_un = tk.Label(sc, text="Username")
label_un.grid(row=0, column=0, padx=10, pady=10)
entry_un = tk.Entry(sc)
entry_un.grid(row=0, column=1, padx=10, pady=10)
label_p = tk.Label(sc, text="Password")
label_p.grid(row=1, column=0, padx=10, pady=10)
entry_p = tk.Entry(sc, show="*")
entry_p.grid(row=1, column=1, padx=10, pady=10)

button_reg = tk.Button(sc, text="Register", command=register)
button_reg.grid(row=2, column=0, padx=10, pady=10)
button_login = tk.Button(sc, text="Login", command=login)
button_login.grid(row=2, column=1, padx=10, pady=10)


conn = sq.connect('userdata.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
    )
''')
conn.commit()


sc.mainloop()
conn.close()
