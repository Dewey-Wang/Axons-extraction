# **Automated Identification of Mouse Spinal Cord Axons Using Deep Learning**

Welcome to the repository for my Master’s thesis: **Establishment of Neural Network Pipeline for Automated Identification of Mouse Spinal Cord Axons**. This project introduces a **deep learning pipeline** that automates the segmentation and analysis of axons in microscopy images, focusing on axonal calcium dynamics in multiple sclerosis (MS) research.

---

## **Abstract**

Multiple sclerosis (MS) causes axonal loss, a key driver of patient disability. Our findings indicate a correlation between axonal degeneration and calcium levels, with elevated calcium observed in degenerating axons. This suggests that the intra-axonal calcium concentration may serve as an important checkpoint towards axonal degeneration. Our project tackles the inefficiencies in manual analysis of axonal calcium levels by implementing a robust **3D-UNet neural network** for volumetric segmentation and a semi-automatic image-processing pipeline to prepare axon segmentation data.

### Key Contributions:
- A **semi-automatic pipeline** employing state-of-the-art denoising and segmentation techniques for efficient data preprocessing and ground truth generation (Steps 1–3 in **Workflow**).
- **High-throughput segmentation** of fluorescently labeled axons using **deep learning** to automate segmentation after training (Steps 1–2 in **Workflow** + trained model).

---

## **Workflow**
1. **Data Acquisition**:
   - Microscopy images of axons from EAE-induced mice expressing FRET calcium sensors.
2. **Preprocessing**:
   - Image denoising using BM3D, BM4D, and bilateral filtering.
3. **Segmentation - ground truth generation**:
   - Semi-automatic segmentation using thresholding and CCL.
   - Using napari to manual correct the segmentaion from thresholding and CC.-This step is to make ground truth image.
4. **Training Data preparation**:
   - create the algorithums to transfer the segmentation labeled image into semantic image. 
5. **Data Augmentation**:
   -  Utilized libraries such as \colorbox{lightgray}{\texttt{kimimaro}} and \colorbox{lightgray}{\texttt{torchio}} to expand dataset diversity.
6. **Model Trainning**:
   - Trainning 3D-Unet model and VGG16-backboned 3D-Unet model. 
7. **Model Estimation**:
   - Compared model predictions with ground truth annotations.
   - Achieved classification accuracy: **Background (0.99)**, **Axons (0.85)**, and **Borders (0.65)**.

---

## **Techniques and Tools**

### **1. Data Acquisition**
- **Microscopy Imaging**: Captured confocal microscopy images of axons using **SP8 Confocal Microscopy (Leica)**.

### **2. Image Preprocessing**
- **Denoising Algorithms**:
  1. **Initial Denoising**:
     - **BM3D**: Applied advanced block-matching and collaborative filtering to reduce noise in 2D/3D images.
  2. **Algorithm Choice Based on Image Characteristics**:
     - For **axon-intensive images**:
       - Used **Bilateral Filtering** to reduce Gaussian noise while preserving edge features, as **BM4D** tends to misinterpret dense axonal signals as noise and removes them entirely.
     - For **less axon-intensive images**:
       - Applied **BM4D** for volumetric data denoising.
  3. **Background Removal**:
     - Applied **Top-Hat Filtering** to extract foreground features and remove uneven background illumination.

- **Initial Segmentation**:
  - Used `cle.greater_or_equal_constant` for custom thresholding to create binary images.
  - Extracted edge features with Sobel filters.
  - Generated labeled regions with `skimage.measure.label`.

     
### **3. Ground Truth Generation**
- **Interactive Ground Truth Creation**:
  - Developed a **custom Python tool** using `napari` and standard Python libraries like `os`, `tifffile`, and `tkinter` to streamline the creation of ground truth labeled images.
  - The tool provides a user-friendly interface for loading, viewing, annotating, and saving labeled images.
- **Key Features**:
  1. **Shortcut-Driven Workflow**:
     - `c`: Confirm and segment a specific region by applying a label mask.
     - `s`: Save the current mask and move to the next image.
     - `n`: Skip the current image without saving.
     - `r`: Return to the previous image for corrections.
     - `v`: Toggle between different viewing perspectives (e.g., y-z plane).
  2. **Normalization**:
     - Automatic normalization of image datasets to enhance contrast and ensure consistent brightness across slices.
  3. **Dynamic Label Masking**:
     - Enables segmentation of specific regions based on a selected label ID and visualizes sharpened or segmented results in real-time.
  4. **File Management**:
     - Integrated functions for loading existing datasets and saving progress, allowing users to resume their work seamlessly.
  5. **Interactive Navigation**:
     - Allows users to navigate large datasets and annotate images efficiently.

- This tool significantly enhances the efficiency and accuracy of ground truth generation, making it easier to create high-quality labeled images for training deep learning models.


