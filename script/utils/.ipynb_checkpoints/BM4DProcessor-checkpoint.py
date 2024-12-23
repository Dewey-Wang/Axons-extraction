import numpy as np
import bm4d
import napari
import numpy as np
import cc3d
from QuestionMaster import Questions




class BM4DProcessor:
    def __init__(self, denoised_images):
        self.denoised_images = denoised_images
        self.non_zero_denoised_images = self.denoised_images[self.denoised_images != 0]
        self.profile = "np"  # 或者使用 "refilter"
        self.PSD = None  # To be set by the user during runtime
        self.threshold_value = None  # To be set by the user during runtime

    def get_user_PSD(self):
        # Ask user if they want to use the default value for PSD
        question = Questions(f"Do you want to use the default value for PSD? The default is std({np.std(self.non_zero_denoised_images)})")
        user_input = question.ask_question(input_type='yes_no')
        if user_input:
            # Use default value for PSD
            self.PSD = np.std(self.non_zero_denoised_images)
        else:
            # Get user input for PSD
            question = Questions("Enter the value for PSD")
            self.PSD = question.ask_question(input_type='num')

    def do_bm4d(self):
        # Execute BM4D denoising
        print("Running BM4D....")
        denoised_image = bm4d.bm4d(self.denoised_images, self.PSD, self.profile)
        return np.array(denoised_image)
    
    def get_user_threshold(self,denoised_image):
        # Ask user if they want to use the default value for threshold
        flat_data = np.array(denoised_image).flatten()
        non_zero_pixels = flat_data[flat_data != 0]
        # Calculate the cumulative distribution function (CDF)
        sorted_pixels = np.sort(non_zero_pixels)

        # Calculate intensity values for 15%
        intensity_015 = np.percentile(sorted_pixels, 15)

        question = Questions(f"Do you want to use the default threshold value for the segmentation? The default is at the 15% of all intensity({intensity_015})")
        user_input = question.ask_question(input_type='yes_no')

        if user_input:
            # Use default value for threshold
            self.threshold_value = intensity_015
        else:
            # Get user input for threshold
            question = Questions("Enter the value for threshold")
            self.threshold_value = question.ask_question(input_type='num')
            
    def label_components(self, denoised_image):
        # Threshold denoised image
        binary_image = denoised_image > self.threshold_value

        # Label connected components
        bm4d_labels = cc3d.connected_components(binary_image, connectivity=6)

        # Filter labels with more than 1000 components
        question = Questions("Enter the minimum label size to keep:")
        min_label_size = question.ask_question(input_type='num')            
        bm4d_selected_labels = [label for label, size in enumerate(np.bincount(bm4d_labels.ravel())) if size > min_label_size]

        # Create a boolean mask
        bm4d_mask = np.isin(bm4d_labels, bm4d_selected_labels)

        # Set labels not in bm4d_selected_labels to 0
        bm4d_labels[~bm4d_mask] = 0

        # Map unique values to sequential integers
        unique_bm4d_labels, inverse_bm4d_indices = np.unique(bm4d_labels, return_inverse=True)
        selected_bm4d_labels_indices = np.digitize(unique_bm4d_labels, bm4d_selected_labels) - 1
        bm4d_labels_flat = selected_bm4d_labels_indices[inverse_bm4d_indices]
        bm4d_labels = bm4d_labels_flat.reshape(bm4d_labels.shape)

        return bm4d_labels
    def run_viewer(self, denoised_image, viewer):
        if viewer is None:
            viewer = napari.Viewer()
            print("You don't have a viewer. Created a new one.")
            viewer.add_image(self.denoised_images, name='Original Image')

        # Add the BM4D denoised image to the Napari viewer
        viewer.add_image(denoised_image, name='BM4D denoised Image')

        # Label components on BM4D denoised image
        bm4d_labels = self.label_components(denoised_image)
        viewer.add_labels(bm4d_labels, name='Selected Components (BM4D)')
        
        # Show the Napari viewer
        napari.run()
        print("Added the BM4D image in your napari")
