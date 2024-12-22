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
1. **Preprocessing**:
   - Image denoising using BM3D, BM4D, and bilateral filtering.
2. **Segmentation - ground truth generation**:
   - Semi-automatic segmentation using thresholding and CCL.
   - Using napari to manual correct the segmentaion from thresholding and CCL.-This step is to make ground truth image.
3. **Training Data preparation**:
   - create the algorithums to transfer the segmentation labeled image into semantic image. 
4. **Data Augmentation**:
   -  Utilized `torchio` libraries to expand dataset diversity.
5. **Model Trainning**:
   - Trainning 3D-Unet model and VGG16-backboned 3D-Unet model. 
6. **Model Estimation**:
   - Compared model predictions with ground truth annotations.
   - Achieved classification accuracy: **Background (0.99)**, **Axons (0.85)**, and **Borders (0.65)**.
   
---

## Usage
The general instructions provided in `instruction.ipynb`. Detailed usage instructions are available in the respective subdirectories. 

---

## **Repository Structure**

| **Directory**          | **Description**                           |
|-------------------------|------------------------------------------|
| `/script`               |Scripts for the whole project.            |
| `/example data`         | Sample images.                           |
| `/trained model`        | The pre-trained model with the settings. |
| `/env`                  | Have the detail of my env settings.      |


---

## Technical Requirements
### Equipment
| **Equipment**           | **Description**            | **Manufacturer** |
|--------------------------|----------------------------|------------------|
| NVIDIA RTX 3060 Ti       | 8GB-GPU                   | ASUS            |
| AMD Ryzen 9 5950X        | 128GB-16 core-CPU         | AMD             |
| SP8                      | Confocal microscopy       | Leica           |

---

## **Data Source**

This repository does not include raw microscopy datasets due to privacy and licensing restrictions. If you'd like to replicate the pipeline, you will need to obtain suitable microscopy images of axons. Please refer to the scripts for data format and preprocessing requirements.

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