### **4. Training Data Preparation**
- Developed algorithms to convert segmentation-labeled images into semantic labels suitable for deep learning.

### **5. Data Augmentation**
- **Kimimaro**: Enhanced data diversity by skeletonizing neuronal structures.
- **TorchIO**: Applied spatial, intensity, and random augmentations for 3D medical imaging datasets.

### **6. Model Training**
- **3D-UNet**: Trained a 3D convolutional neural network for volumetric segmentation.
- **VGG16-backboned 3D-UNet**: Incorporated VGG16 as a backbone for improved feature extraction and segmentation accuracy.

### **7. Model Estimation**
- Compared model predictions with ground truth annotations using evaluation metrics such as:
  - **Precision**, **Recall**, and **F1 Score**.
  - Achieved segmentation accuracy:
    - **Background**: 0.99
    - **Axons**: 0.85
    - **Borders**: 0.65

---

## Installation
### Prerequisites
- Python 3.8+ (recommended Anaconda environment)
- GPU for training (NVIDIA RTX 3060 Ti or similar)

### Technical Requirements
#### Equipment
| **Equipment**           | **Description**            | **Manufacturer** |
|--------------------------|----------------------------|------------------|
| NVIDIA RTX 3060 Ti       | 8GB-GPU                   | ASUS            |
| AMD Ryzen 9 5950X        | 128GB-16 core-CPU         | AMD             |
| SP8                      | Confocal microscopy       | Leica           |

#### Software & Packages
##### Global Setting
| **Software**            | **Version**     | **Purpose**                                    |
|--------------------------|-----------------|-----------------------------------------------|
| Windows                 | 10 Enterprise   | Computer system                               |
| Anaconda                | 2.6.0           | Manage different environments for programming |
| Microsoft Build Tools   | 2022-x86        | Associate with Microsoft Visual C++ download  |
| Microsoft Visual C++    | 2022-x86        | Run some python packages that are written in C/C++ |
| ImageJ                  | 1.54d           | Make the profile plot                         |
| CUDA                    | V11.8           | Run GPU in training                           |
| Cudnn                   | V9.0            | Associate with CUDA                           |

---

### Anaconda Environment
#### Pre-processing and Machine Learning Settings
| **Pre-processing Setting** | **Version** | **Machine Learning Setting**   | **Version** |
|-----------------------------|-------------|--------------------------------|-------------|
| python                      | 3.11.8      | python                         | 3.9.19      |
| jupyterlab                  | 4.0.11      | jupyterlab                     | 4.0.11      |
| readlif                     | 0.6.5       | tensorflow                     | 2.10.0      |
| numpy                       | 1.24.4      | numpy                          | 1.26.4      |
| matplotlib                  | 3.8.0       | segmentation_models_3D        | 1.0.0       |
| tqdm                        | 4.66.2      | skimage                        | 0.22.0      |
| cv2                         | 4.9.0       | patchify                       | 0.2.2       |
| IPython                     | 8.12.0      | keras                          | 2.10.0      |
| bm4d                        | 4.2.3       | matplotlib                     | 3.8.4       |
| bm3d                        | 4.0.1       | sklearn                        | 1.4.2       |
| napari                      | 0.4.18      | scipy                          | 1.13.0      |
| skimage                     | 0.22.0      | tifffile                       | 2024.2.12   |
| connected-components-3d     | 3.12.4      | napari                         | 0.4.19.post1|
| scipy.ndimage               | 1.11.4      | tqdm                           | 4.66.2      |
| pyclesperanto_prototype     | 0.24.2      |                                |             |
| napari_simpleitik_image_processing | 0.4.5      |                                |             |
| stackview                   | 0.7.4       |                                |             |
| tifffile                    | 2023.2.28   |                                |             |

---

## Usage
Follow the instructions provided in `instruction.ipynb` to set up, preprocess the data, and run the neural network pipeline. The guide includes:
- Environment setup
- Data preparation
- Model training
- Evaluation and result generation

---

## Results
The pipeline achieves state-of-the-art performance in axonal identification with metrics as detailed in the thesis. All results are reproducible using the provided scripts.

---

## Citation
If you use this repository, please cite:
> Ding Yang Wang, "Establishment of Neural Network Pipeline for Automated Identification of Mouse Spinal Cord Axons," Master’s Thesis, Ludwig-Maximilians-Universität München, 2024.

---

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

## Contact
For any questions or issues, please contact:  
**Ding Yang Wang**  
Email: [deweywang2000@gmail.com](deweywang2000@gmail.com)

---
## Supervisor
**Prof. Dr. med. Martin Kerschensteiner**  
Email: [Martin.Kerschensteiner@med.uni-muenchen.de](mailto:Martin.Kerschensteiner@med.uni-muenchen.de)
