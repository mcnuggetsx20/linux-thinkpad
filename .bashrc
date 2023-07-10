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

alias qconf='nv ~/.config/qtile/config.py'
alias l='exa --group-directories-first --icons -lagBh'
alias pacinstall='sudo pacman -S'
alias pacclear='sudo pacman -Scc'
alias pacremove='sudo pacman -Rns'
alias pacupgrade='sudo pacman -Syyu; sudo pacman -Scc'
alias pacrefresh='sudo pacman -Syy'
alias oi='cd ~/documents/programming/oi_2021/'
alias term='vim ~/.config/alacritty/alacritty.yml'
alias calc='python ~/Documents/stuff/calculator.py'
alias pb='python -B'
alias cd='nvim_autocd'
#alias nv='internal_nvim'
alias take='_take'
alias ogmake='cd /home/minecraft; sudo java -Xmx4096M -Xms4096M -jar server.jar -nogui'

bind "set completion-ignore-case on"

function evim (){
    urxvt -e vim $1 &
}

function initx (){
    cat ~/wms/$1 > ~/.xinitrc
    startx
}
nvim_autocd(){
    builtin cd "$@"
    if [ -v NVIM ]; then
        (nvim_client_python -cd &) > /dev/null
    fi
}

nv(){
    if [ -v NVIM ]; then
        (nvim_client_python -p $@ &) > /dev/null
    fi
}

_take(){
    mkdir "$@"
    cd "$@"
}

openLid(){
    systemd-inhibit --what=handle-lid-switch sleep 2592000
}

niezle(){
    echo nvim_client_python -p \"$@\"
}


# The next line updates PATH for the Google Cloud SDK.
if [ -f '/home/mcnuggetsx20/program-files/google-cloud-sdk/path.bash.inc' ]; then . '/home/mcnuggetsx20/program-files/google-cloud-sdk/path.bash.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/home/mcnuggetsx20/program-files/google-cloud-sdk/completion.bash.inc' ]; then . '/home/mcnuggetsx20/program-files/google-cloud-sdk/completion.bash.inc'; fi
