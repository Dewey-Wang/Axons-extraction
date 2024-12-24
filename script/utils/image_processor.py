import os
import numpy as np
import tifffile
from tqdm import tqdm
from LifFileProcessor import LifImageProcessor
from matplotlib import pyplot as plt
from QuestionMaster import Questions
import file_utilities as fu

def process_image():
    # Get the file path
    file_path = fu.choose_file()

    # Check if the file is .tif or .lif
    if file_path.endswith('.lif'):
        return process_lif_file(file_path)
    elif file_path.endswith('.tif'):
        return process_tiff_file(file_path)
    elif file_path.endswith('.tiff'):
        return process_tiff_file(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a .tif/.tiff or .lif file.")

def process_lif_file(file_path):
    # Create an instance of LifImageProcessor
    lif_processor = LifImageProcessor(file_path)
    
    # Calculate the sum of series
    sum_of_series = lif_processor.calculate_sum_of_series()
    print("Sum of series:", sum_of_series)
    
    # Input the desired series number with validation
    while True:
        question = Questions("Please enter the serie number that you're interested in:")
        serie_number = question.ask_question(input_type='int')
        if 1 <= serie_number <= sum_of_series:
            break
        else:
            print(f"Please enter a valid number between 1 and {sum_of_series}.")
    
    # Select images based on the series number
    selected_list, z_list, x_list, y_list, corrected_m = lif_processor.select_images_by_series_number(serie_number)
    
    # Print additional information about the selected images
    print("The number of the image that you selected is at section", len(selected_list),
          "when the m = ", str(corrected_m), "when the z = ", str(z_list[-1]))
    
    # Example of using the selected image
    selected_image = selected_list[-1]
    sum_of_channels = len([i for i in selected_image.get_iter_c(t=0, z=0)])
    print("Sum of channels:", sum_of_channels)
    
    # Input the desired channel number with validation
    while True:
        question = Questions("Please enter the channel number that you're interested in:")
        channel_number = question.ask_question(input_type='int')
        if 1 <= channel_number <= sum_of_channels:
            break
        else:
            print(f"Please enter a valid number between 1 and {sum_of_channels}.")
    
    # Get the image frame
    frame = selected_image.get_frame(z=int(z_list[-1]) - 1, t=0, c=channel_number-1)
    image = np.array(frame)
    
    print("shape: {}".format(image.shape))
    print("dtype: {}".format(image.dtype))
    print("range: ({}, {})".format(np.min(image), np.max(image)))
    
    # Create and display the integrated image and a slice from the 3D image
    integrated_image, image_3D = lif_processor.create_integrated_image(selected_list, z_list, x_list, y_list, channel_number-1)
    return integrated_image, image_3D

def process_tiff_file(file_path):
    # Load .tif file
    image_3D = tifffile.imread(file_path)
    print(f"Loaded TIFF file with shape: {image_3D.shape}")
    
    # Initialize an integrated image
    integrated_image = np.zeros((image_3D.shape[1], image_3D.shape[2]), dtype=np.uint8)
    
    # Loop through the Z dimension and perform max projection
    for i in tqdm(range(image_3D.shape[0]), desc="Processing Z Values", unit="z"):
        for x in range(image_3D.shape[1]):
            for y in range(image_3D.shape[2]):
                if integrated_image[x][y] < image_3D[i][x][y]:
                    integrated_image[x][y] = image_3D[i][x][y]
                    
    return integrated_image, image_3D

if __name__ == "__main__":
    integrated_image, image_3D = process_image()
    # Displaying the integrated and 3D image
    plt.figure(figsize=(16, 8))
    
    plt.subplot(1, 2, 1)
    plt.imshow(integrated_image, cmap='gray')
    plt.title('Integrated Image')

    plt.subplot(1, 2, 2)
    plt.imshow(image_3D[0], cmap='gray')
    plt.title('3D Image Slice')

    plt.show()
