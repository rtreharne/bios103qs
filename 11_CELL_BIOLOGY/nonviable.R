# Load necessary libraries
library(png)
library(EBImage)


count_blue_objects <- function(image_path, blue_threshold = 0.5) {
  # Read the image
  img <- readPNG(image_path)
  
  # Split the image into R, G, B channels
  red_channel <- img[,,1]
  green_channel <- img[,,2]
  blue_channel <- img[,,3]
  
  # Create a binary mask for blue regions
  # Only pixels where the blue channel is strong and dominates red and green will be counted
  blue_mask <- (blue_channel > blue_threshold) & (blue_channel > red_channel) & (blue_channel > green_channel)
  
  # Find connected components in the blue mask
  cc <- bwlabel(blue_mask)
  
  # Count the number of blue objects
  num_blue_objects <- max(cc)
  
  return(num_blue_objects)
}
