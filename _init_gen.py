import os

def drop_all_files(directory):
    for r, d, f in os.walk(directory):
        for dirname in d:
            if dirname != '__pycache__':
                open(r + "\\" + str(dirname) + "\\__init__.py", "w+")
                drop_all_files(r + "\\" + str(dirname))

def build(directory):        
    drop_all_files(directory)