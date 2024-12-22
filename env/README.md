# **Environment Setup**

This repository provides two environment files for setting up the necessary dependencies: `training_env.yml` for GPU-based model training and `preprocessing_env.yml` for preprocessing tasks. Please follow the instructions below to set up the environments using Anaconda.

---

## **Environment Files**
1. **`training_env.yml`**: Includes all packages and dependencies for training models, requiring a GPU (e.g., NVIDIA RTX 3060 Ti or equivalent).
2. **`preprocessing_env.yml`**: Includes dependencies for preprocessing data and generating ground truth images. This environment is sufficient if you are not training models.

---

## **Setup Instructions**

### **Step 1: Install Anaconda**
Ensure you have Anaconda installed on your system. Download it from [Anaconda Official Website](https://www.anaconda.com/).

### **Step 2: Clone the Repository**
Clone this repository to your local machine:
```bash
git clone https://github.com/your-repo-link.git
cd your-repo
```
### **Step 3: Create an Environment**
Use the appropriate environment file based on your requirements:

- For GPU Training
```bash
conda env create -f training_env.yml
conda activate training_env
```

- For Preprocessing and other usage
```bash
conda env create -f preprocessing_env.yml
conda activate preprocessing_env
```
### **Step 4: Verify Installation**
After activating the environment, verify the installation:

```bash
python --version
conda list
```

---

## **Troubleshooting**
If you encounter issues during the setup (e.g., missing dependencies or GPU compatibility errors), please check the following:

### **1. Ensure your system meets the Global Settings requirements**
- **Operating System**: Windows 10 Enterprise
- **GPU**: CUDA V11.8 and CuDNN V9.0 installed
- **Anaconda**: 2.6.0 or later installed

### **2. Ensure you have installed the necessary Microsoft Build Tools and Visual C++**
- Download and install the following:
  - [Microsoft Build Tools 2022](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
  - [Microsoft Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist)

### **3. For GPU issues**
- Verify that your CUDA and CuDNN versions are compatible with your GPU and TensorFlow version.

---

## **Alternative Setup (Manual Installation)**
If you cannot directly download the `training_env.yml` or `preprocessing_env.yml` files, you can manually install the necessary packages using the versions listed below:

### **Anaconda Environment**
#### **Pre-processing and Machine Learning Settings**
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

### **Steps for Manual Installation**
1. Create a new environment using Anaconda:
   ```bash
   conda create -n custom_env python=3.11.8
   conda activate custom_env
   ```
2. Install the required packages individually:

   ```bash
   conda install jupyterlab=4.0.11 numpy=1.24.4 matplotlib=3.8.0 tqdm=4.66.2
   pip install tensorflow==2.10.0 keras==2.10.0 segmentation_models_3D==1.0.0
   pip install skimage==0.22.0 patchify==0.2.2 tifffile==2024.2.12
   pip install bm3d==4.0.1 bm4d==4.2.3 napari==0.4.19.post1
   ```
3. Add any additional dependencies required for your specific tasks.

---

## **Note**
- If you do not have access to a GPU or do not need to train models, it is recommended to use only the packages under the Pre-processing Settings column.
- For GPU training, ensure that CUDA and CuDNN are correctly installed and compatible with TensorFlow.
  
---

## **Global Settings**

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

## **Contact**
If further assistance is required, please contact:  
**Ding Yang Wang**  
Email: [deweywang2000@gmail.com](mailto:deweywang2000@gmail.com)
