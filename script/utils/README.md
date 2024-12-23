# **Utils Directory**

The `utils` directory contains a set of modular and reusable Python scripts designed to streamline key processes in the pipeline, such as file handling, image preprocessing, denoising, and user interaction.

---

## **Files and Descriptions**

### **1. LifFileProcessor.py**
- **Purpose**:
  - Provides functions for handling `.lif` microscopy files and extracting 3D image stacks.
- **Key Functions**:
  - `calculate_sum_of_series()`: Computes the total number of series from `.lif` metadata.
  - `select_images_by_series_number(serie_number)`: Selects image stacks based on the number of series.
  - `create_integrated_image(selected_list, z_list, x_list, y_list, channel_num)`: Combines 3D slices into a single integrated image.
  - `process_cropped(integrated_image)`: Processes and crops specific regions of interest from the integrated image.
  - `mask_3D_image(image_3D, cropped_image)`: Applies a cropped image mask to a 3D stack.

---

### **2. capture_partial_image.py**
- **Purpose**:
  - Interactive tool for selecting and cropping regions of interest (ROIs) from images.
- **Key Features**:
  - Allows users to draw polygons to define ROIs interactively.
  - Saves cropped regions as `cropped_region.jpg`.
- **Key Controls**:
  - **`r` (Reset)**:
    - Resets the image to its original state and clears any selected points. This is useful if you want to start the ROI selection process again from scratch.
  - **`s` (Save)**:
    - Saves the selected ROI as `cropped_region.jpg` after ensuring that at least two points are selected to define a polygonal region.


---

### **3. file_utilities.py**
- **Purpose**:
  - Provides utilities for file and directory management.
- **Key Functions**:
  - `save_in_same_directory(original_file_path, file_name)`: Saves a file in the same directory as the original.
  - `choose_file()`: Simplified interface for choosing files of any type/TIF files/Lif files.

---

### **4. QuestionMaster.py**
- **Purpose**:
  - Handles user input with structured prompts and input validation.
- **Key Features**:
  - Supports various input types such as `yes_no`, `int`, and `num`.
- **Example**:
  - `ask_question(input_type='yes_no')`: Prompts the user for a yes/no response with validation.

---

### **5. BM4DProcessor.py**
- **Purpose**:
  - Implements BM4D denoising for 3D volumetric images and provides segmentation functionalities.
- **Key Features**:
  - **Denoising with BM4D**:
    - `do_bm4d()`: Executes BM4D denoising with user-defined or default noise parameters.
  - **Parameter Customization**:
    - **PSD (`sigma`)**: The noise level, defaulting to the standard deviation of non-zero pixels.
    - **Threshold Value**: Segmentation threshold, defaulting to the 15th percentile of intensity values.
  - **Component Labeling**:
    - `label_components(denoised_image)`: Identifies and filters connected components based on user-defined size criteria.
  - **Integration with Napari**:
    - `run_viewer(denoised_image, viewer)`: Displays the denoised image and labeled components in a Napari viewer.

---

## **Contact**

For further questions or assistance, please contact:  
**Ding Yang Wang**  
[deweywang2000@gmail.com](mailto:deweywang2000@gmail.com)
