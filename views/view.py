import tkinter as tk
from abc import abstractmethod


class View(tk.Frame):
    def __init__(self, master=None):
        super().__init__()

        self.master = master

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky=tk.E + tk.W)

    @abstractmethod
    def create_view(self, controller):
        raise NotImplementedError
