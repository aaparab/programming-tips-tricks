# .bashrc

# Source global definitions
# Bash prompt becomes [user@machine ~]$
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
export JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")
## Add CUDA to system path
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/msabp/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/msabp/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/home/msabp/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/msabp/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

PATH=$PATH:$HOME/bin
export PATH

##############################
# Code for colored prompt
##############################

# Supporting Definitions ####
source "$HOME/.bash/term_colors"
# get from https://raw.github.com/git/git/master/contrib/completion/git-prompt.sh
source $HOME/.bash/git-prompt.sh

# Variables ####
export LS_COLOR='--color=tty'
export EDITOR=$( which vi )
PROMPT_COLOR=$G
if [ ${UID} -eq 0 ]; then
  PROMPT_COLOR=$R ### root is a red color prompt
fi
# Setting PS1
# (1) The time shows when each command was executed, when I get back to my terminal
# (2) Git information really important for git users
# (3) Prompt color is red if I'm root
# (4) The last part of the prompt can copy/paste directly into an SCP command
# (5) Color highlight out the current directory because it's important
# (6) The export PS1 is simple to understand!
# (7) If the prev command error codes, the prompt '>' turns red
CURSOR_PROMPT="$ "
export PS1="$Y\t$N $W"'$(__git_ps1 "(%s) ")'"$N$PROMPT_COLOR\u@\H$N:$C\w$N\n"'$CURSOR_PROMPT '
##############################
# End code for colored prompt
##############################

# Abhishek customizations
conda activate basenv

# Some Git Aliases
alias s='git status'
alias a='git add'
alias aa='git add -A'
alias graph='git log --graph --decorate --oneline --all'


