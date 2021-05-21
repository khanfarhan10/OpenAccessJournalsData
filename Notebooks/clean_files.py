"""
python clean_files.py
- & was changed to _ in filepath as Kaggle Datasets don't support it
"""

import os
ROOT_DIR = os.getcwd()
DATA_PATH = os.path.join(ROOT_DIR, "Journals_Metadata")


def clean_name(string):
    return string.replace("&", "_")


for path, subdirs, files in os.walk(DATA_PATH):
    for fname in files:
        if "&" in fname:
            file_path = os.path.join(path, fname)
            new_name = os.path.join(path, clean_name(fname))
            os.rename(file_path, new_name)
            print("Renamed :", file_path)
            print("To :", new_name)
