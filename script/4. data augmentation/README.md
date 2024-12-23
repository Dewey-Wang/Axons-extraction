# **Image Augmentation**

This script provides a comprehensive pipeline for applying data augmentation techniques to medical imaging datasets, particularly in `.tif` or `.tiff` formats. The script integrates functions for loading data, applying transformations, saving augmented images and masks, and visualizing the results using Napari.

---

## **Features**
1. **File Loading**:
   - Uses the `file_utilities` module for selecting preprocessed images and label images. If you use my script, it should be named `bg_remove.tiff` for a preprocessed image and `label_wih_border_mask_3.tif` for a label image.
   - Compatible with `.tif` and `.tiff` formats.

2. **Data Augmentation**:
   - Leverages the `torchio` library for applying a wide range of 3D medical imaging transformations.
   - Supports composable transformations to generate diverse augmentation combinations.

3. **Visualization**:
   - Uses Napari to visualize the augmented images and masks.
   - Displays both original and augmented images for easy comparison.

4. **Saving Augmented Data**:
   - Automatically organizes augmented data into separate folders for images and masks.
   - Ensures augmented files are saved in the `Augmentation/` directory.

5. **Customizable Transformations**:
   - Includes predefined transformations such as `RandomGamma` and `RandomFlip`.
   - Easily extendable to include additional transformations from `torchio`.

---

## **How It Works**

### **1. File Selection**
The script allows users to select input image and label files using a file dialog:
```python
image_file_path = fu.choose_file()
label_file_path = fu.choose_file()
```

### **2. Transformations**
Define and compose a list of transformations:
```python
transforms_list = [
    tio.transforms.RandomGamma(),
    tio.RandomFlip(axes=('LR'), flip_probability=1),
    #Any transformations from `torchio` could be used
]
transforms_combinations = compose_transforms(transforms_list)
```

### **3. Apply Transformations**
For each transformation combination, the script applies the transformations to the input image and label, and stores the results in dictionaries:
```python
images, masks = apply_transforms_and_save(subjects, combination, transpose=True)
```

### **4. Save Augmented Data**
The augmented images and masks are saved in a structured directory under `Augmentation/`:
```python
save_images_from_dict(images, original_folder_name, suffix)
save_images_from_dict(masks, original_folder_name, suffix)

```
- suffix: (Optional) A string appended to the file names to indicate specific transformations or additional metadata.
   - If provided, the suffix will be added to the base file name of each saved file, helping distinguish between files processed with different transformations.
   - If omitted, the original keys from the dictionary will be used as the file names.

#### **Folder Structure**
The augmented data is saved in the following structure:
```plaintext
Augmentation/
├── <original_folder_name>/
│   ├── image/   # Augmented images
│   ├── mask/    # Augmented masks
```
#### **Augmentation Folder Location**
The `Augmentation/` folder is saved in the current working directory where the script is executed. This is determined by `os.getcwd()`.
For example:
If you execute the script in `/home/user/project/`, the `Augmentation/` folder will be created at `/home/user/project/Augmentation/`.

---

### **5. Visualization**
Visualize the augmented results using Napari:
```python
viewer = show_transformed_images(images, viewer)
```

---

## **Dependencies**
- `torchio`: For applying medical imaging transformations.
- `napari`: For visualizing images and masks.
- `file_utilities`: Custom module for file handling.
- `itertools`: For generating combinations of transformations.
- `tifffile`: For handling `.tif` file operations.
- `numpy`: For array manipulations.

---

## **Contact**
For any questions or issues, please contact:
**Ding Yang Wang**  
[deweywang2000@gmail.com](mailto:deweywang2000@gmail.com)
