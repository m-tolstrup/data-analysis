import tkinter as tk


class Component:
    def __init__(self, master=None, controller=None):

        self.master = master
        self.controller = controller

        self.labels = {}
        self.buttons = {}
        self.entries = {}
        self.list_boxes = {}
        self.check_buttons = {}

    def create_label(self, frame, name, row, column, padx=0, pady=0, ipadx=0, ipady=0):
        self.labels[name] = tk.Label(frame)
        self.labels[name]["text"] = name
        self.labels[name].grid(row=row, column=column)
        self.labels[name].grid(padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)

    def create_button(self, frame, name, row, column, padx=0, pady=0, ipadx=0, ipady=0):
        self.buttons[name] = tk.Button(frame)
        self.buttons[name]["text"] = name
        self.buttons[name].grid(row=row, column=column)
        self.buttons[name].grid(padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)

    def create_checkbutton(self, frame, name, variable, row, column, padx=0, pady=0, ipadx=0, ipady=0):
        self.check_buttons[name] = tk.Checkbutton(frame)
        self.check_buttons[name]["text"] = name
        self.check_buttons[name]["variable"] = variable
        self.check_buttons[name].grid(row=row, column=column)
        self.check_buttons[name].grid(padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)

    def create_entry(self, frame, name, width, row, column, padx=0, pady=0, ipadx=0, ipady=0):
        self.entries[name] = tk.Entry(frame)
        self.entries[name]["width"] = width
        self.entries[name].grid(row=row, column=column)
        self.entries[name].grid(padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)

    def create_list_box(self, frame, name, entry_list, row, column, padx=0, pady=0, ipadx=0, ipady=0):
        self.list_boxes[name] = tk.Listbox(frame, selectmode='multiple')
        self.list_boxes[name]["listvariable"] = entry_list
        self.list_boxes[name]["height"] = 10
        self.list_boxes[name].grid(row=row, column=column)
        self.list_boxes[name].grid(padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)

    def toggle_button(self, button_name: str, enable: bool):
        if enable:
            self.buttons[button_name]["state"] = tk.NORMAL
        else:
            self.buttons[button_name]["state"] = tk.DISABLED

    def update_entry_text(self, entry_name: str, text: str):
        self.entries[entry_name].delete(0, tk.END)
        self.entries[entry_name].insert(0, text)
