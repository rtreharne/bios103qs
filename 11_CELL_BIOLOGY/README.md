# BIOS103 QS WORKSHEET

## Introduction

## Part 1

The image below represents an image captured by a digital microscope from a hemocytometer prepared with 100 &mu;L of initial cell suspension diluted with 100 &mu;L of Trypan blue.

Each white circle (with a black outline) represents a viable red blood cell. Each blue circle represents a non-viable cell.

![Hemocytometer Slide](hemo_grid.png)


### Tasks
1. Following the methodology in this [video](https://youtu.be/pP0xERLUhyc?si=VuGRVFv75Rax0fKF), count the total number of viable cells.
2. Count the total number of non-viable cells.
3. Calculate the percentage of viable cells.
4. Calculate the average number of viable cells per major square.
5. Calculate the concentration of viable cells (cells /  mL)

## Part 2

How long did it take you to calculate the concentration for that single sample? Probably not that long, but what if you had to measure 100 samples? Are you going to do that manually? Good luck with that.

Let's use our coding superpowers to automate the task of counting viable cells and calculating the cell concentration for a single sample. Here's a script called [hemo-tools.R](hemo-tools.R) that I prepared earlier. I don't need you to understand this script line for line, just know that it contains a function called `count_objects()`. This function will analyse a hemocytometer slide image and count the number of viable cells for you. You're welcome!

Download and save the file [hemo-tools.R](hemo-tools.R) to your R project.

Before you use this script you'll need to make sure that you have the `png` and `EBImage` packages installed. In your [R terminal](/glossary.md#r-terminal), run the following lines:

```
install.packages("png")
install.packages("EBImage")
```

OK. We're ready, let's create a new `count.R` script file in our current R project and import `hemo-tools.R`.

```{R}
# count.R script file

# Import the hemo-tools.R script
source("hemo-tools.R")
```

Download the [hemo.png](hemo.png) file to your R project's directory. Note that this file is the same as the image above but without the grid lines. Now let's use the `count_objects()` function to count the number of viable cells as follows:

```{R}
# count.R script file
...

# Use count_objects() on my hemocytometer_slide_no_grid.png file
result <- count_objects("hemo.png")

# Print the total number of cells
cat("Total number of cells:", result, "\n")
```

After running these lines you should see the the following result in your R Terminal:

```{R}
Total number of cells: 78 
```
In other words, the script has identified 78 viable cells in the full image (i.e. 9 squares).

Let's finish off our `count.R` script by also calcuating the concentration of viable cells. 

```
# count.R script file
...

# Calculate cell concentration
cell_concentration <- result * 2 * 1e4 / 9

# Print the cell concentration in standard form and to 2 decimal places
cat("Cell concentration:", 
    sprintf("%.2e", cell_concentration), 
    "cells/mL\n")
```

After running the full script one last time you should see the following in your terminal:
```
Total number of cells: 78 
Cell concentration: 1.73e+05 cells/mL
```
How does this calculation compare with the one you made manually in [part 1](#part-1) above? Your numbers should be pretty similar, but the value provided by the R script is more accurate. Also, now that you've written the script you can use it over and over again without breaking a sweat.


## Part 3
The compressed file [hemo.zip](hemo.zip) contains 100 hemocytomter slides collected from 100 patients (fictional of course). Download this file to your current R project.

Let's augment our `count.R` script to do the following things:
+ Extract all image files in `hemo.zip` to a new folder called `image_files`.
+ Use a loop to apply our `count_objects()` function to each image file in turn and count the total viable cells in each.
+ Calculate the cell concentration for each image.
+ Calculate, and output, the mean cell concentration and standard deviation for all images.

I'll create a new script file called [count_zip.R](count_zip) to do this. Here it is, in its entirety:

```
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

# Output meand and sd of cell concentrations
cat(" Mean cell concentration: ", 
    sprintf("%.2e", mean(cell_concentrations)), " cells/mL\n",
    "Standard deviation:",
    sprintf("%.2e", sd(cell_concentrations)), " cells/mL \n")
```

If you compile this script successfully you should see the following output in your terminal:

```
Counting number of viable cells in each image ... Done! 
 Mean cell concentration:  1.96e+05  cells/mL
 Standard deviation: 2.56e+04  cells/mL
```

I'd be quite interested to see what a histogram looks like for our cell concentrations (wouldn't you?). We can append the following code to our script to achieve this:

```
# count_zip. R script file
...

# Plot a histogram of cell concentrations
hist(
    cell_concentrations,
    breaks = 20,
    col = "lightblue",
    main = "",
    xlab = "Cell concentration (cells/mL)"
    )
```
And here's the result ...

![hemo_hist.png](hemo-hist.png)

**Figure 1:** Histogram showing the distribution of red cell concentrations in 100 patients.

I wonder if that distribution is normal. Let's perform a [Shapiro-Wilks](/glossary.md#shapiro.test) test:

```
# count_zip. R script file
...

# Perform a Shapiro-Wilks test.
# If p < 0.5 then reject null hypothesis that data is normally distributed.
print(shapiro.test(cell_concentrations))
```

Here's the output:

```
        Shapiro-Wilk normality test

data:  cell_concentrations
W = 0.98815, p-value = 0.5195
```

# Part 4









