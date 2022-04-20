import tkinter as tk
from tkinter import ttk


class Notebook(ttk.Notebook):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

    def new_tab(self, controller, view, name: str):
        controller.bind(view)
        self.add(view, text=name)
