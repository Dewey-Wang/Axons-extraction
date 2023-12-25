import cv2 as cv
import numpy as np
import argparse

ap = argparse.ArgumentParser()

# Add the arguments with default values and types
ap.add_argument("-i", "--image", required=True, help="Path to the image")
ap.add_argument("-ith", "--initial_theshold", default=100, type=int, help="initial threshold")
ap.add_argument("-mth", "--maximum_theshold", default=255, type=int, help="maximum_theshold")

# Parse the command line arguments
args = ap.parse_args()

# Access the values of arguments
image_path = args.image
threshold = args.initial_theshold
max_thresh = args.maximum_theshold

# Global variable to track if grayscale conversion has been done
grayscale_converted = False

# Define the thresh_callback function
def thresh_callback(threshold, image):
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    _, binary_img = cv.threshold(gray_image, threshold, 255, cv.THRESH_BINARY)

    # Find contours
    contours, hierarchy = cv.findContours(binary_img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    # Draw contours
    drawing = np.copy(image)
    cv.drawContours(drawing, contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv.LINE_AA)
    # Show in a window
    cv.imshow('Contours', drawing)

# Load image
src = cv.imread(image_path, cv.IMREAD_COLOR)  # Replace this line with your actual 

# Create Window
cv.namedWindow('Contours')

# Create trackbar and set the callback function
cv.createTrackbar('Canny Thresh:', 'Contours', threshold, max_thresh, lambda x, src=src: thresh_callback(x, src))

thresh_callback(cv.getTrackbarPos('Canny Thresh:', 'Contours'), src)
while True:
    # Check for 'E' key press
    key = cv.waitKey(1) & 0xFF
    if key == ord('e') or key == ord('E'):
        break

# Destroy all windows when 'E' is pressed
cv.destroyAllWindows()
