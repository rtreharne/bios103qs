
import cv2
import numpy as np

def count_circles(file_path):
    # Read the image
    img = cv2.imread(file_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    gray_blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply HoughCircles transform
    circles = cv2.HoughCircles(gray_blur, cv2.HOUGH_GRADIENT, 1, 20, param1=5, param2=10, minRadius=5, maxRadius=10)

    # Count the number of circles detected
    count = len(circles[0])

    # Draw circles on the original image
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(img, (x, y), r, (0, 255, 0), 2)

    # Save the annotated image
    cv2.imwrite(f"{file_path[:-4]}_annotated.jpg", img)

    return count

# Example usage:
filename = "hemocytometer_slide.png"  # Replace with your image file path
num_circles = count_circles(filename)
print(f"Number of circles in {filename}: {num_circles}")
