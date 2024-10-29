setwd("C:/Users/treharne/Documents/bios103qs/ASSESSMENT/05")

# Load the data
data <- read.csv("compost_999999999.csv")


# Plot a histogram of "Viable counts"
hist(data$Viable.counts, main="Histogram of Viable counts", xlab="Viable counts", ylab="Frequency")

# Add a vertical lines at the mean and median
abline(v=mean(data$Viable.counts), col="red")
abline(v=median(data$Viable.counts), col="blue")

# add a Legend. Quote values to avoid scientific notation
legend("topright", legend=c(paste("Mean =", format(mean(data$Viable.counts), scientific=FALSE)),
                           paste("Median =", format(median(data$Viable.counts), scientific=FALSE))),
       col=c("red", "blue"), lty=1, cex=0.8)

# create a grouped boxplot of "viable counts" by "location"
boxplot(Viable.counts ~ Location, data=data, main="Boxplot of Viable counts by Location", xlab="Location", ylab="Viable counts")

# Map Location values to colors with transparency
location_colors <- as.numeric(factor(data$Location))
color_palette <- rainbow(length(unique(data$Location)))
transparent_colors <- sapply(color_palette, function(col) rgb(t(col2rgb(col)), maxColorValue=255, alpha=100))

# scatter plot of "Viable counts" by "Temperature". color by "Location"
plot(
  data$Temperature, 
  data$Viable.counts, 
  col=transparent_colors[location_colors], 
  pch=19, 
  main="",
  xlab="Temperature (deg C)", 
  ylab="Viable Counts",
  #ylim=c(100, 150),
  #xlim=c(50, 80)
  )

# Add a legend for the locations
legend("topright", legend=levels(factor(data$Location)), col=transparent_colors, pch=19, cex=0.8)

# Load the plotly library
library(plotly)

# Create a 3D scatter plot
fig <- plot_ly(data, x = ~Temperature, y = ~Moisture, z = ~Viable.counts, color = ~Location, colors = rainbow(length(unique(data$Location))), type = 'scatter3d', mode = 'markers', marker = list(size = 5, opacity = 0.7))

# Add titles and labels
fig <- fig %>% layout(title = "3D Scatter Plot of Temperature, Moisture, and Viable Counts",
                      scene = list(xaxis = list(title = 'Temperature'),
                                   yaxis = list(title = 'Moisture'),
                                   zaxis = list(title = 'Viable Counts')))

# Show the plot
fig

