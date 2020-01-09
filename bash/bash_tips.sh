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



# Change system timezone without SUDO access
# (for instance, remote server, cloud).
# Reference: https://superuser.com/a/856673

# vi .bashrc
export TZ="/usr/share/zoneinfo/{TIMEZONE-DIRECTORY}/{TIMEZONE_FILE}"


