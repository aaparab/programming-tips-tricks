# General purpose Python tips (not Jupyter)

########################################
# Measure program execution time
########################################
from time import time
start = time()
# Program code
end = time()
print("Time to execute: {} seconds.".format(end - start))

########################################
# Format printing large numbers
########################################
"{:_}".format(123456789)
# >> '123_456_789













