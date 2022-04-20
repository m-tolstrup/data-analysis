import tkinter as tk
from views.components.component import Component


class OptionsMenu(Component):
    def __init__(self, master, controller):
        super().__init__(master, controller)

        self.frame = tk.LabelFrame(master=self.master)
        self.frame.grid(row=1, column=0, padx=5, pady=5)

        self.auto_update_table = tk.BooleanVar()
        self.create_button(self.frame, "Opdater tabel", row=0, column=0, padx=5, pady=5, ipadx=25)
        # TODO add button function
        self.buttons["Opdater tabel"]["state"] = tk.DISABLED
        self.create_checkbutton(self.frame, "Opdater automatisk", self.auto_update_table, row=0, column=1, padx=5, pady=5, ipadx=25)

        self.create_label(self.frame, "Typer:", row=1, column=0)
        self.labels["Typer:"].grid(columnspan=2)
        self.create_list_box(self.frame, "Typer", tk.StringVar(value=[]), row=2, column=0, padx=5, ipadx=80)
        self.list_boxes["Typer"].grid(columnspan=2)
        self.create_button(self.frame, "Fokuser typer", row=3, column=0, padx=5, pady=5, ipadx=25)
        # TODO add button function
        self.buttons["Fokuser typer"]["state"] = tk.DISABLED
        self.create_button(self.frame, "Fjern typer", row=3, column=1, padx=5, pady=5, ipadx=25)
        # TODO add button function
        self.buttons["Fjern typer"]["state"] = tk.DISABLED
        self.create_button(self.frame, "Nulstil typer", row=4, column=0, padx=5, pady=5, ipadx=25)
        # TODO add button function
        self.buttons["Nulstil typer"]["state"] = tk.DISABLED
        self.create_button(self.frame, "Rediger typer", row=4, column=1, padx=5, pady=5, ipadx=25)
        # TODO add button function
        self.buttons["Rediger typer"]["state"] = tk.DISABLED

        self.create_label(self.frame, "Serier:", row=5, column=0)
        self.labels["Serier:"].grid(columnspan=2)
        self.create_list_box(self.frame, "Serier", tk.StringVar(value=[]), row=6, column=0, padx=5, ipadx=80)
        self.list_boxes["Serier"].grid(columnspan=2)
        self.create_button(self.frame, "Fokuser serier", row=7, column=0, padx=5, pady=5, ipadx=25)
        # TODO add button function
        self.buttons["Fokuser serier"]["state"] = tk.DISABLED
        self.create_button(self.frame, "Fjern serier", row=7, column=1, padx=5, pady=5, ipadx=25)
        # TODO add button function
        self.buttons["Fjern serier"]["state"] = tk.DISABLED
        self.create_button(self.frame, "Nulstil serier", row=8, column=0, padx=5, pady=5, ipadx=25)
        # TODO add button function
        self.buttons["Nulstil serier"]["state"] = tk.DISABLED
        self.create_button(self.frame, "Rediger serier", row=8, column=1, padx=5, pady=5, ipadx=25)
        # TODO add button function
        self.buttons["Rediger serier"]["state"] = tk.DISABLED

        self.create_label(self.frame, "Tidsintervaller:", row=9, column=0)
        self.labels["Tidsintervaller:"].grid(columnspan=2)
        self.create_list_box(self.frame, "Tidsint", tk.StringVar(value=[]), row=10, column=0, padx=5, ipadx=80)
        self.list_boxes["Tidsint"].grid(columnspan=2)
        self.create_button(self.frame, "Tilføj interval", row=11, column=0, padx=5, pady=5, ipadx=25)
        # TODO add button function
        self.buttons["Tilføj interval"]["state"] = tk.DISABLED
        self.create_button(self.frame, "Fjern valgte", row=11, column=1, padx=5, pady=5, ipadx=25)
        # TODO add button function
        self.buttons["Fjern valgte"]["state"] = tk.DISABLED
        self.create_label(self.frame, "Fra (min.):", row=13, column=0, padx=5, pady=5, ipadx=25)
        self.create_entry(self.frame, "tid_min", width=10, row=13, column=1, padx=5, pady=5, ipadx=25)
        self.create_label(self.frame, "Til (min.):", row=14, column=0, padx=5, pady=5, ipadx=25)
        self.create_entry(self.frame, "tid_max", width=10, row=14, column=1, padx=5, pady=5, ipadx=25)


