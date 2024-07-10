
# create a list of 100 sequential integers in the range 100-200
seeds <- seq(100, 300)

# create a corresponding list of randum numbers using the seeds
random_numbers <- lapply(seeds, function(x) {
  set.seed(x)
  runif(1)
})

# combine seeds and random_numbers into a data frame
random_numbers <- data.frame(seed = seeds, random_number = unlist(random_numbers))


# set current working directory as the directory where the script is located
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))


# save the file as a .csv file in the current working directory (i.e. the same directory as the script)


write.csv(random_numbers, "random_numbers.csv", row.names = FALSE)