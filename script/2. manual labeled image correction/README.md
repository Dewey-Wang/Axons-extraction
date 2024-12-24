# **Manual Labeled Image Correction Notebook**

This notebook provides a comprehensive pipeline for manually correcting labeled microscopy images. It includes loading and processing 3D image data, applying segmentation and sharpening, and enabling interactive editing of image patches using Napari.

---

## **Steps in Manual Correction**

### **1. Load Preprocessed Images**
- **Purpose**: Load background-removed images (`bg_remove.tiff`) for further processing.
- **Tools**: 
  - `file_utilities.choose_file()` for selecting files interactively.
  - `tifffile.imread` for loading TIFF images.

### **2. Interactive Thresholding and Labeling**
- **Purpose**: Allow interactive tuning of threshold values for binary segmentation.
- **Tools**:
  - `stackview.interact` for real-time visualization of threshold effects.
  - Pyclesperanto's `greater_or_equal_constant` for binarization.
  - Scikit-image’s `label` for connected component labeling.

### **3. Filtering Small Components**
- **Purpose**: Retain only significant components based on size criteria.
- **Process**:
  - Use `ndi.label` to label connected components.
  - Filter out components smaller than a user-defined minimum size (default: 1000 pixels).

### **4. Image Patching (Optional)**
- **Purpose**: Split large images into smaller patches for easier manual correction.
- **Process**:
  - Use `patchify` to divide images and masks into patches of user-defined size.
  - Validate patch sizes to ensure compatibility with image dimensions.

### **5. 3D Image Sharpening**
- **Purpose**: Enhance image clarity for better manual corrections.
- **Tools**:
  - Apply Laplacian sharpening using `ndi.laplace`.

### **6. Interactive Editing with Napari**
- **Purpose**: Enable manual corrections and segmentation using Napari’s interactive viewer.
- **Tools**:
  - `napari_editor.ImageEditor` for editing and segmenting image patches.
  - Controls for navigating, segmenting, and saving corrected datasets.

### **7. Reload Existing Datasets**
- **Purpose**: Reload previously saved datasets for further corrections.
- **Tools**:
  - `manual_correction_data_loader.choose_directory_and_load_datasets` to select and load existing datasets.

---

## **Interactive Features**
1. **Threshold Adjustment**:
   - Fine-tune threshold values interactively for binarization.
   - Preview results using `stackview`.

2. **Patching Options**:
   - Choose patch sizes interactively.
   - Ensure patches fit the image dimensions for seamless processing.

3. **Napari Integration**:
   - Navigate through image slices and patches.
   - Segment and edit labels using intuitive key bindings.

---

## **Key Outputs**
- **Patches**:
  - Divided image and mask patches for manual corrections.
- **Sharpened Images**:
  - Laplacian-sharpened 3D images for enhanced visibility.
- **Final Corrected Masks**:
  - Saved masks (`mask_dataset.tiff`) reflecting manual corrections.

---

## **Dependencies**
Ensure the following libraries are installed before running the notebook:
- `numpy`
- `tifffile`
- `pyclesperanto_prototype`
- `napari`
- `stackview`
- `patchify`

---

## **How to Use**
1. **Run Preprocessing**:
   - Ensure background-removed images (`bg_remove.tiff`) are ready.
2. **Load and Process**:
   - Follow the prompts to load and binarize images, apply segmentation, and create patches.
3. **Edit in Napari**:
   - Use `NapariEditor` for manual corrections. See [README](../utils/README.md) for operation.
4. **Save Results**:
   - Save corrected datasets for downstream analysis.

---

## **For Python Script Details**
If you have any questions about the Python scripts used in this notebook (e.g., `napari_editor.py`, `manual_correction_data_loader.py`), refer to the [README](../utils/README.md) in the `utils` directory for detailed descriptions and usage instructions.

---

For questions or support, contact:  
**Ding Yang Wang**  
[deweywang2000@gmail.com](mailto:deweywang2000@gmail.com)
