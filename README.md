# README for Master’s Thesis

## Title
**Establishment of Neural Network Pipeline for Automated Identification of Mouse Spinal Cord Axons**

## Author
**Ding Yang Wang**  

## Institution
**Ludwig-Maximilians-Universität München**  
**Department of Biology, Molecular and Cellular Biology**

## Supervisor
**Prof. Dr. med. Martin Kerschensteiner**  
Email: [Martin.Kerschensteiner@med.uni-muenchen.de](mailto:Martin.Kerschensteiner@med.uni-muenchen.de)

---

## Abstract
This thesis focuses on the development of a neural network pipeline designed to automate the identification of axons in mouse spinal cord images. The proposed solution integrates deep learning techniques with advanced image processing, enabling efficient and accurate identification. This work has potential applications in neurobiology, specifically for improving the understanding of spinal cord injuries and axonal behaviors.

## Repository Overview
This repository contains all code and data required to reproduce the results presented in the thesis. Below is an overview of the structure:

- `src/` - Core source code for the neural network pipeline.
- `data/` - Sample datasets and preprocessed images.
- `models/` - Pre-trained and fine-tuned models.
- `notebooks/` - Jupyter notebooks for visualization and analysis.
- `results/` - Generated outputs, including figures and performance metrics.
- `docs/` - Documentation and supplementary materials.
- `instruction.ipynb` - Step-by-step operation guide for setting up and running the pipeline.

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

