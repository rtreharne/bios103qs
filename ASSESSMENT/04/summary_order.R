# Read the CSV and filter out invalid rows
data <- read.csv("pantheria_999.csv")
data_filtered <- data[data$NeonateBodyMass_g != -999, ]

# Calculate summary statistics for each Family using tapply
summary_table <- data.frame(
  Mean = tapply(data_filtered$NeonateBodyMass_g, data_filtered$Family, mean, na.rm = TRUE),
  Median = tapply(data_filtered$NeonateBodyMass_g, data_filtered$Family, median, na.rm = TRUE),
  Max = tapply(data_filtered$NeonateBodyMass_g, data_filtered$Family, max, na.rm = TRUE),
  Min = tapply(data_filtered$NeonateBodyMass_g, data_filtered$Family, min, na.rm = TRUE),
  SD = tapply(data_filtered$NeonateBodyMass_g, data_filtered$Family, sd, na.rm = TRUE),
  Count = tapply(data_filtered$NeonateBodyMass_g, data_filtered$Family, function(x) length(x[!is.na(x)]))
)

# Format all numeric values to 1 decimal place (except Count)
summary_table[, 1:6] <- round(summary_table[, 1:6], 1)

# Sort by Count in decreasing order
summary_table <- summary_table[order(-summary_table$Count), ]

# Write to CSV and print
write.csv(summary_table, "summary_table.csv", row.names = FALSE)
print(summary_table)
