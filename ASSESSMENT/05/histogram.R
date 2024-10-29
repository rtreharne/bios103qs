# Load the data
data <- read.csv("compost_999999999.csv")

# Calculate the conversion factor
factor <- 2e5 / 1e7

# Calculate cfu per gram
data$cfu_per_g <- data$Viable.counts * factor

# Calculate the mean of cfu_per_g
mean_cfu_per_g <- mean(data$cfu_per_g, na.rm = TRUE)

# Generate a simple histogram for all "Viable counts"
hist(data$cfu_per_g,
     breaks = 20,
     main = "", 
     xlab = expression(cfu ~ g^{-1} ~ (x ~ 10^7)), 
     ylab = "Frequency",
     col = "lightblue",
     border = "black")

# Add a vertical line for the mean
abline(v = mean_cfu_per_g, col = "red", lwd = 2, lty = 2)


# Add a watermark
text(x = 2.8, 
     y = 20, 
     labels = "Example", 
     col = rgb(0.5, 0.5, 0.5, alpha = 0.5), 
     cex = 3, 
     srt = 45)

box()




