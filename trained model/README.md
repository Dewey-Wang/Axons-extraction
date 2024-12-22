# **Trained Models**

| **File Name**         | **Description**                               |
|------------------------|-----------------------------------------------|
| `3d_unet_model.h5`    | Pre-trained weights for the custom 3D-Unet.   |
| `vgg16_unet_model.h5` | Pre-trained weights for the VGG16-based 3D-Unet.|

---

## **Model Overview**

### **1. 3D-Unet**
- **Description**:
  - Custom-built 3D-Unet designed to segment axons in 3D volumetric microscopy images.
  - Features symmetric encoder-decoder architecture with skip connections and dropout layers for better regularization.


### **2. VGG16-backboned 3D-Unet**
- **Description**:
  - A 3D-Unet with a pre-trained VGG16 encoder backbone.
  - Built using the `segmentation_models_3D` library.

---

## **Input Data Requirements**

The models expect input data with the following specifications:

- **Shape**: `(32, 64, 64, channels)`  
  - `32`: Depth (number of slices in the Z-axis).  
  - `64`: Height (size along the Y-axis).  
  - `64`: Width (size along the X-axis).  
  - `channels`: Number of image channels (e.g., 1 for grayscale or 3 for RGB).  
- **Data Type**: 3D volumetric data.  
- **Normalization**: Ensure pixel values are normalized between `0` and `1`.  

---

## **Usage**

### **Load Models**
The pre-trained models can be loaded as follows:
```python
from tensorflow.keras.models import load_model

# Load 3D-Unet model
unet_model = load_model('3d_unet_model.h5')

# Load VGG16-backboned 3D-Unet model
vgg16_model = load_model('vgg16_unet_model.h5', compile=False)
```

### **Run Inference**
To use the models for prediction:
```python
# Input data: shape (batch_size, depth, height, width, channels)
predictions = unet_model.predict(input_data)

# For VGG16-backboned model
vgg16_predictions = vgg16_model.predict(input_data)
```

---

## **Additional Details**

### **Training Information**
- Training details, including optimizer, loss functions, metrics, and callbacks, are available in the [5. model training & estimation](../script/5.%20model%20trainning%20&%20estimation) folder.

### **Performance**
- A detailed performance evaluation is also provided in the [5. model training & estimation](../script/5.%20model%20trainning%20&%20estimation) folder.

---

## **Contact**

For further questions or assistance, please contact:  
**Ding Yang Wang**  
[deweywang2000@gmail.com](mailto:deweywang2000@gmail.com)
