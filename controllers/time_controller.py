from tkinter import filedialog

from .controller import Controller

import os
from os import walk
import datetime
import pandas as pd


class TimeController(Controller):
    def __init__(self, model=None, status_bar=None):
        super().__init__(model, status_bar)

        self.data_path = None

    def bind(self, view):
        self.view = view
        self.view.create_view(self)

    def choose_file(self):
        # Prompts user to choose the file to load
        try:
            data_path = filedialog.askopenfilename()

            if data_path == "" and self.data_path is None:
                # When no path has ever been chosen and no path was selected
                self.status_bar.set_status("Der blev ikke valgt en fil")
            elif data_path == "":
                # When a path has been chosen before, but no new path was selected
                self.view.timeFileSelection.toggle_button("Indlæs data", False)
                self.status_bar.set_status("Der blev ikke valgt en ny fil")
            elif not data_path.endswith(".csv"):
                # The chosen file is not a .csv file
                self.view.timeFileSelection.toggle_button("Indlæs data", False)
                self.status_bar.set_status("Den valgte fil var ikke en .csv-fil")
            else:
                # A path was chosen
                self.data_path = data_path
                self.status_bar.set_status("Fil valgt")
                self.view.timeFileSelection.toggle_button("Indlæs data", True)
                self.view.timeFileSelection.update_entry_text("Fil sti", self.data_path)
        except Exception as e:
            # Very broad exception - might not be thrown ever, but better safe than sorry
            # I am mainly scared of filedialog window
            self.view.timeFileSelection.toggle_button("Indlæs data", False)
            self.status_bar.set_status(f"Det opstod en fejl. Fejlbesked: {e}")

    def load_data_from_file(self, load_single_file: bool):

        self.status_bar.set_status("Indlæser data...")

        # TODO check if new data is actually gonna be loaded

        if load_single_file:
            self.model.data_frame = pd.read_csv(self.data_path,
                                                header=None,
                                                delimiter=";",
                                                usecols=[0, 3],
                                                encoding="ISO-8859-1")
        else:
            # Split path into path name and the file extension
            directory_path = os.path.dirname(self.data_path)

            all_files = []
            # Find ALL the files at the path directory
            for (dirpath, dirname, file) in walk(directory_path):
                all_files.extend(file)

            # Remove files that do not start with 'orders' and ends with '.csv'
            all_files = [file for file in all_files if file.startswith("orders_") and file.endswith(".csv")]
            # Update file names to contain directory path
            all_files = [directory_path + '/' + file for file in all_files]

            # Sort by date
            all_files = sorted(all_files,
                               key=lambda x: datetime.datetime.strptime(x, directory_path + '/orders_%d_%m_%Y.csv'))

            # Load all files into data frames
            data_frame_list = []
            for file in all_files:
                df = pd.read_csv(file, header=None, delimiter=";", usecols=[0, 3], encoding="ISO-8859-1")
                data_frame_list.append(df)

            # Set the data frame of the model to a concatenation of data frames loaded above
            self.model.data_frame = pd.concat(data_frame_list, axis=0, ignore_index=True)

        # Set the total_rows variable
        self.model.total_rows = len(self.model.data_frame)
        # Add a column that contains the time it took to finish a given job
        self.model.add_time_column()

        self.status_bar.set_status("Data indlæst")
