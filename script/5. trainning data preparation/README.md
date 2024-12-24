# **Training Data Preparation Notebook**

This notebook outlines the steps for preparing training data from raw microscopy images and corresponding masks. The preparation includes validation, resizing, patching, augmentation, and saving the data in a format suitable for deep learning models.

---

## **Steps in Training Data Preparation**

### **1. Load Images and Masks**
- **Purpose**: Load raw microscopy images and their corresponding masks.
- **Tools**:
  - `file_utilities.choose_file()` for selecting files interactively.
  - `skimage.io.imread` for loading `.tiff` images.

---

### **2. Validate Shapes**
- **Purpose**: Ensure that the shapes of all images and masks are consistent for model training.
- **Process**:
  - Use `check_shapes` to validate that all images and masks have the same dimensions.
  - Raise errors for mismatched shapes.

---

### **3. Adjust Image Sizes**
- **Purpose**: Resize images and masks to ensure their dimensions are multiples of 32 (a common requirement for deep learning models).
- **Process**:
  - Crop or pad images in the Z-dimension to meet the target size using `adjust_image_size`.

---

### **4. Patching Images**
- **Purpose**: Divide large 3D images and masks into smaller patches for training.
- **Tools**:
  - `patchify` to split images and masks into patches.
  - Reshape patches into 4D datasets (e.g., `n_patches, depth, height, width`).

---

### **5. Augmentation Data Loading**
- **Purpose**: Load and validate augmented image datasets from a specified directory.
- **Process**:
  - Use `read_augmentation_images` to read images and masks from augmentation folders.
  - Validate shape consistency between images and masks.

---

### **6. Merge Augmented Data**
- **Purpose**: Combine original and augmented data to create a comprehensive dataset.
- **Process**:
  - Concatenate image and mask datasets using `numpy.concatenate`.

---

### **7. Sanity Check**
- **Purpose**: Randomly visualize image-mask pairs to ensure data integrity.
- **Tools**:
  - Use `matplotlib.pyplot` to display random patches from the dataset.

---

### **8. Prepare Data for Training**
- **Purpose**: Convert datasets into a format suitable for deep learning.
- **Process**:
  - Add a channel dimension to images.
  - Convert masks into categorical data using `to_categorical` for multi-class segmentation.

---

### **9. Save Prepared Data**
- **Purpose**: Save training and testing datasets for future use.
- **Process**:
  - Split the data into training and testing sets using `train_test_split`.
  - Save datasets as `.npy` files:
    - `X_train.npy`, `X_test.npy`: Images for training and testing.
    - `y_train.npy`, `y_test.npy`: Masks for training and testing.

---

## **Interactive Features**
1. **Dynamic Validation**:
   - Ensure all images and masks are correctly paired and have consistent dimensions.
2. **Flexible Patching**:
   - Allow user-defined patch sizes, ensuring compatibility with deep learning requirements.
3. **Augmentation Integration**:
   - Automatically integrate augmented datasets into the preparation pipeline.

---

## **Key Outputs**
- **Processed Datasets**:
  - `train_img.npy`: Processed training images.
  - `train_mask.npy`: Processed training masks.
  - `X_train.npy`, `X_test.npy`: Training and testing image datasets.
  - `y_train.npy`, `y_test.npy`: Training and testing mask datasets.

---

## **Dependencies**
Ensure the following libraries are installed before running the notebook:
- `numpy`
- `skimage`
- `tifffile`
- `patchify`
- `keras`
- `scikit-learn`

---

## **How to Use**
1. Place the notebook in the `trainning data preparation` directory.
2. Ensure required utility scripts (`file_utilities.py`, etc.) are available in the `utils` directory.
3. Follow interactive prompts to load, validate, patch, and save datasets.

---

## **For Python Script Details**
If you have any questions about the Python scripts used in this notebook (e.g., `file_utilities.py`), refer to the [README](../utils/README.md) in the `utils` directory for detailed descriptions and usage.

---

For questions or support, contact:  
**Ding Yang Wang**  
[deweywang2000@gmail.com](mailto:deweywang2000@gmail.com)
