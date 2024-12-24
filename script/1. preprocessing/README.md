# **Preprocessing Notebook**

This notebook demonstrates the preprocessing steps applied to microscopy image data, preparing it for downstream analysis. The steps include image integration, cropping, denoising, background removal, and dataset preparation using various tools and techniques.

---

## **Steps in Preprocessing**

### **1. Image Integration and Visualization**
- **Goal**: Combine slices of 3D image stacks into a single integrated image for easier visualization.
- **Tools**:
  - `process_image` from `image_processor.py` for loading and processing `.lif` and `.tif/.tiff` files.
  - Matplotlib for visualizing the integrated and 3D images.

### **2. Cropping Regions of Interest (ROI)**
- **Goal**: Allow interactive cropping of regions from the integrated image.
- **Tools**:
  - `process_cropped` from `image_cropper.py` to enable user-defined cropping using polygonal selections.
  - `mask_3D_image` to apply the cropped region as a mask to the 3D image stack.
- **Interactive Controls**:
  - `s`: Save the selected crop.
  - `r`: Restart the cropping process.

### **3. BM3D Denoising**
- **Goal**: Reduce noise in 3D image stacks while preserving important structures.
- **Process**:
  - Apply BM3D denoising to each 2D slice of the 3D stack.
  - Normalize the intensity values to ensure consistency.
- **Visualization**:
  - Display original and denoised images using Napari and `stackview`.

### **4. Optional BM4D Denoising**
- **Goal**: Perform volumetric denoising using BM4D for datasets with less axon density.
- **Process**:
  - Use `BM4DProcessor` for BM4D denoising.
  - Label and visualize components in Napari.

### **5. Bilateral Filtering (Optional)**
- **Goal**: Provide an alternative denoising method for datasets with high axon density.
- **Process**:
  - Apply bilateral filtering with customizable intensity parameters.
  - Use `napari_simpleitk_image_processing` for filtering.

### **6. Background Removal**
- **Goal**: Remove uneven background illumination for clearer segmentation.
- **Tools**:
  - Apply top-hat filtering using `cle.top_hat_box`.
  - Background removal is adapted for either BM3D or BM4D denoised images.

### **7. Saving Processed Data**
- Save the processed images (`bg_remove.tiff`) in the same directory as the input files.

---

## **Interactive Features**
1. **User Prompts**:
   - Ask whether to crop the image or proceed with denoising.
   - Guide the user through parameter selection for BM4D or bilateral filtering.
2. **Napari Integration**:
   - Provides an interactive viewer for inspecting original, denoised, and processed images.
   - Visualizes label components and different views (e.g., x-y, y-z).

---

## **Outputs**
- **Intermediate Results**:
  - Cropped 2D images.
  - BM3D and BM4D denoised images.
  - Background-removed images.
- **Final Output**:
  - Saved as `bg_remove.tiff` in the same directory as the input files.

---

## **Dependencies**
Ensure the following libraries are installed before running the notebook:
- `numpy`
- `bm3d`
- `cc3d`
- `napari`
- `pyclesperanto_prototype`
- `matplotlib`
- `tifffile`
- `napari_simpleitk_image_processing`

---

## **How to Use**
1. Place the notebook in the preprocessing directory.
2. Ensure the required utility scripts (`image_processor.py`, `image_cropper.py`, etc.) are available in the `utils` directory.
3. Run the notebook, following the interactive prompts for cropping, denoising, and processing.

---

## **For Python Script Details**
If you have any questions about the Python scripts used in this notebook (e.g., `image_processor.py`, `image_cropper.py`), please refer to the [README](../utils/README.md) in the `utils` directory for detailed descriptions and usage.

---

For questions or support, contact:  
**Ding Yang Wang**  
[deweywang2000@gmail.com](mailto:deweywang2000@gmail.com)
