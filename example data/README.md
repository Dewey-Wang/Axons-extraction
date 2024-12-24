# **Example Data Directory**

This folder contains example microscopy data for testing and demonstrating the pipeline. The data is categorized into two types based on axon density:

1. **`intensive/`**: High axon density datasets.
2. **`less_intensive/`**: Low axon density datasets.

Each dataset includes raw files, preprocessed versions, and semantic labels generated at different stages of the pipeline.

---

## **Folder Structure and Descriptions**

### **1. Augmentation**
- Contains augmented datasets to enhance model robustness:
  - **`intensive/`**:
    - **`image/`**: Augmented images (e.g., `RandomFlip_LR transpose 0 Image/`).
    - **`mask/`**: Corresponding masks for the augmented images.
  - **`less_intensive/`**:
    - **`image/`**: Augmented images (e.g., `RandomGamma_RandomFlip_transpose 0 Image.tif`).
    - **`mask/`**: Corresponding masks.

---

### **2. Intensive Data (`intensive/`)**
- **`raw_capture/raw_capture.tiff`**:  
  Raw microscopy data with high axon density.
- **`BM3D/part_*`**:  
  Data preprocessed using BM3D denoising for initial noise reduction (split into parts for size).
- **`bilateral/part_*`**:  
  Further processed using bilateral filtering to preserve fine structures (split into parts for size).
- **`top_hat/part_*`**:  
  Final step: Top-Hat filtering to remove uneven background illumination (split into parts for size).
- **`GT/GT.tif`**:  
  Ground truth segmentation labels for the dataset.
- **`GT - rm 9/GT-rm 9.tif`**:  
  Ground truth labels with the 9th label removed for experimental purposes.
- **`semantic image/label_with_border_mask.tif`**:  
  Semantic labels including borders for model training.

---

### **3. Less Intensive Data (`less_intensive/`)**
- **`raw_capture/raw_capture.tiff`**:  
  Raw microscopy data with low axon density.
- **`BM3D/BM3D.tif`**:  
  Data preprocessed using BM3D denoising for initial noise reduction.
- **`BM4D/BM4D.tif`**:  
  Further processed using BM4D denoising for volumetric noise reduction.
- **`top_hat/top_hat.tiff`**:  
  Final step: Top-Hat filtering to remove uneven background illumination.
- **`GT/GT.tif`**:  
  Ground truth segmentation labels for the dataset.
- **`semantic image/label_with_border_mask.tif`**:  
  Semantic labels including borders for model training.

---

## **File Reassembly Instructions**
Some files are split into parts (e.g., `part_*`) due to their large size. To reassemble, navigate to the directory containing the split files and use the following command in Git Bash:

```bash
cat part_* > filename.tif
```
Replace `filename.tif` with the desired output file name (e.g., `BM3D.tif`, `bilateral.tif`).


---

## **Usage Notes**

1. **File Naming**:
   - Files reflect their processing stages (e.g., **`BM3D`**, **`bilateral`**, **`top_hat`**)
   - Subfolders (`intensive` and `less_intensive`) indicate dataset types based on axon density.

2. **Preprocessing Workflow**:
   - **`intensive/`:**
     - `raw_capture` → `BM3D` → `bilateral` → `top_hat`.
   - **`less_intensive/`:**
     - `raw_capture` → `BM3D` → `BM4D` → `top_hat`.
     - 
3. **Compatibility**:
   - All files are compatible with pipeline scripts in the **`scripts/`** directory.
   - Ensure proper reassembly before using split files in the pipeline.

---

## **Acknowledgment**

The data in this folder is shared with permission from **Prof. Dr. Kerschensteiner’s Laboratory** and is intended for educational and testing purposes only. For further use or questions, please contact the laboratory or the repository owner.

---

## **Contact**

For additional information or assistance, refer to the main [README.md](../README.md) or contact:  
**Ding Yang Wang**  
[deweywang2000@gmail.com](mailto:deweywang2000@gmail.com)
