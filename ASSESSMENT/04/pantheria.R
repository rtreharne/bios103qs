# read file to dataframe

setwd("C:/Users/treharne/Documents/bios103qs/ASSESSMENT/04")

data <- read.csv("pantheria_127.csv")

family_counts <- sort(table(data$Family), decreasing = TRUE)

df <- data.frame(head(family_counts, 10))

names(df) <- c("Family", "Count")

#write.csv(df, "pantheria_top10.csv", row.names = FALSE)

names(data)

