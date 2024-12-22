import argparse
import cv2
import numpy as np

points = []
cropping = False

def shape_selection(event, x, y, flags, param):
    global points, cropping

    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        cropping = True

    elif event == cv2.EVENT_LBUTTONUP:
        points.append((x, y))
        cropping = False

        if len(points) >= 2:
            # Draw a polygon around the selected points
            cv2.polylines(image, [np.array(points)], isClosed=True, color=(255, 255, 255), thickness=2)
            cv2.imshow("image", image)

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", shape_selection)

while True:
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("r"):
        image = clone.copy()
        points = []  # Reset points on 'r' keypress

    elif key == ord("s") and len(points) >= 2:
        # Check if at least two points are selected
        mask = np.zeros_like(image)  # Create a mask for the polygon
        roi_corners = np.array([points], dtype=np.int32)
        cv2.fillPoly(mask, roi_corners, (255, 255, 255))  # Fill the polygon with white color

        # Apply the mask to the original image
        result = cv2.bitwise_and(clone, mask)

        # Display the result
        cv2.imshow("crop_img", result)
        cv2.imwrite("cropped_region.jpg", result)
        print("Cropped region saved as 'cropped_region.jpg'")
        break  # Break out of the loop after saving

    elif key != 255:  # Check if any key is pressed (excluding special keys)
        break  # Break out of the loop if any key is pressed

if len(points) >= 2:
    # Draw the final polygon on the image
    cv2.polylines(image, [np.array(points)], isClosed=True, color=(255, 255, 255), thickness=2)
    cv2.imshow("image", image)
    cv2.waitKey(0)

cv2.destroyAllWindows()