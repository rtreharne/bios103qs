data <- read.csv("pantheria_999.csv")

orders <- table(data$Order)

most_common_order <- names(which.max(orders))

print(most_common_order)

