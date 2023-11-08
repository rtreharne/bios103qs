# count_zip.R script file

# Load my existing hemo-tools.R script
source("hemo-tools.R")

# Extract all images from hemo.zip to a new directory
unzip("hemo.zip", exdir = "image_files")

# Get a list of all image files in the new directory
image_files <- list.files("image_files", pattern = ".png", full.names = TRUE)

# Loop through all image files and count the number of cells in each
results <- c()
cat("Counting number of viable cells in each image ...")
for (i in 1:length(image_files)) {
  results[i] <- count_objects(image_files[i])
}
cat(" Done! \n")

# Calculate cell concentrations
cell_concentrations <- results * 2 * 1e4 / 9

# Output mean and sd of cell concentrations
cat(" Mean cell concentration: ", 
    sprintf("%.2e", mean(cell_concentrations)), " cells/mL\n",
    "Standard deviation:",
    sprintf("%.2e", sd(cell_concentrations)), " cells/mL \n")

# Plot a histogram of cell concentrations and include 95% confidence interval
hist(cell_concentrations, 
     main = "Cell Concentrations", 
     xlab = "Cell Concentration (cells/mL)",
     ylab = "Frequency",
     breaks = 10,
     col = "lightblue",
     border = "black",
     freq=FALSE)

# Add a vertical line at the mean
abline(v = mean(cell_concentrations), col = "red")

# Add a vertical line at the mean + 2 standard deviations
abline(v = mean(cell_concentrations) + 2 * sd(cell_concentrations), col = "red", lty = 2)

# Add a vertical line at the mean - 2 standard deviations
abline(v = mean(cell_concentrations) - 2 * sd(cell_concentrations), col = "red", lty = 2)

# Add a normal distribution curve
# Create a sequence of values from the minimum to the maximum cell concentration
x <- seq(min(cell_concentrations), max(cell_concentrations), length = 100)

# Calculate the normal distribution for the sequence of values
y <- dnorm(x, mean = mean(cell_concentrations), sd = sd(cell_concentrations))

# Plot the normal distribution curve
lines(x, y, col = "blue", lwd = 2)

# Add a legend
legend("topright", 
       legend = c("Data", "Mean", "95% CI", "Normal Distribution"), 
       col = c("lightblue", "red", "red", "blue"), 
       lty = c(1, 1, 2, 1), 
       lwd = c(1, 1, 1, 2))

# Make the plot landscape
# Set the margins
par(mar = c(5, 5, 1, 1))

# Rotate the plot 90 degrees
par(mai = c(1, 1, 5, 1))







# Perform a Shapiro-Wilks test.
# If p < 0.5 then reject null hypothesis that data is normally distributed.
print(shapiro.test(cell_concentrations))