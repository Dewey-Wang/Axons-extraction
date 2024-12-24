# **Utils Directory**

The `utils` directory contains a set of modular and reusable Python scripts designed to streamline key processes in the pipeline, such as file handling, image preprocessing, denoising, and user interaction.

---

## **Description**

| **File Name**                   | **Description**                                                                 |
|----------------------------------|---------------------------------------------------------------------------------|
| `LifFileProcessor.py`           | Functions for processing `.lif` microscopy files, including image integration and masking. |
| `capture_partial_image.py`      | Tool for interactively selecting and cropping regions of interest from images.   |
| `file_utilities.py`             | General file-handling utilities, such as file selection dialogs and directory management. |
| `QuestionMaster.py`             | Utility for interacting with users, including question prompts and input validation. |
| `BM4DProcessor.py`              | Specific implementation for BM4D denoising in the pipeline.                     |
| `image_processor.py`            | Handles `.tif` and `.lif` file processing. |
| `manual_correction_data_loader.py` | Loads and checks required datasets for manual corrections, ensuring all necessary files are present. |
| `napari_editor.py`              | Interactive tool for manual corrections and segmentations using Napari.         |
| `image_cropper.py`              | Automates the cropping of integrated images and applies 3D masks.               |

---

## **Files and Descriptions**

### **1. LifFileProcessor.py**
- **Purpose**: Provides functions for handling `.lif` microscopy files and extracting 3D image stacks.
- **Key Functions**:
  - `calculate_sum_of_series()`: Computes the total number of series from `.lif` metadata.
  - `select_images_by_series_number(serie_number)`: Selects image stacks based on the number of series.
  - `create_integrated_image(selected_list, z_list, x_list, y_list, channel_num)`: Combines 3D slices into a single integrated image.
  - `mask_3D_image(image_3D, cropped_image)`: Applies a cropped image mask to a 3D stack.

---

### **2. capture_partial_image.py**
- **Purpose**: Interactive tool for selecting and cropping regions of interest (ROIs) from images.
- **Key Features**:
  - Draws polygons interactively to define ROIs.
  - Saves cropped regions as `cropped_region.jpg`.
- **Key Controls**:
  - `r`: Reset the selection.
  - `s`: Save the ROI as `cropped_region.jpg`.

---

### **3. file_utilities.py**
- **Purpose**: Provides utilities for file and directory management.
- **Key Functions**:
  - `save_in_same_directory(original_file_path, file_name)`: Saves a file in the same directory as the original.
  - `choose_file()`: Simplified interface for selecting files.

---

### **4. QuestionMaster.py**
- **Purpose**: Handles user input with structured prompts and validation.
- **Key Features**:
  - Supports various input types like `yes_no`, `int`, and `num`.

---

### **5. BM4DProcessor.py**
- **Purpose**: Implements BM4D denoising for 3D volumetric images.
- **Key Features**:
  - **Denoising**: `do_bm4d()` with customizable parameters.
  - **Segmentation**: `label_components()` for filtering connected components.
  - **Napari Integration**: Displays images with labeled components.

---

### **6. image_processor.py**
- **Purpose**: Processes `.tif` and `.lif` files, generating integrated images and 3D stacks.
- **Key Functions**:
  - `process_lif_file(file_path)`: Integrates `.lif` file processing and metadata extraction.
  - `process_tiff_file(file_path)`: Performs maximum intensity projection for `.tif` files.

---

### **7. manual_correction_data_loader.py**
- **Purpose**: Loads and validates datasets required for manual corrections.
- **Key Functions**:
  - `load_or_check_datasets(directory_path)`: Verifies the presence of required datasets (`image_dataset.tiff`, `sharpened_img_dataset.tiff`, `mask_dataset.tiff`).
  - `choose_directory_and_load_datasets()`: Opens a dialog for directory selection and loads datasets.

---

### **8. napari_editor.py**
- **Purpose**: Interactive editor for manual corrections using Napari.
- **Key Features**:
  - Allows segmentation, toggling views, label selection, and dataset saving.
  - Interactive user controls via key bindings.

#### **Key Bindings and Functionalities**
| **Key** | **Functionality**                                                                                             |
|---------|---------------------------------------------------------------------------------------------------------------|
| `c`     | **Confirm and Segment**: Segments the image using the currently selected label ID (`focus_id`) and overlays the segmented result. |
| `s`     | **Save and Exit**: Saves the current mask and datasets, then exits the viewer for the current image. If this is the last image, it finalizes the saving process. |
| `n`     | **Skip and Next**: Skips saving the current image and moves to the next image in the dataset. If it’s the last image, it will stop the process. |
| `r`     | **Return to Previous**: Returns to the previous image for review or corrections. Reopens the previous image in the viewer. |
| `v`     | **Toggle View**: Switches the view orientation between the original view (`x-y plane`) and alternate planes (`y-z`, `x-z`). Useful for reviewing 3D images from different perspectives. |

---

### **9. image_cropper.py**
- **Purpose**: Automates the cropping and masking of integrated images.
- **Key Functions**:
  - `process_cropped(integrated_image)`: Interactively crops and processes a region.
  - `mask_3D_image(image_3D, cropped_image)`: Masks a 3D image using the cropped 2D region.

---

## **Contact**

For further questions or assistance, please contact:  
**Ding Yang Wang**  
[deweywang2000@gmail.com](mailto:deweywang2000@gmail.com)
