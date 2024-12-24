# **Run the Model README**

This directory contains two notebooks designed to perform model inference and analyze the prediction results for 3D segmentation tasks:

1. **Run the Model (`Run the model.ipynb`)**: 
   - Breaks large 3D volumes into manageable patches.
   - Loads a pretrained model and performs predictions on the patches.
   - Reconstructs the segmented volume and saves it for further analysis.

2. **Read Prediction Results (`Read prediction result.ipynb`)**:
   - Reads the segmented volume, processes the results, and filters small or insignificant labels.
   - Displays the filtered results interactively using Napari.

---

## **1. Run the Model**

### **Steps**
1. **Load the Input Volume**:
   - Supports large 3D images (e.g., `1024x1024x32`).
   - Resizes input volumes to match the patch dimensions used during model training.

2. **Patchify the Volume**:
   - Splits the input volume into smaller 3D patches of shape `(32, 64, 64)` for efficient processing.

3. **Load the Pretrained Model**:
   - Allows selection of the desired model (`.h5` file) using `file_utilities.choose_file`.
   - Loss function: `Dice Loss + Categorical Focal Loss` to handle class imbalance.
   - Metric: Intersection Over Union (IOU) for segmentation performance.

4. **Perform Predictions**:
   - Predicts segmentation masks for each patch.
   - Converts class probabilities into discrete class labels using `argmax`.

5. **Reconstruct the Volume**:
   - Reassembles patches into the original volume shape.
   - Converts the segmented volume into `uint8` for compatibility with visualization tools.

6. **Save the Segmented Volume**:
   - Outputs the segmented volume as `prediction_result_1.tif`.

---

### **Configurations**
- **Patch Size**: `(32, 64, 64)`, chosen to balance memory constraints and prediction accuracy.
- **Overlap**: No overlap is used during patching.
- **Loss Function**: Combines `Dice Loss` and `Categorical Focal Loss` for robust handling of class imbalances.

---

## **2. Read Prediction Results**

### **Steps**
1. **Load the Predicted Volume**:
   - Uses `file_utilities.choose_file` to select the segmented volume (`.tif`).

2. **Filter Labels**:
   - Removes small, insignificant labels (e.g., components smaller than 1000 pixels).
   - Uses `scipy.ndimage.label` for connected component analysis.

3. **Visualize with Napari**:
   - Adds the filtered segmentation labels to Napari's interactive viewer.
   - Allows users to inspect the results in 3D.

---

## **Outputs**

### **Run the Model**
- **Segmented Volume**: 
  - `prediction_result_1.tif`: Contains the reconstructed segmented volume with class labels.

### **Read Prediction Results**
- **Filtered Labels**: 
  - Interactive visualization in Napari with labels displayed in 3D.

---

## **Dependencies**
Ensure the following libraries are installed:
- TensorFlow 2.x
- Keras
- NumPy
- Matplotlib
- Scipy
- Napari
- tifffile
- segmentation_models_3D
- patchify

---

## **How to Use**

### **Run the Model**
1. Place the input volume in a supported format (e.g., `.tif`).
2. Use the notebook to:
   - Select the input file and the pretrained model.
   - Perform inference and save the segmented volume.

### **Read Prediction Results**
1. Load the segmented volume using the notebook.
2. Filter and analyze the results interactively with Napari.

---

## **Notes**
- **Patch Size**:
  - Ensure the patch size matches the one used during training for consistent results.
- **Memory Constraints**:
  - Adjust the batch size during inference if GPU memory is limited.
- **Label Filtering**:
  - Labels smaller than 1000 pixels are removed to reduce noise in the segmentation results.

---

For questions or support, contact:  
**Ding Yang Wang**  
[deweywang2000@gmail.com](mailto:deweywang2000@gmail.com)
