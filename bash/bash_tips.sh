##############################
#  General bash tips
##############################

# See (sorted) size of all files 
# Reference: https://askubuntu.com/a/363681

du -sch .[!.]* * |sort -h


# Read input from the user and perform actions

read -n1 -rep "Starting conda environments. Press
(0) or (p) for Python,
(1) or (r) for R: " inp
case $inp in
        0|p|P) conda activate basenv ;;
        1|r|R) conda activate renv ;;
        *) conda deactivate ;;
esac


# Perform a command repeatedly
# Reference: https://www.tecmint.com/run-repeat-linux-command-every-x-seconds/

watch --difference --interval 5 nvidia-smi
watch script.sh

# Follow the end of file as it is being written

tail --follow <filepath>

# Change system timezone without SUDO access
# (for instance, remote server, cloud).
# Reference: https://superuser.com/a/856673

# vi .bashrc
export TZ="/usr/share/zoneinfo/{TIMEZONE-DIRECTORY}/{TIMEZONE_FILE}"


