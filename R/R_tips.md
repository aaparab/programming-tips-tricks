## General purpose R tips
---

#### Install R kernel for Jupyter
```
conda create --name r_env r-essentials jupyterlab
```

#### The pain in the nec that is R
- Why is `stringsAsFactors` not `FALSE` by default?
```
read.csv("file.csv", stringsAsFactors = FALSE)
```

#### Write to file
file.create('foo.txt')
fileconn <- file('foo.txt', 'w')
a <- runif(10)
writeLines(as.character(a), fileconn)
close(fileconn)

#### Write and install R packages

- To make package:
```
package.skeleton(name = "mypkg"
		, code_files = "/path/to/R/code/files")
```

- To install above package:
```
install.packages("devtools")
devtools::install("/path/to/mypkg")
```

- To create single bundled file from package:
```
devtools::build()
```

- To load package:
```
library(mypkg)
```
