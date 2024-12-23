import cv2 as cv
import os
import numpy as np
from matplotlib import pyplot as plt
from skimage.color import rgb2gray
import subprocess

__all__ = [
    'process_cropped',
    'mask_3D_image'
]

def process_cropped(integrated_image, remove_generated_image=True):
    """
    Crop a region from the provided integrated image.
    
    Args:
        integrated_image (numpy.ndarray): The input image to crop.
        remove_generated_image (bool): Whether to remove the intermediate images.
        
    Returns:
        cropped_image (numpy.ndarray): The cropped region of the image.
    """
    # Save the NumPy array as an image file
    image_path = "./integrated_image.jpg"  # Specify the desired path and file name
    cv.imwrite(image_path, integrated_image)

    # Call the capture_partial_image.py script with the image path
    script_path = "./capture_partial_image.py"  # Replace with the actual path
    subprocess.run(["python", script_path, "--image", image_path], check=True)

    cropped_image = cv.imread("./cropped_region.jpg")
    print("Script executed successfully.")

    # Convert to grayscale and scale the intensity
    cropped_image = np.uint8(rgb2gray(cropped_image) * 255)
    plt.imshow(cropped_image, cmap='gray')

    if remove_generated_image:
        os.remove("./cropped_region.jpg")
        os.remove("./integrated_image.jpg")
    return cropped_image


def mask_3D_image(image_3D, cropped_image):
    """
    Mask the 3D image with the cropped 2D image.

    Args:
        image_3D (numpy.ndarray): The 3D image to be masked.
        cropped_image (numpy.ndarray): The 2D mask (cropped region).

    Returns:
        numpy.ndarray: Masked 3D image.
    """
    # Mask the merged with cropped image
    zero_mask = (cropped_image == 0)

    # Set corresponding values in image_3D to 0
    image_3D[:, zero_mask] = 0
    return image_3D
