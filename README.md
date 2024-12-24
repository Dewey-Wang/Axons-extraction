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
   - **Key Packages**: `BM3D`, `BM4D`, `pyclesperanto_prototype`, `skimage`.
   - **Custom Python Scripts**: `image_processor.py`, `image_cropper.py`, `BM4DProcessor`. (See [README](./script/utils/README.md) for detail.)
   <img src="./for%20readme%20image/preprocessing1.png" alt="Preprocessing Representation" width="300"/>  
   <img src="./for%20readme%20image/signal%201.png" alt="Signal 1" width="240"/>
-
   <img src="./for%20readme%20image/preprocessing2.png" alt="Preprocessing Representation" width="300"/>  
   <img src="./for%20readme%20image/signal%202.png" alt="Signal 2" width="240"/>

   ![After Preprocessing](./for%20readme%20image/after%20preprocessing.gif)

2. **Manual Labeled Image Correction**:
   - **Key Packages**: `napari`, `scipy.ndimage`, `pyclesperanto_prototype`.
   - **Custom Python Scripts**: `napari_editor.py`, `manual_correction_data_loader.py`. (See [README](./script/utils/README.md) for detail.)
   ![After Manual Correction](./for%20readme%20image/after%20manual%20correction.gif)

3. **Semantic Data Generation**:
   - **Key Packages**: `numpy`, `skimage`.
   - **Custom Python Algorithms**: See [notebook](./script/3.%20semantic%20data%20generation/) for detail.
   ![After Semantic Generation](./for%20readme%20image/after%20semantic%20generation.gif)

4. **Data Augmentation**:
   - **Key Packages**: `torchio`, `patchify`.
   - **Custom Python Algorithms**  See [notebook](./script/4.%20data%20augmentation/) for detail.

5. **Training Data Preparation**:
   - **Key Packages**: `patchify`, `scipy.ndimage`.
   - **Custom Python Algorithms**  See [notebook](./script/5.%20trainning%20data%20preparation/) for detail.

6. **Model Training**:
   - **Key Packages**: `tensorflow`, `segmentation_models_3D`, `keras`.

7. **Model Evaluation**:
   - **Key Packages**: `sklearn`, `matplotlib`, `tensorflow`.

8. **Run the Model**:
   - **Key Packages**: `tensorflow`, `patchify`, `tifffile`.
   
---

## **Repository Structure**

| **Directory**          | **Description**                           |
|-------------------------|------------------------------------------|
| `/script`               |Scripts for the whole project.            |
| `/example data`         | Sample images.                           |
| `/trained model`        | The pre-trained model with the settings. |
| `/env`                  | Have the detail of my env settings.      |

---

### **Note**
Each directory corresponding to these workflow stages includes a detailed README file explaining the specific methods, scripts, and outputs. If you are interested in learning more, explore the README files within each folder.

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
