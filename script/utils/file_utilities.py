import os
import tkinter as tk
from tkinter import filedialog

__all__ = [
    'save_in_same_directory',
    'get_file_name',
    'choose_file_dialog',
    'choose_file'
]

def save_in_same_directory(original_file_path, file_name):
    directory = os.path.dirname(original_file_path)
    save_path = os.path.join(directory, file_name)
    return save_path

    
def get_file_name(__file__):
    file_path = os.path.abspath(__file__)
    file_name = os.path.basename(file_path)
    return file_name

def choose_file_dialog(filetype):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(
        filetypes=filetype,
        title="Select a file"
    )

    root.destroy()
    print(f"Selected File: {file_path}")
    return file_path

def choose_file():
    return choose_file_dialog([("All files", "*.*"), ("TIF files", "*.tif *.tiff"), ("LIF files", "*.lif")])
