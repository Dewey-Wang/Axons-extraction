# **Script Directory**

This directory contains all the Jupyter Notebooks and Python scripts required for the pipeline. It is organized into subdirectories corresponding to different stages of the workflow, with a `utils/` folder for reusable functions and utilities.

---

## **Subdirectory Descriptions**

### **1. Preprocessing**
- Jupyter Notebooks for raw data preprocessing, including denoising and filtering.

### **2. Manual Labeled Image Correction**
- Notebooks for manually correcting labeled images, leveraging tools like Napari.

### **3. Training Data Preparation**
- Notebooks to prepare data for model training, such as generating semantic labels from ground truth.

### **4. Data Augmentation**
- Notebooks for applying data augmentation techniques to enhance dataset diversity.

### **5. Model Training & Estimation**
- Notebooks for training models (e.g., 3D-Unet, VGG16-backboned 3D-Unet) and evaluating their performance.

### **Utils**
A collection of Python scripts providing shared functionality for the pipeline:

| **File Name**             | **Description**                                                    |
|----------------------------|--------------------------------------------------------------------|
| `LifFileProcessor.py`      | Functions for processing `.lif` microscopy files, including image integration and masking. |
| `capture_partial_image.py` | Tool for interactively selecting and cropping regions of interest from images. |
| `file_utilities.py`        | General file-handling utilities, such as file selection dialogs and directory management. |
| `QuestionMaster.py`        | Utility for interacting with users, including question prompts and input validation. |
| `BM4DProcessor.py`         | Specific implementation for BM4D denoising in the pipeline.      |

---

## **How to Use**

### Importing Utilities
To use a utility script from the `utils/` folder in your Jupyter Notebook:
```python
from utils.data_loader import load_data
from utils.image_processing import denoise_image
```

### Running Notebooks
Each subdirectory contains Jupyter Notebooks tailored for specific pipeline stages. Refer to the documentation in each notebook for detailed instructions.

---

## **Contact**

For further questions or assistance, please contact:  
**Ding Yang Wang**  
[deweywang2000@gmail.com](mailto:deweywang2000@gmail.com)
