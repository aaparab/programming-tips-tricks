## Plotting in R
# 1. Multiple plots 
# 2. Two ways of saving a file

# fake data:
library('data.table')
set.seed(8)
hist <- rbinom(1000, size = 50, prob = 0.1)
sqdt <- data.table(x = 1:10, y = (1:10)^2)

# Method 1: Save an image which will be generated in future. 

png(
    # https://stackoverflow.com/a/8400798
    'example01.png'
    , width = 15
    , height = 6
    , units = 'in'    # (default px) or in, cm, mm
    , res = 400
)

options(repr.plot.width = 12, repr.plot.height = 6)
layout(matrix(c(1, 2), nrow = 1, ncol = 2, byrow = TRUE))
hist(
    x = hist
    , breaks = 10
    , ylim = c(0, 200)
    , density = 10     # density of lines
    , col = 'red'
    , border = 'blue'
    , main = 'Very basic histogram'
    , xlab = 'X axis'
)
plot(
    sqdt
    , main = 'Squares'
    , type = 'o'
    , xlab = 'X-axis'
    , ylab = 'Frequency'
    , ylim = c(0, 120)
    , col = 'green'
)

# save plot: https://stackoverflow.com/a/7144203
dev.off()

graphics.off()    # something like reset graphics

# Method 2: Plot exists on screen and copy to disk

options(repr.plot.width = 12, repr.plot.height = 6)
layout(matrix(c(1, 2), nrow = 1, ncol = 2, byrow = TRUE))
hist(
    x = hist
    , breaks = 10
    , ylim = c(0, 200)
    , density = 10     # density of lines
    , col = 'red'
    , border = 'blue'
    , main = 'Very basic histogram'
    , xlab = 'X axis'
)
plot(
    sqdt
    , main = 'Squares'
    , type = 'o'
    , xlab = 'X-axis'
    , ylab = 'Frequency'
    , ylim = c(0, 120)
)

# save plot: https://stackoverflow.com/a/7144203
dev.copy(
    png
    , filename = 'example02.png'
    , width = 15    # ... : arguments to `png` function
    , height = 6
    , units = 'in'    # (default px) or in, cm, mm
    , res = 400
)
dev.off()    # This actually saves and closes the png file. 
