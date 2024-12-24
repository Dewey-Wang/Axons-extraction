import os
import tifffile as tiff
from tkinter import filedialog, Tk, messagebox

def load_or_check_datasets(directory_path):
    file_names = ['image_dataset.tiff', 'sharpened_img_dataset.tiff', 'mask_dataset.tiff']
    datasets = {}
    missing_files = []

    for file_name in file_names:
        file_path = os.path.join(directory_path, file_name)
        if os.path.exists(file_path):
            datasets[file_name] = tiff.imread(file_path)
            print(f"Loaded {file_name} from {file_path}")
        else:
            missing_files.append(file_name)
            print(f"{file_name} not found in {directory_path}")

    if missing_files:
        print(f"The following files are missing: {', '.join(missing_files)}")
        return datasets, missing_files
    else:
        print("All required files are loaded.")
        return datasets, None

def choose_directory_and_load_datasets():
    root = Tk()
    root.attributes("-topmost", True)
    root.withdraw()

    # 彈窗提醒
    messagebox.showinfo("Choose Directory", "Please choose a folder to check or load datasets.")

    directory_path = filedialog.askdirectory(
        title="Select a directory to check and load datasets"
    )
    root.destroy()

    if not directory_path:
        print("No directory selected.")
        return None

    datasets, missing_files = load_or_check_datasets(directory_path)
    if missing_files:
        print("Some files are missing.")
    else:
        print("All files loaded successfully.")
    
    return datasets, missing_files