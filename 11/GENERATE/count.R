# Load necessary libraries
library(png)
library(EBImage)

# Function to count the number of objects in an image

count_objects <- function(image_path, threshold = 0.5) {
  # Read the image
  img <- readPNG(image_path)

  # Convert the image to grayscale
  gray_img <- channel(img, "gray")

  # Apply thresholding to create a binary image
  binary_img <- gray_img > threshold

  # Find connected components
  cc <- bwlabel(binary_img)

  # Count the number of objects
  num_objects <- max(cc) - 1

  # Print the result
  cat("Number of objects:", num_objects, "\n")
  
  return(num_objects)
}

count_blue_circles <- function(image_path, threshold = 0.99) {
  # Read the image
  img <- readPNG(image_path)

  # Convert the image to grayscale
  gray_img <- channel(img, "gray")

  # Apply thresholding to create a binary image
  binary_img <- gray_img > threshold

  # Find connected components
  cc <- bwlabel(binary_img)

  # Identify blue circles
  blue_mask <- img[,,3] > img[,,2] & img[,,3] > img[,,1]

  # Find connected components within blue regions
  blue_cc <- bwlabel(blue_mask)

  # Count the number of blue circles
  num_blue_circles <- max(blue_cc)


  
  return(num_blue_circles)
}

# Example usage
result <- count_blue_circles("11/GENERATE/hemocytometer_slide.png")
print(result)


# Example usage
result <- count_objects("11/GENERATE/hemocytometer_slide.png")
print(result)

