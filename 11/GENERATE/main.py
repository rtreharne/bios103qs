import cv2

def count_cells(filename):
    # Read the image
    image = cv2.imread(filename, cv2.IMREAD_COLOR)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply adaptive thresholding
    thresholded = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                        cv2.THRESH_BINARY_INV, 11, 2)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter out contours that are too square (potential noise)
    min_aspect_ratio = 0.7  # Adjust as needed
    valid_contours = [contour for contour in contours if not (0.7 < cv2.contourArea(contour) / cv2.arcLength(contour, True) < 1.3)]

    # Draw contours on the original image (optional)
    cv2.drawContours(image, valid_contours, -1, (0, 255, 0), 2)

    # Display the image with contours (optional)
    cv2.imshow('Image with Contours', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return len(valid_contours)

# Example usage:
filename = "hemocytometer_slide.png"  # Replace with your image file path
num_cells = count_cells(filename)
print(f"Number of cells in {filename}: {num_cells}")
