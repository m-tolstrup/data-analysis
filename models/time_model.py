from .model import Model


class TimeModel(Model):
    def __init__(self):
        super().__init__()

        self.data_frame = None
        self.total_rows = 0

    def add_time_column(self):
        # time_list first contains which second of the day the job was finished
        time_list = []
        for row in range(self.total_rows):
            # Split the "timestamp" (string) given in the .csv-file
            time = self.data_frame.iloc[row, 0].split()
            # Split the hour:min:sec string
            time = time[3].split(':')
            # Convert hour:min:sec to integer from strings
            time = [int(unit) for unit in time]
            # Adds the 'second' of the day where the job was completed
            time_list.append(time[0] * 3600 + time[1] * 60 + time[2])
