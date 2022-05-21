import os
import requests
import openpyxl
import traceback
import validators
import pandas as pd


class DownloadContent(object):

    file_path = ''
    sheet_name = ''
    file_type = ''

    def __init__(self, file_path, sheet_name, file_type) -> None:
        self.file_path = file_path
        self.file_type = file_type
        self.sheet_name = sheet_name
        self.read_file_type()

    def read_file_type(self):
        file_path = str(self.file_path)
        full_path = os.path.join(os.getcwd(), 'mediafiles')
        full_path = os.path.join(full_path, file_path)
        file_name = full_path.split('/')[-1]

        print("file name is ", file_name)

        df = pd.read_excel(full_path, sheet_name=self.sheet_name)
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

        print("data frame from here >>>>>>> ")
        print(df)

        if self.file_type == 'Life':
            self.life_call(file_name=file_name, sheet_name=self.sheet_name)
        else:
            self.school_call(file_name=file_name, sheet_name=self.sheet_name)


    def school_call(self, file_name, sheet_name):
        print("school call ======= ")

    def life_call(self, file_name, sheet_name):

        print("life call from upper functions ")


