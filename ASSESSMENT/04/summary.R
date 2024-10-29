# script name: summary.R

# Read the CSV and filter out invalid rows
data <- read.csv("pantheria_999.csv")
data_filtered <- data[data$NeonateBodyMass_g != -999, ]

# Calculate summary statistics for each Family
summary_table <- aggregate(AdultBodyMass_g ~ Family, data_filtered, function(x) 
  c(Mean = mean(x), Median = median(x), Max = max(x), Min = min(x), SD = sd(x), Count = length(x)))

# Convert the list columns to individual columns
summary_table <- do.call(data.frame, summary_table)

# Rename the columns
colnames(summary_table) <- c("Order", "Mean", "Median", "Max", "Min", "Std. Dev.", "Count")

# Format all numeric values to 1 decimal place (except Count)
summary_table[, 2:6] <- round(summary_table[, 2:6], 1)

# Sort by Count in decreasing order and return top 10 most frequently occurring families in data
summary_table <- summary_table[order(-summary_table$Count), ][1:10, ]

# Sort top 10 by Mean
summary_table <- summary_table[order(-summary_table$Mean), ]

# Write to CSV and print
write.csv(summary_table, "summary_table.csv", row.names = FALSE)
print(summary_table)