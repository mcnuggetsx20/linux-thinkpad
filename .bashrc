#
# ~/.bashrc
#

# If not running interactively, don't do anything
GREEN="\[$(tput setaf 2)\]"
RESET="\[$(tput sgr0)\]"
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
#the first one is the default, the second one shows the whole directory
PS1="[\W]${GREEN}$ ${RESET}"
#PS1='[\u@\h \w]$ '

#set -o vi

alias qconf='nvim ~/.config/qtile/config.py'
alias l='ls -lah'
alias pacinstall='sudo pacman -S'
alias pacclear='sudo pacman -Scc'
alias pacremove='sudo pacman -Rns'
alias pacupgrade='sudo pacman -Syyu'
alias pacrefresh='sudo pacman -Syy'
alias oi='cd ~/documents/programming/oi_2021/'
alias term='vim ~/.config/alacritty/alacritty.yml'
alias calc='python ~/documents/stuff/calculator.py'
alias pb='python -B'
alias cd='nvim_autocd'
alias nv='internal_nvim'

bind "set completion-ignore-case on"

function evim (){
    urxvt -e vim $1 &
}

function initx (){
    cat ~/wms/$1 > ~/.xinitrc
    startx
}

nvim_autocd(){
    builtin cd $1 
    if [ -v NVIM_LISTEN_ADDRESS ]; then
        (nvim_client_python -c &) > /dev/null
    fi
}

internal_nvim(){
    if [ -v NVIM_LISTEN_ADDRESS ]; then
        (nvim_client_python -tn $1 &) > /dev/null
    fi
}
