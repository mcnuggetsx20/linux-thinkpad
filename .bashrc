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
alias pacclear='echo y | sudo pacman -Scc; sudo pacman -Scc --noconfirm'
alias pacremove='sudo pacman -Rns'
alias pacupgrade='configpush; sudo pacman -Syyu --noconfirm; sudo pacman -Scc --noconfirm; echo y | sudo pacman -Scc; echo; speed'
alias pacrefresh='sudo pacman -Syy'
alias oi='cd ~/documents/programming/oi_2021/'
alias term='vim ~/.config/alacritty/alacritty.yml'
alias calc='python ~/Documents/stuff/calculator.py'
alias pb='python -B'
alias cd='nvim_autocd'
#alias nv='internal_nvim'
alias take='_take'
alias ogmake='cd /home/minecraft; sudo java -Xmx4096M -Xms4096M -jar server.jar -nogui'
alias telewizor='xrandr --newmode "1360x768_60.00"   84.75  1366 1431 1567 1776  768 771 781 798 -hsync +vsync; xrandr --addmode VGA1 1360x768_60.00; xrandr --output VGA1 --mode 1360x768_60.00'
alias praca='xrandr --newmode "1920x1080_60.00"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync; xrandr --addmode DP1 1920x1080_60.00; xrandr --output DP1 --mode 1920x1080_60.00'
alias screenoff='sudo vbetool dpms off'
alias screenon='sudo vbetool dpms on'
alias speed='xset r rate 200 90'
alias battery='cat /sys/class/power_supply/BAT0/capacity'

bind "set completion-ignore-case on"

function gitpush(){
    DATE=$(date "+%d %b %Y %H:%M:%S")
    git add -A
    git commit -m "${DATE}"
    git push
}

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

aur(){
    cd /home/mcnuggetsx20/program-files/
    rm -rf $1
    git clone https://aur.archlinux.org/$1.git
    cd $1
    makepkg -si
}


# The next line updates PATH for the Google Cloud SDK.
if [ -f '/home/mcnuggetsx20/program-files/google-cloud-sdk/path.bash.inc' ]; then . '/home/mcnuggetsx20/program-files/google-cloud-sdk/path.bash.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/home/mcnuggetsx20/program-files/google-cloud-sdk/completion.bash.inc' ]; then . '/home/mcnuggetsx20/program-files/google-cloud-sdk/completion.bash.inc'; fi
