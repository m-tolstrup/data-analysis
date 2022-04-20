from .view import View
from .components.data_table import DataTable
from .components.options_menu import OptionsMenu
from .components.file_selection import FileSelection


class TimeView(View):
    def __init__(self, master=None):
        super().__init__(master)

        self.timeDataTable = None
        self.timeOptionsMenu = None
        self.timeFileSelection = None

    def create_view(self, controller):
        # A view is the master of the components within it
        self.timeDataTable = DataTable(master=self, controller=controller)
        self.timeOptionsMenu = OptionsMenu(master=self, controller=controller)
        self.timeFileSelection = FileSelection(master=self, controller=controller)
