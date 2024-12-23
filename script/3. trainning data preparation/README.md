# **Generate Border.ipynb**

This notebook provides three different methods to generate semantic label images for training 3D-Unet models. These semantic images include three classes:
- **0 (Background)**: Regions with no axons or borders.
- **1 (Axons)**: Regions occupied by axons.
- **2 (Borders)**: Boundary regions separating axons.

The generated borders help distinguish individual axons during training, enhancing model performance. Users can choose among the three available methods based on their requirements.

---

## **Purpose**
- Transfer label images into semantic label images with classes 0, 1, and 2.
- Provide flexibility in border generation methods to suit different dataset characteristics.

---

## **Methods Overview**

### **1. Generate Borders Everywhere**
This method creates borders around all labeled regions, ensuring clear separation between any adjacent regions, including touching axons.

- **Process**:
  - Identifies unique intensity values in small patches.
  - Replaces regions with mixed intensities with borders (class 2).
  - Applies dilation to ensure consistent border thickness.
- **Use Case**:
  - Useful for datasets where all adjacent labels must be distinctly separated.
- **Output**:
  - **Borders**: 2 (Between all labels).
  - **Axons**: 1 (Remaining labeled regions).
  - **Background**: 0.

---

### **2. Generate Borders Between Connected Labels**
This method focuses on generating borders only between touching labels. 

- **Process**:
  - Examines adjacent labels in the x-y and y-z planes.
  - Identifies transitions between touching labels and inserts borders.
- **Use Case**:
  - Ideal for datasets where clear boundaries between connected labels are critical.
- **Output**:
  - **Borders**: 2 (Only at touching points between labels).
  - **Axons**: 1.
  - **Background**: 0.

---

### **3. Generate Borders Based on YZ Plane (Recommended)**
This method, used in the associated research, emphasizes creating borders based on adjacent regions in the y-z plane and applies dilation to emphasize the borders.

- **Process**:
  - Dilates each slice in the y-z plane to identify borders.
  - Integrates additional borders between connected labels.
  - Swaps axes to ensure consistent 3D representation.
- **Use Case**:
  - Recommended for training 3D-Unet models, as it balances clear border delineation with axon segmentation accuracy.
- **Output**:
  - **Borders**: 2 (Based on y-z adjacency and touching labels).
  - **Axons**: 1.
  - **Background**: 0.

---

## **How to Use**

### File Selection
The notebook allows users to load label images using the `file_utilities` module:
```python
from skimage import io
import file_utilities as fu

# Select file
file_path = fu.choose_file()
image = io.imread(file_path)
```

---

### Choose a Method
Users can select one of the three border generation methods by running the corresponding function:
```python
# Method 1: Generate Borders Everywhere
border, labeled, label_with_border = generate_border_3d(image)

# Method 2: Generate Borders Between Connected Labels
border, labeled, label_with_border = generate_border_3d(image, border_size=1)

# Method 3 (Recommended): Generate Borders Based on YZ Plane
border, labeled, label_with_border = generate_border_3d(image)
```

---

### Visualization
The generated semantic image can be visualized using Napari:
```python
import napari

viewer = napari.Viewer()
viewer.add_labels(label_with_border, name='Semantic Image')
napari.run()
```

---

## **Comparison of Methods**

| **Method**                     | **Key Characteristics**                                                        | **Use Case**                                            |
|--------------------------------|--------------------------------------------------------------------------------|--------------------------------------------------------|
| **Borders Everywhere**         | Adds borders between all adjacent regions.                                     | Suitable for datasets with low-density axons.       |
| **Borders Between Connections**| Focuses on touching labels, minimizing unnecessary borders.                    | Ideal for datasets with minimal touching axons.        |
| **Borders Based on YZ Plane**  | Adds borders in the y-z plane with additional dilation for consistency.         | Recommended for robust 3D-Unet training datasets.      |

---

## **Contact**
For questions or additional assistance:
**Ding Yang Wang**  
[deweywang2000@gmail.com](mailto:deweywang2000@gmail.com)
