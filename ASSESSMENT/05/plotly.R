library(plotly)

# Load the data
data <- read.csv("compost_999999999.csv")

# Calculate the conversion factor for cfu per gram
factor <- 2e5 / 1e7
data$cfu_per_g <- data$Viable.counts * factor

# Create an interactive 3D scatterplot
fig <- plot_ly(data = data, 
               x = ~Temperature, 
               y = ~Moisture,
               z = ~cfu_per_g, 

               color = ~Location,
               colors = "Set2",  # Choose a color palette
               type = 'scatter3d',
               mode = 'markers',
               marker = list(size = 5)) %>%
  layout(scene = list(xaxis = list(title = 'Temperature (°C)'),
                      zaxis = list(title = 'VBC'),
                      yaxis = list(title = 'Moisture (%)')))

# Show the figure
fig
