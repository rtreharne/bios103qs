# Load necessary library
#library(dplyr)

data <- read.csv("compost_999999999.csv")

factor = 2e5/1e7

# Assuming your data frame is named 'data'
summary_stats <- summarise(
  group_by(data, Location),
  Avg_Temperature = mean(Temperature, na.rm = TRUE),
  SD_Temperature = sd(Temperature, na.rm = TRUE),
  Avg_Moisture = mean(Moisture, na.rm = TRUE),
  SD_Moisture = sd(Moisture, na.rm = TRUE),
  Avg_Viable_Counts = mean(Viable.counts, na.rm = TRUE)*factor,
  SD_Viable_Counts = sd(Viable.counts, na.rm = TRUE)*factor
)

# View the summary statistics
print(summary_stats)

# Save the summary statistics to a CSV file
write.csv(summary_stats, file = "summary_statistics.csv", row.names = FALSE)


