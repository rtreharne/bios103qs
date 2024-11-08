activity_data <- read.csv("https://raw.githubusercontent.com/rtreharne/qs/main/data/08/activity_295.csv")

activity_data$activity <- as.numeric(activity_data$activity) 
activity_data <- na.omit(activity_data)


activity_data <- activity_data[activity_data$activity >= 0,]

activity_data$ph <- as.factor(activity_data$ph)
activity_data$temperature <- as.factor(activity_data$temperature)



# anova_result
anova_result <- aov(activity ~ ph * temperature, data = activity_data)

summary(anova_result)


# Perform Tukey's HSD test
tukey_result <- TukeyHSD(anova_result)

tukey_df <- as.data.frame(tukey_result[["ph:temperature"]])

tukey_df$diff <- abs(tukey_df$diff)

max(tukey_df$diff)

# Count rows where "p adj" (adjusted p-value) is less than 0.05
count_reject_true <- sum(tukey_df$`p adj` < 0.05)

# Calculate percentage of significant comparisons and round to 1 decimal place
percentage_significant <- round(count_reject_true * 100 / nrow(tukey_df), 1)

# Display the result
print(paste("Percentage of significant pairwise comparisons:", percentage_significant))

# View the results
print(tukey_result)

head(activity_data)

boxplot(activity ~ ph, data=activity_data)
boxplot(activity ~ temperature, data=activity_data)

# anova_result
anova_result <- aov(activity ~ ph * temperature, data = activity_data)

summary(anova_result)



tukey_result <- TukeyHSD(anova_result)


# View the results
print(tukey_result)

plot(tukey_result)

# Interaction plot of pH and Temperature on enzyme activity
interaction.plot(activity_data$temperature, activity_data$ph, activity_data$activity,
                 col = c("red", "green", "blue"), lwd = 2,
                 
                 xlab = "Temperature (°C)", ylab = "Catalase Activity (ΔA/min)",
                 legend = TRUE)

# Boxplot grouped by pH and Temperature
boxplot(activity ~ ph, data = filtered,
        xlab = "pH", ylab = "Catalase Activity (ΔA/min)",
        main = "Catalase Activity by pH and Temperature")

# Reshape the data for heatmap visualization
library(reshape2)
matrix <- acast(activity_data, ph ~ temperature, value.var = "activity", mean)

# Create a blue-red color palette
color_palette <- colorRampPalette(c("white", "red"))(256)

# Create heatmap with blue-red colors and color key
heatmap(matrix, Rowv = NA, Colv = NA, scale = "none", 
        col = color_palette,  # Use the blue-red color palette
        xlab = "Temperature (°C)", 
        ylab = "pH", 

        margins = c(5, 5), # Adjust margins if needed
        

)  # Y-axis label for the color key (set to NULL to hide)

color_palette

res <- data.frame(tukey_result$`ph:temperature`)

sum(res$p.adj <= 0.05)

