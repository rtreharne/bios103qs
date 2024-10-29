# Read data
data <- read.csv("compost_999999999.csv")

factor <- 2e5 / 1e7

library(dplyr)

summary_stats <- summarise(
  group_by(data, Location),
  mean_temp = mean(Temperature),
  sd_temp = sd(Temperature),
  mean_moisture = mean(Moisture),
  sd_moisture = sd(Moisture),
  mean_vbc = mean(Viable.counts, na.rm=TRUE)*factor,
  sd_vbc = sd(Viable.counts, na.rm=TRUE)*factor
)

print(summary_stats)

write.csv(summary_stats, file="summary_stats.csv", row.names=FALSE)
