import napari
import numpy as np
import os
import tifffile as tiff
from tkinter import filedialog, Tk

class ImageEditor:
    def __init__(self, image_dataset, sharpened_img_dataset, mask_dataset):
        self.image_dataset = self.normalize(image_dataset)
        self.sharpened_img_dataset = self.normalize(sharpened_img_dataset)
        self.mask_dataset = mask_dataset
        self.current_index = 0
        self.viewer = None
        self.directory_path = self.choose_save_directory()
        self.save_datasets_once = False  # Flag to ensure datasets are saved only once
        self.focus_id = None  # Store the most recently selected label ID
        self.transpose = None  # To store original camera angles

    def normalize(self, dataset):
        # Normalize each 3D image in the dataset
        normalized_dataset = np.zeros_like(dataset, dtype=np.float32)
        for i in range(dataset.shape[0]):
            img = dataset[i]
            non_zero_pixels = img[img > 0]
            if len(non_zero_pixels) > 0:
                min_val = np.min(non_zero_pixels)
                max_val = np.max(non_zero_pixels)
                normalized_img = (img - min_val) / (max_val - min_val)
                normalized_img[img == 0] = 0  # Set original zero values back to zero
                normalized_dataset[i] = normalized_img
            else:
                normalized_dataset[i] = img
        return normalized_dataset

    def choose_save_directory(self):
        root = Tk()
        root.attributes("-topmost", True)
        root.withdraw()
        directory_path = filedialog.askdirectory(
            title="Select a directory to save your files"
        )
        root.destroy()
        if not directory_path:
            raise Exception("No directory selected. Operation aborted.")
        return directory_path

    def start(self):
        # Ask the user to enter the starting index
        try:
            user_index = int(input(f"Enter the image index to start with (0 to {self.image_dataset.shape[0] - 1}): "))
            if 0 <= user_index < self.image_dataset.shape[0]:
                self.current_index = user_index
            else:
                print(f"Invalid index. Starting from index 0.")
                self.current_index = 0
        except ValueError:
            print("Invalid input. Starting from index 0.")
            self.current_index = 0

        self.show_image(self.current_index)

    def show_image(self, index):
        self.viewer = napari.Viewer()
        self.viewer.add_image(self.image_dataset[index], name=f"Image {index}")
        self.viewer.add_image(self.sharpened_img_dataset[index], name=f"sharpened Image {index}")
        self.mask_layer = self.viewer.add_labels(self.mask_dataset[index], name=f"Mask {index}")
        
        # Initialize current_dims_order with the initial order
        self.current_dims_order = tuple(self.viewer.dims.order)
        
        # Bind an event listener to check for changes in dims order
        self.viewer.dims.events.order.connect(self.check_dims_order_change)


        # Add mouse drag callback for selecting label IDs
        @self.mask_layer.mouse_drag_callbacks.append
        def report_selected_label_id(layer, event):
            active_layer = self.viewer.layers.selection.active

            if active_layer.mode == 'pick':
                start_point, end_point = layer.get_ray_intersections(
                    position=event.position,
                    view_direction=event.view_direction,
                    dims_displayed=event.dims_displayed,
                    world=True
                )

                num_points = int(end_point[0]) + 1
                intermediate_points = np.linspace(start_point, end_point, num_points)

                for point in intermediate_points:
                    point = tuple(point)
                    val = layer.get_value(point)
                    if val != 0 and val is not None:
                        self.focus_id = val  # Store only the most recent label ID
                        print(f"Selected Focus ID: {self.focus_id}")
                        break

        # Bind 'c' key to confirm and segment the image
        @self.viewer.bind_key('c')
        def confirm_and_segment(event):
            if self.focus_id is not None:
                mask = (self.mask_layer.data == self.focus_id)
                segmented_image = self.image_dataset[index] * mask  # Assuming mask is binary
                sharpened_segmented_image = self.sharpened_img_dataset[index] * mask
                self.viewer.add_image(segmented_image, name=f'Segmented Image (Label {self.focus_id})')
                self.viewer.add_image(sharpened_segmented_image, name=f'Sharpened Segmented Image (Label {self.focus_id})')



        # Bind 'v' key to toggle between original view and y-z plane view
        @self.viewer.bind_key('v')
        def toggle_view(event):
            # Check current dims order and toggle between original and (1, 2, 0)
            if self.viewer.dims.order == (1, 2, 0) or self.viewer.dims.order == (1, 0, 2):
                if self.transpose == 0:
                    self.viewer.dims.order = (0, 1 ,2)
                    self.viewer.layers.selection.active.mode = 'fill'

                else:
                    self.viewer.dims.order = (0, 2, 1)
                    self.viewer.layers.selection.active.mode = 'fill'
    
                    print("Switched back to original view")
            else:
                # Save the current order as original and switch to (1, 2, 0)
                if self.current_dims_order ==  (0,2,1):
                    self.viewer.dims.order = (1, 0, 2)
                    self.viewer.camera.angles = (-90, 0, 0)
                    self.viewer.layers.selection.active.mode = 'fill'
                    self.transpose = 1

                else:
                    self.viewer.dims.order = (1, 2, 0)
                    self.viewer.layers.selection.active.mode = 'fill'
                    self.transpose = 0
    
                    self.viewer.camera.angles = (180, 270, 0)
                print("Switched to y-z plane view")



        # Bind 's' key to save and close the current image
        @self.viewer.bind_key('s')
        def save_and_exit(event):
            self.save_and_close(index)

        # Bind 'n' key to skip saving and go to the next image
        @self.viewer.bind_key('n')
        def skip_and_next(event):
            print(f"skip {index} image.")
            self.current_index += 1
            if self.current_index < self.image_dataset.shape[0]:
                self.viewer.close()  # Close the current viewer
                self.show_image(self.current_index)
            else:
                print("This is the last image!")
                self.current_index = self.image_dataset.shape[0]

        # Bind 'r' key to return to the previous image
        @self.viewer.bind_key('r')
        def return_previous(event):
            print(f"return to {index} image.")
            self.current_index -= 1
            if self.current_index >= 0:
                self.viewer.close()  # Close the current viewer
                self.show_image(self.current_index)
            else:
                print("This is the first image!")
                self.current_index = 0
        
        napari.run()


    def check_dims_order_change(self, event):
        new_order = tuple(self.viewer.dims.order)
        if new_order != self.current_dims_order:
            self.current_dims_order = new_order  # Update the stored order
            
    def save_and_close(self, index):
        self.mask_dataset[index] = self.mask_layer.data.astype(np.uint8)
        print(f"Mask {index} updated.")

        mask_save_path = os.path.join(self.directory_path, 'mask_dataset.tiff')
        tiff.imwrite(mask_save_path, self.mask_dataset)
        print(f"Mask saved to {mask_save_path}")

        if not self.save_datasets_once:
            image_save_path = os.path.join(self.directory_path, 'image_dataset.tiff')
            sharpened_save_path = os.path.join(self.directory_path, 'sharpened_img_dataset.tiff')
            tiff.imwrite(image_save_path, self.image_dataset)
            tiff.imwrite(sharpened_save_path, self.sharpened_img_dataset)
            print(f"Image dataset saved to {image_save_path}")
            print(f"Sharpened image dataset saved to {sharpened_save_path}")
            self.save_datasets_once = True

        self.viewer.close()
        self.current_index += 1

        if self.current_index < self.image_dataset.shape[0]:
            self.show_image(self.current_index)

