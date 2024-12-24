# **Model Training README**

This directory contains two separate notebooks for training deep learning models for 3D image segmentation: 
1. **3D-UNet**
2. **SM-UNet** (Vgg16-backbone 3D-Unet).

Both models are designed for semantic segmentation of microscopy images with three classes: background, axons, and borders. Below, we describe the key setups, configurations, and reasons behind these choices.

---

## **1. 3D-UNet Training**

### **Overview**
The 3D-UNet architecture is customized for 3D volumetric data, using encoder-decoder blocks with skip connections to preserve spatial information during downsampling and upsampling.

### **Key Configurations**
1. **Batch Normalization**:
   - Added to every convolutional block to stabilize training and improve convergence.
   - Not present in the original 3D-UNet but essential here due to the complexity of 3D data.

2. **Dropout Rates**:
   - Applied varying rates (0.1 to 0.5) across layers to prevent overfitting.

3. **Loss Function**:
   - Combination of `Dice Loss` (handles imbalanced data) and `Categorical Focal Loss` (focuses on difficult-to-classify regions).

4. **Learning Rate**:
   - Initial learning rate: **0.0001**, optimized for gradual convergence.

5. **Training Details**:
   - Input shape: `(32, 64, 64, 3)` (patch size with 3 channels).
   - Number of epochs: **150**.
   - Batch size: **2** (due to memory limitations with 3D data).

6. **Callbacks**:
   - **ModelCheckpoint**: Saves the best model based on validation loss.
   - **ReduceLROnPlateau**: Reduces learning rate when validation loss plateaus.

### **Why These Settings?**
- **Batch Normalization** helps reduce internal covariate shifts, making training more stable and faster.
- **Dropout** is essential to regularize the model and avoid overfitting on volumetric data.
- **Low Batch Size** accommodates the large memory footprint of 3D convolution operations.

---

## **2. SM-UNet Training**

### **Overview**
The SM-UNet uses the `Segmentation Models 3D` library, leveraging pre-trained backbones for efficient feature extraction.

### **Key Configurations**
1. **Backbone**:
   - Used `VGG16` with `ImageNet` pre-trained weights as the encoder.
   - Limitation: **VGG16 lacks Batch Normalization**, making the training less stable.

2. **Loss Function**:
   - Similar to 3D-UNet: `Dice Loss + Categorical Focal Loss`.

3. **Learning Rate**:
   - Initial learning rate: **0.0001**.

4. **Training Details**:
   - Input shape: `(32, 64, 64, 3)` (patch size with 3 channels).
   - Number of epochs: **500**.
   - Batch size: **2**.

5. **Callbacks**:
   - **ModelCheckpoint**: Saves the best model based on validation loss.
   - **ReduceLROnPlateau**: Reduces learning rate when validation loss plateaus.

6. **Preprocessing**:
   - Input data normalized using the `preprocess_input` function from the `Segmentation Models` library.

### **Why These Settings?**
- **Pre-trained VGG16** provides a strong initialization, accelerating convergence.
- The absence of Batch Normalization in VGG16 makes training less stable but manageable with proper learning rate scheduling.
- **High Epochs (500)** are required to counter the instability and ensure convergence.

---

## **Common Details**

### **Dataset**
- Input images and masks:
  - Images: Normalized to three channels.
  - Masks: Converted to one-hot encoding with three classes (background, axons, borders).
- Data split:
  - **90% training**, **10% testing**.

### **Hardware Requirements**
- GPU is required for efficient training of both models.
- Ensure CUDA and CuDNN are correctly installed.
- See  [README](../../env/README.md)

### **Saved Outputs**
- **Best Model**: Saved as `best_model.h5`.
- **Training History**: Logged in `history_au.csv`.
- **Processed Datasets**: Stored as `.npy` files:
  - `X_train.npy`, `X_test.npy`
  - `y_train.npy`, `y_test.npy`

---

## **How to Use**
1. Ensure required datasets are preprocessed and available as `.npy` files.
2. Load and execute the desired notebook (`3D-UNet` or `SM-UNet`).
3. Monitor training stability and adjust hyperparameters as needed (e.g., learning rate, dropout rates).
4. Evaluate the model using validation metrics and saved checkpoints.

---

## **Dependencies**
- Python 3.8+
- TensorFlow 2.x
- Segmentation Models 3D (`segmentation_models_3D`)
- NumPy, Matplotlib, Scikit-learn

---

For questions or support, contact:  
**Ding Yang Wang**  
[deweywang2000@gmail.com](mailto:deweywang2000@gmail.com)
