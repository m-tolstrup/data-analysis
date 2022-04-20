import tkinter as tk
from views.components.component import Component


class FileSelection(Component):
    def __init__(self, master, controller):
        super().__init__(master, controller)

        self.load_single_file = tk.BooleanVar()

        self.frame = tk.LabelFrame(master=self.master)
        self.frame.grid(row=0, column=0, sticky=tk.W + tk.E, padx=5, pady=5, columnspan=2)

        self.create_label(self.frame, "Nuværende sti: ", row=0, column=0)
        self.create_entry(self.frame, "Fil sti", width=45, row=0, column=1, padx=5, pady=10, ipadx=70)
        self.create_button(self.frame, "Vælg fil", row=0, column=2, padx=5)
        self.buttons["Vælg fil"]["command"] = lambda: self.controller.choose_file()
        self.create_button(self.frame, "Indlæs data", row=0, column=3, padx=5)
        self.buttons["Indlæs data"]["command"] = lambda: \
            self.controller.load_data_from_file(self.load_single_file.get())
        self.buttons["Indlæs data"]["state"] = tk.DISABLED
        self.create_checkbutton(self.frame, "Indlæs kun den valgte fil", self.load_single_file, row=0, column=4)

