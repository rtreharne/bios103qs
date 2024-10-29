# Load the required library for color palette
#library(viridis)

# Load the data
data <- read.csv("compost_999999999.csv")

# Calculate the conversion factor for cfu per gram
factor <- 2e5 / 1e7
data$cfu_per_g <- data$Viable.counts * factor

# Define a color palette accessible for colorblind viewers
colors <- rainbow(length(unique(data$Location)), alpha = 0.6)

# Adjust the margins to prevent y-axis label from being cut off
par(mar = c(5, 5, 4, 2))  # Increase the second value for left margin

# Create a scatterplot of cfu vs. temperature, colored by location
plot(data$Temperature, data$cfu_per_g,
     main = "",
     xlab = "Temperature (°C)",
     ylab = expression(cfu.g^{-1} ~ (x ~ 10^7)),
     pch = 19,  # solid circles for points
     cex = 1.5,  # increase point size
     col = colors[as.numeric(factor(data$Location))])  # color by location with transparency

# Add faint gridlines
grid(col = "gray90", lty = "dotted")

# Add a legend without a border
legend("bottomleft", 
       legend = unique(data$Location), 
       col = colors, 
       pch = 19,  # same symbol as in the plot
       bty = "n",  # no box around the legend
       pt.cex = 1.5)  # match point size in legend


# Add a watermark
text(x = mean(range(data$Temperature)), 
     y = mean(range(data$cfu_per_g)), 
     labels = "Example", 
     col = rgb(0.5, 0.5, 0.5, alpha = 0.5), 
     cex = 3, 
     srt = 45)

