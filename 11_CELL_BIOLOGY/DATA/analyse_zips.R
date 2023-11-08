#setwd("11_CELL_BIOLOGY/DATA")

# Load my existing hemo-tools.R script
source("..//hemo-tools.R")

count_cells <- function(zip_file_path, pattern = ".png") {
    # Extract all images from the zip file to a new directory
    unzip(zip_file_path, exdir = "image_files")

    # Get a list of all image files in the new directory
    image_files <- list.files("image_files", pattern = pattern, full.names = TRUE)

    # Loop through all image files and count the number of cells in each
    results <- c()
    cat("Counting number of viable cells in each image ...")
    for (i in 1:length(image_files)) {
        results[i] <- count_objects(image_files[i])
    }
    
    return(results)
}

# Get all filenames with zip extension
zip_paths <- list.files(cwd, pattern = "\\.zip$", full.names = TRUE)

# Loop through all zip files and calculate the mean number of cells in each
means <- c()

for (i in 1:length(zip_paths)) {
    print(zip_paths[i])
    
    # Unzip the zip file to temp directory
    unzip(zip_paths[i], exdir = "image_files")

    # Get all fnames in image_files
    image_files <- list.files("image_files", pattern = ".png", full.names = TRUE)
    
    counts <- c()

    # Count the number of cells in each image
    for (j in 1:length(image_files)) {
       counts[j] <- count_objects(image_files[j])
    }

    # Calculate the mean number of cells in each image
    means[i] <- mean(counts)
    stds[i] <- sd(counts)

    print(paste("Mean number of cells:", means[i]))
    print(paste("Standard deviation:", stds[i]))
}

# Create a datatable with the zip filename and the mean number of cells
results <- data.frame(zip_paths, means, stds)

# Save as a .csv file
write.csv(results, "results.csv", row.names = FALSE)


