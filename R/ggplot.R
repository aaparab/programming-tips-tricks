# Plotting bars:

library('data.table')
library('ggplot2')
library('magrittr')

# helper function to flatten dataset:
flatten <- function(dt, cols_to_flatten, cols_to_repeat, names = c('V1', 'V2')) {
    newdt <- data.table()
    for (col in cols_to_flatten) {
        tmp <- data.table(dt[, c(cols_to_repeat, col), with = FALSE])
        setnames(tmp, col, names[1])
        tmp[, names[2] := col]
        newdt <- rbind(newdt, tmp)
    }
    return (newdt)
}

# generate fake data:
set.seed(8)
x <- 1:8 + 2*runif(8)
y <- 1:8 + rnorm(8)
dt <- data.table(id = 1:8, old = x, new = y)
dt <- flatten(dt, c('old', 'new'), c('id'), c('value', 'level'))
dt %>% head()

ggplot(data = dt, aes(x = id, y = value, fill = level)) + 
    geom_bar(position = 'dodge', stat = 'identity') +
    ggsave('bars.png')
