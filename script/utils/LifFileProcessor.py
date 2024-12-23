# File: LifFileProcessor.py
from readlif.reader import LifFile

import numpy as np
from matplotlib import pyplot as plt
from tqdm import tqdm
import cv2 as cv
from IPython.display import display, Image
from skimage.color import rgb2gray
import subprocess
import os


class LifImageProcessor:
    def __init__(self, lif_file_path):
        self.lif_file = LifFile(lif_file_path)
        self.img_list = [i for i in self.lif_file.get_iter_image()]
        self.m_values = [int(''.join(char for char in str(item).split("m=")[1].split(",")[0] if char.isdigit())) for item in self.img_list]

    def calculate_sum_of_series(self):
        return sum(self.m_values)

    def select_images_by_series_number(self, serie_number):
        selected_list = []
        z_list, x_list, y_list = [], [], []
        current_sum, corrected_m = 0, 0

        for item in self.img_list:
            m_value = int(''.join(char for char in str(item).split("m=")[1].split(",")[0] if char.isdigit()))
            z_value = int(''.join(char for char in str(item).split("z=")[1].split(",")[0] if char.isdigit()))
            x_value = int(''.join(char for char in str(item).split("x=")[1].split(",")[0] if char.isdigit()))
            y_value = int(''.join(char for char in str(item).split("y=")[1].split(",")[0] if char.isdigit()))

            if current_sum + m_value <= serie_number:
                selected_list.append(item)
                z_list.append(z_value)
                x_list.append(x_value)
                y_list.append(y_value)
                current_sum += m_value
                corrected_m = m_value
            else:
                if current_sum + m_value > serie_number and current_sum != serie_number:
                    selected_list.append(item)
                    z_list.append(z_value)
                    x_list.append(x_value)
                    y_list.append(y_value)
                    current_sum += m_value
                    corrected_m = m_value - (current_sum - serie_number)
                break

        return selected_list, z_list, x_list, y_list, corrected_m

    def create_integrated_image(self, selected_list, z_list, x_list, y_list, channel_num):
        z_value = z_list[-1]
        z_values = np.arange(0, z_value)
    
        x_value = x_list[-1]
        x_values = np.arange(0, x_value)
    
        y_value = y_list[-1]
        y_values = np.arange(0, y_value)
    
        image_3D = np.zeros((z_value, x_value, y_value), dtype=np.uint8)
    
        for i in z_values:
            img = np.array(selected_list[-1].get_frame(z=i, t=0, c=channel_num))
            image_3D[i, :, :] = img
    
        integrated_image = np.zeros((x_value, y_value), dtype=np.uint8)
    
        for i in tqdm(z_values, desc="Processing Z Values", unit="z"):
            for x in x_values:
                for y in y_values:
                    if integrated_image[x][y] < image_3D[i][x][y]:
                        integrated_image[x][y] = image_3D[i][x][y]
    
        return integrated_image, image_3D
