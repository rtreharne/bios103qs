# count.R script file

# Load my existing hemo-tools.R script
source("hemo-tools.R")

# Count the number of cells in the image
result <- count_objects("hemo.png")

# Calculate cell concentration
cell_concentration <- result * 2 * 1e4 / 9

# Print the total number of cells
cat("Total number of cells:", result, "\n")

# Print the cell concentration in standard form and to 2 decimal places
cat("Cell concentration:", 
    sprintf("%.2e", cell_concentration), 
    "cells/mL\n")
