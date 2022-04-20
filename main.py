import tkinter as tk

from views import TimeView
from views.components import StatusBar, Notebook
from models import TimeModel
from controllers import TimeController

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Data Analyse Værktøj")
    root.grid_columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    app = Notebook(master=root)

    statusBar = StatusBar(master=root)

    # Named "time" since the data analysis is mainly about time spent per job
    timeModel = TimeModel()
    timeView = TimeView(master=root)
    timeController = TimeController(model=timeModel, status_bar=statusBar)
    app.new_tab(view=timeView, controller=timeController, name="Tid Analyse")

    app.mainloop()
