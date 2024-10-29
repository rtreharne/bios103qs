data <- read.csv("compost_999999999.csv")

# Calculate summary statistics for Temperature, Moisture, and Viable counts for each Location
summary_table <- aggregate(cbind(Temperature, Moisture, Viable.counts) ~ Location, 
                           data, 
                           function(x) c(Mean = mean(x), SD = sd(x)))

# Convert the list columns to individual columns
summary_table <- do.call(data.frame, summary_table)

# Multiply Viable Counts Mean and SD columns by factor to convert to units of cfu/g
factor <- 2e5 / 1e7

summary_table$Viable.counts.Mean <- summary_table$Viable.counts.Mean * factor
summary_table$Viable.counts.SD <- summary_table$Viable.counts.SD * factor

write.csv(summary_table, "mushroom_summary.csv", row.names = FALSE)
