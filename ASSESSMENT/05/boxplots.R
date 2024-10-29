# Load the data
data <- read.csv("compost_999999999.csv")

# Calculate the conversion factor
factor <- 2e5 / 1e7

# Calculate cfu per gram
data$cfu_per_g <- data$Viable.counts * factor

# Adjust the margins to prevent y-axis label from being cut off
par(mar = c(5, 5, 4, 2))  # Increase the second value for left margin

# Generate a grouped boxplot for Viable counts across different Locations
boxplot(cfu_per_g ~ Location, 
        data = data, 
        main = "", 
        xlab = "Location", 
        ylab = expression(cfu.g^{-1} ~ (x ~ 10^7)),
        col = "lightblue", 
        border = "black",
        cex.axis = 0.8)

text(x = 2.8, 
     y = max(data$cfu_per_g) * 0.9,  # Position the watermark below the maximum value
     labels = "Example", 
     col = rgb(0.5, 0.5, 0.5, alpha = 0.3),  # Slightly lighter for subtlety
     cex = 3, 
     srt = 30)  # Adjusted angle for better fit



