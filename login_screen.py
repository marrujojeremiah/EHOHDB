import tkinter as tk
from tkinter import messagebox
from database import get_user

class LoginScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create the layout for login screen
        self.grid(padx=10, pady=10)

        # Username label and entry
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        # Password label and entry
        self.password_label = tk.Label(self, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        # Login button
        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.grid(row=2, column=1, padx=10, pady=10, sticky="e")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Retrieve user data from the database
        user = get_user(username)
        if user and user[2] == password:
            role = user[3]  # Get the user role from the database
            self.master.show_main_screen(role)
        else:
            messagebox.showerror("Login", "Invalid username or password.")
