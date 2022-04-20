import tkinter as tk
from tkinter import ttk
from views.components.component import Component


class DataTable(Component):
    def __init__(self, master, controller):
        super().__init__(master, controller)

        self.frame = tk.LabelFrame(master=self.master)
        self.frame.grid(row=1, column=1, padx=5, pady=5)

        self.tree_view = ttk.Treeview(self.frame)
        self.tree_view.grid(row=0, column=0)
        self.tree_view['columns'] = ("Serie", "Type", "Antal", "Total tid", "Snit pr. styk")
