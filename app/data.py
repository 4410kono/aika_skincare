import os
import pandas as pd


class Data:
    def get_data(self):
        """
        This function returns a Python dict.
        """

        root_dir = os.path.dirname(os.path.dirname(__file__))
        gsheet_path = os.path.join(root_dir, "data")
        file_name = os.listdir(gsheet_path)

        data = pd.read_csv(os.path.join(gsheet_path, file_name))

        return data
