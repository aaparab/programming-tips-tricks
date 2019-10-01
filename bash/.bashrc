# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific aliases and functions
export JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")

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

# Some Git Aliases
alias gs='git status'
alias ga='git add'
alias gaa='git add -A'
alias ggraph='git log --graph --decorate --oneline --all'

conda activate basenv
