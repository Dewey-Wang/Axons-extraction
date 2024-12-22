# **Data Folder**

This folder contains example microscopy data for testing and demonstrating the pipeline. The data is categorized into two types based on axon density:

1. **`intensive/`**: Contains data with high axon density.
2. **`less_intensive/`**: Contains data with low axon density.

Each dataset includes raw files and preprocessed versions generated at different stages of the pipeline.

---

## **Files and Descriptions**

### **1. Intensive Data (`intensive/`)**
- **`raw.lif`**:  
  Raw microscopy data with high axon density.
- **`bm3d.tiff`**:  
  Data preprocessed using BM3D denoising for initial noise reduction.
- **`bilateral.tiff`**:  
  Further processed using bilateral filtering to preserve fine structures.
- **`top_hat.tiff`**:  
  Final step: Top-Hat filtering to remove uneven background illumination.

### **2. Less Intensive Data (`less_intensive/`)**
- **`raw.lif`**:  
  Raw microscopy data with low axon density.
- **`bm3d.tiff`**:  
  Data preprocessed using BM3D denoising for initial noise reduction.
- **`bm4d.tiff`**:  
  Further processed using BM4D denoising for volumetric noise reduction.
- **`top_hat.tiff`**:  
  Final step: Top-Hat filtering to remove uneven background illumination.

---

## **Usage Notes**

1. **File Naming**:
   - File names are simplified to reflect the processing stages:
     - `raw`: Raw data.
     - `bm3d`: BM3D denoised data.
     - `bilateral`: BM3D + bilateral filtered data.
     - `bm4d`: BM3D + BM4D filtered data (less intensive only).
     - `top_hat`: Final preprocessed data after Top-Hat filtering.
   - Each folder (`intensive` and `less_intensive`) represents a specific dataset type.

2. **Preprocessing Workflow**:
   - Files in each folder follow a sequential processing pipeline:
     - **`intensive/`:**
       - `raw` → `bm3d` → `bilateral` → `top_hat`.
     - **`less_intensive/`:**
       - `raw` → `bm3d` → `bm4d` → `top_hat`.

3. **Data Formats**:
   - `.lif`: Raw microscopy image format.
   - `.tiff`: Preprocessed image files, ready for further steps in the pipeline.

4. **Compatibility**:
   - The current pipeline scripts support `.lif` and `.tiff` formats.
   - For other file formats, modify the preprocessing step in **`current step.ipynb`**, specifically the first block of code.

---

## **Acknowledgment**

The data in this folder is shared with permission from **Prof. Dr. Kerschensteiner’s Laboratory** and is intended for educational and testing purposes only. For further use or questions, please contact the laboratory or the repository owner.

---

## **Contact**

For additional information or assistance, refer to the main [README.md](../README.md) or contact:  
**Ding Yang Wang**  
[deweywang2000@gmail.com](mailto:deweywang2000@gmail.com)
