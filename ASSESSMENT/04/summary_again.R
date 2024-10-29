#!/usr/bin/env Rscript

# Read the CSV file
data <- read.csv("pantheria_200.csv")

# Get numeric columns
numeric_columns <- sapply(data, is.numeric)
numeric_data <- data[, numeric_columns]

# Display a numbered list of numeric columns
cat("Select a variable to summarize:\n")
for (i in seq_along(colnames(numeric_data))) {
  cat(i, ":", colnames(numeric_data)[i], "\n")
}

# Ask for user input
selection <- as.numeric(readline(prompt = "Enter the number corresponding to the column: "))

# Ensure valid input
if (selection > 0 && selection <= length(numeric_data)) {
  selected_column <- colnames(numeric_data)[selection]
  
  # Filter out invalid values from the selected column
  valid_data <- data[data[[selected_column]] != -999, ]
  
  # Calculate summary statistics for the selected column
  summary_table <- aggregate(valid_data[[selected_column]] ~ Order, valid_data, function(x) 
    c(Mean = mean(x, na.rm = TRUE), 
      Median = median(x, na.rm = TRUE), 
      Max = max(x, na.rm = TRUE), 
      Min = min(x, na.rm = TRUE), 
      `Std. Dev.` = sd(x, na.rm = TRUE), 
      Count = length(x)))
  
  # Convert the list columns to individual columns
  summary_table <- do.call(data.frame, summary_table)
  
  # Rename the columns
  colnames(summary_table) <- c("Order", "Mean", "Median", "Max", "Min", "Std. Dev.", "Count")
  
  # Format all numeric values to 1 decimal place (except Count)
  summary_table[, 2:6] <- round(summary_table[, 2:6], 1)
  
  # Sort by Count in decreasing order
  summary_table <- summary_table[order(-summary_table$Count), ]
  
  # Write to CSV and print
  write.csv(summary_table, "summary_table.csv", row.names = FALSE)
  print(summary_table)
  
}
