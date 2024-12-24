# **Model Evaluation**

This directory contains the notebook for evaluating the performance of trained deep learning models. The evaluation involves visualizing training history, computing performance metrics, generating confusion matrices, and reporting classification results.

---

## **Steps in Model Evaluation**

### **1. Visualizing Training History**
- **Purpose**: To analyze the model's learning behavior over epochs.
- **Plots**:
  1. **Loss Plot**:
     - Displays training and validation loss across epochs.
     - Helps identify overfitting or underfitting.
  2. **IOU (Intersection Over Union) Plot**:
     - Compares training and validation IOU scores.
     - Shows how well the model segments.

- **Output**:
  - `loss_plot.png`: Saved plot for loss.
  - `iou_plot.png`: Saved plot for IOU.

---

### **2. Loading Test Data**
- **Purpose**: Load the test dataset for evaluation.
- **Process**:
  - Images: `X_test.npy`.
  - Masks: `y_test.npy`.
  - Preprocessing: Optional (e.g., if a specific backbone like `VGG16` is used, apply its preprocessing).

---

### **3. Loading the Pretrained Model**
- **Purpose**: Load the best-performing model saved during training for evaluation.
- **Custom Objects**:
  - **Loss Function**: `Dice Loss + Categorical Focal Loss` to handle class imbalance and focus on misclassified pixels.
  - **Metrics**: IOU Score to measure segmentation performance.

---

### **4. Generating Predictions**
- **Purpose**: Use the loaded model to predict segmentation masks for the test set.
- **Process**:
  - Convert predictions from probabilities to class indices using `argmax`.

---

### **5. Evaluation Metrics**

#### **Confusion Matrix**
- **Purpose**: Visualize the relationship between true labels and predictions.
- **Process**:
  - Compute a normalized confusion matrix for classes: `background`, `axons`, `border`.
  - Save the matrix as `confusion_matrix.png`.

#### **Classification Report**
- **Purpose**: Provide precision, recall, and F1-score for each class.
- **Output**:
  - Includes a detailed textual report summarizing performance for all classes.

---

## **Key Configurations**

1. **Learning Rate**:
   - Set to `0.0001` for evaluation consistency with training.

2. **Custom Loss and Metrics**:
   - **Dice Loss**: Handles class imbalance.
   - **Focal Loss**: Focuses on hard-to-classify pixels.
   - **IOU Score**: Measures segmentation accuracy.

3. **Classes**:
   - Background, axons, and border.

---

## **Outputs**

- **Visualizations**:
  - `loss_plot.png`: Loss trends during training.
  - `iou_plot.png`: IOU trends during training.
  - `confusion_matrix.png`: Normalized confusion matrix.

- **Metrics**:
  - Precision, recall, F1-score (from the classification report).
  - Mean IoU for segmentation performance.

---

## **How to Use**
1. **Pretrained Model**:
   - Place the best-performing model file (`best_model.h5`) in the `6. model trainning` directory.
2. **Test Dataset**:
   - Ensure `X_test.npy` and `y_test.npy` are available.
3. **Run the Notebook**:
   - Follow the notebook to generate predictions and evaluate metrics.

---

## **Dependencies**
- Python 3.8+
- TensorFlow 2.x
- Segmentation Models 3D (`segmentation_models_3D`)
- NumPy, Pandas, Matplotlib, Scikit-learn, Keras

---

## **Notes**
- Ensure GPU availability for efficient evaluation.
- Preprocess input if the model uses a specific backbone like `VGG16`.

---

For questions or support, contact:  
**Ding Yang Wang**  
[deweywang2000@gmail.com](mailto:deweywang2000@gmail.com)
