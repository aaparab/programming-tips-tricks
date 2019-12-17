##############################
#  General bash tips
##############################

# See (sorted) size of all files 
# Reference: https://askubuntu.com/a/363681

du -sch .[!.]* * |sort -h

# Perform a command repeatedly
# Reference: https://www.tecmint.com/run-repeat-linux-command-every-x-seconds/

watch --difference --interval 5 nvidia-smi
watch script.sh
