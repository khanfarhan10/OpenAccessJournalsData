"""
python clean_files.py
- & was changed to _ 
- = was changed to _ 
in filepath as Kaggle Datasets don't support it
Unfortunately we could not create your dataset.
File name contains invalid character (=):

Unfortunately we could not create your dataset.
File or directory name must not have leading or trailing whitespaces: CDC.json
"""

import os
import pandas as pd

ROOT_DIR = os.getcwd()
DATA_PATH = os.path.join(ROOT_DIR, "Journals_Metadata")

CHARS_TO_REPLACE = ["&", "="," "]
REPLACE_BY = "_"


def clean_name(string):
    for each_char in CHARS_TO_REPLACE:
        string = string.replace(each_char, REPLACE_BY)
    return string


for path, subdirs, files in os.walk(DATA_PATH):
    for fname in files:
        for each_char in CHARS_TO_REPLACE:
            if each_char in fname:
                file_path = os.path.join(path, fname)
                new_name = os.path.join(path, clean_name(fname))
                os.rename(file_path, new_name)
                print("Renamed :", file_path)
                print("To :", new_name)

CSV_PATH = os.path.join(ROOT_DIR,"MainOpenAccessJournalsData.csv")
EXCEL_PATH = os.path.join(ROOT_DIR,"MainOpenAccessJournalsData.xlsx")
df = pd.read_csv(CSV_PATH)
for each_char in CHARS_TO_REPLACE:
    df["Journals_Metadata_Paths"].replace([each_char,REPLACE_BY], regex=True,inplace=True)
df.to_excel(EXCEL_PATH,index=False)
df.to_csv(CSV_PATH,index=False)