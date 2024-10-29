data <- read.csv("pantheria_999.csv")

colnames(data)

slice <- data[, c("Order", "AdultBodyMass_g", "BasalMetRate_mLO2hr")]

subset <- slice[slice$AdultBodyMass_g >=0 & slice$BasalMetRate_mLO2hr >=0, ]

plot(subset$AdultBodyMass_g, subset$BasalMetRate_mLO2hr,
     log="xy",
     xlab = "Adult Body Mass (g)", 
     ylab = "Basal Metabolic Rate (mLO2/hr)",
     main = "")

# Create a color palette for different Orders
colors <- rainbow(length(unique(subset$Order)))

# Create a plot
plot(subset$AdultBodyMass_g, subset$BasalMetRate_mLO2hr,
     log = "xy",
     xlab = "Adult Body Mass (g)", 
     ylab = "Basal Metabolic Rate (mLO2/hr)",
     main = "",
     pch = 19,  # Point type
     col = colors[as.numeric(factor(subset$Order))]  # Color by Order
)
