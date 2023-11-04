# count_zip.R script file

# Load my existing hemo-tools.R script
source("11_CELL_BIOLOGY/hemo-tools.R")

# Extract all images from hemo.zip to a new directory
unzip("11_CELL_BIOLOGY/hemo.zip", exdir = "11_CELL_BIOLOGY/image_files")

# Get a list of all image files in the new directory
image_files <- list.files("11_CELL_BIOLOGY/image_files", pattern = ".png", full.names = TRUE)

# Loop through all image files and count the number of cells in each
results <- c()
cat("Counting number of viable cells in each image ...")
for (i in 1:length(image_files)) {
  results[i] <- count_objects(image_files[i])
}
cat(" Done! \n")

# Calculate cell concentrations
cell_concentrations <- results * 2 * 1e4 / 9

# Output meand and sd of cell concentrations
cat(" Mean cell concentration: ", 
    sprintf("%.2e", mean(cell_concentrations)), " cells/mL\n",
    "Standard deviation:",
    sprintf("%.2e", sd(cell_concentrations)), " cells/mL \n")

# Plot a histogram of cell concentrations
hist(
        cell_concentrations,
        breaks = 20,
        col = "lightblue",
        main = "Number of cells per image",
        xlab = "Number of cells"
    )

# Perform a Shapiro-Wilks test.
# If p < 0.5 then reject null hypothesis that data is normally distributed.
print(shapiro.test(cell_concentrations))