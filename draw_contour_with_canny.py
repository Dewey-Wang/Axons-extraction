import cv2 as cv
import numpy as np
import argparse

ap = argparse.ArgumentParser()

# Add the arguments with default values and types
ap.add_argument("-i", "--image", required=True, help="Path to the image")
ap.add_argument("-ith", "--initial_threshold", default=100, type=int, help="initial threshold")
ap.add_argument("-mth", "--maximum_threshold", default=255, type=int, help="maximum threshold")

# Parse the command line arguments
args = ap.parse_args()

# Access the values of arguments
image_path = args.image
threshold = args.initial_threshold
max_thresh = args.maximum_threshold

# Global variable to track if grayscale conversion has been done
grayscale_converted = False

# Define the thresh_callback function
def thresh_callback(threshold_1, threshold_2, image):
    global grayscale_converted

    if not grayscale_converted and len(image.shape) == 3 and image.shape[2] == 3:
        message = "The input image is not grayscale. Converting to grayscale."
        print((f"**{message}**"))
        image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        grayscale_converted = True
    else:
        image_gray = image

    canny_output = cv.Canny(image_gray, threshold_1, threshold_2, apertureSize = 5,L2gradient = True )

    # Find contours
    contours, hierarchy = cv.findContours(canny_output, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    # Draw contours
    drawing = np.copy(image)
    cv.drawContours(drawing, contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv.LINE_AA)
    # Show in a window
    cv.imshow('Contours', drawing)

# Load image
src = cv.imread(image_path, cv.IMREAD_COLOR)  # Replace this line with your actual image data

# Create Window
cv.namedWindow('Contours')

# Create trackbars and set the callback function
cv.createTrackbar('Canny Thresh_1:', 'Contours', threshold, max_thresh, lambda x, src=src: None)
cv.createTrackbar('Canny Thresh_2:', 'Contours', threshold, max_thresh, lambda x, src=src: None)

while True:
    # Get current values from the trackbars
    threshold_1 = cv.getTrackbarPos('Canny Thresh_1:', 'Contours')
    threshold_2 = cv.getTrackbarPos('Canny Thresh_2:', 'Contours')

    # Call the callback function with the current values
    thresh_callback(threshold_1, threshold_2, src)

    # Check for 'E' key press
    key = cv.waitKey(1) & 0xFF
    if key == ord('e') or key == ord('E'):
        break

# Destroy all windows when 'E' is pressed
cv.destroyAllWindows()
