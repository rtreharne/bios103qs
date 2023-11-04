
# Import count_objects function from hemo_count.R
source("11_CELL_BIOLOGY/ANALYSIS/hemo_count.R")

# extract images from "11/DATA/hemo.zip"
unzip("11_CELL_BIOLOGY/DATA/hemo.zip", exdir = "11_CELL_BIOLOGY/ANALYSIS/image_files")

# get list of image files in image_files dir
image_files <- list.files("11_CELL_BIOLOGY/ANALYSIS/image_files", pattern = ".png", full.names = TRUE)

# loop through image files and count objects. Create a vector to store the results
results <- c()
for (i in 1:length(image_files)) {
  results[i] <- count_objects(image_files[i])
}

# Calculate cell concentraition
cell_concentration <- results * 2 * 1e4

# plot a histogram of results
#hist(cell_concentration, breaks = 20, col = "lightblue", main = "Number of cells per image", xlab = "Number of cells")

shapiro.test(results)

summary(cell_concentration)

value <- 1700000

# perform a one-sample t-test
t.test(cell_concentration, mu = value)
