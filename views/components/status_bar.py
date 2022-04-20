import tkinter as tk


class StatusBar:
    def __init__(self, master):
        self.master = master

        self.status_label = tk.Label(self.master, text="Status: Klar", anchor=tk.W, padx=15)
        self.status_label.grid(row=2, column=0, sticky=tk.W + tk.E)
        self.status_label.config(bd=1, relief=tk.SUNKEN, font="lucida 12 italic")

    def set_status(self, status: str):
        self.status_label.config(text=f'Status: {status}', font="lucida 12 italic")
