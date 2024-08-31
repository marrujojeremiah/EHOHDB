import tkinter as tk
from login_screen import LoginScreen
from main_screen import MainScreen

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("EHOH Client Database")
        self.geometry("800x600")

        self.show_login_screen()

    def show_login_screen(self):
        login_screen = LoginScreen(self)
        login_screen.grid(padx=10, pady=10)

        login_screen.login_button.config(command=lambda: self.show_main_screen(login_screen))

    def show_main_screen(self, role):
        self.clear_screen()

        main_screen = MainScreen(self, role)
        main_screen.grid(padx=10, pady=10)

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
