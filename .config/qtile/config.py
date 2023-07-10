from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from subprocess import check_output, Popen, call
from funx import *
import os
from time import sleep

orange = '#F0Af16'
ored   = '#F77B53'
black  = '#000000'
swamp  = '#335D03'  
lime   = '#32CD32'
green  = '#A9DC76'
violet = '#C76BFA'
dviolet= '#7A05BE'
dblue  = '#3A69F0'
white  = '#FFFFFF'
dgray  = '#a5c2c5'
gray   = '#D0D0D0'
red    = '#C61717'
dred   = '#6b1015'
solar  = '#fdf6e3'   
gray_orange='#E6D69B'
light_orange = '#F0C674'
dimmed = '#707880'

mod = "mod1"
sup = "mod4"
terminal = "alacritty -e nvim -c term -c 'set ma' -c startinsert"
dmenu = "dmenu_run -sb '" + gray_orange + "' -nf '" + gray_orange + "' -sf '" + red + "'"
iconPath = '~/.config/qtile/icons/'

network_devices={
        'ethernet'  : 'I',
        'wireless'  : 'H',
        'None'      : 'J',
        }

target = [0, 0,0,0]

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    call([home + '/.config/qtile/autostart.sh'])

@hook.subscribe.client_new
def func(new_window):
    if new_window.name=='Straw':
        #Popen('echo essa > ~/temp', shell=True)
        new_window.cmd_toggle_floating()
    elif new_window.name=='QPanel':
        new_window.cmd_static(screen=0)

    elif new_window.name == 'weatherReport':
        new_window.cmd_toggle_floating()
        new_window.cmd_set_position(100, 100)

        new_window.cmd_static(screen=0)

    elif new_window.name == 'whiteout':
        new_window.cmd_toggle_floating()
        new_window.cmd_set_size_floating(1000,1000)
        new_window.cmd_static(screen=0)

    elif new_window.name == 'blacktest':
        target[0:2] = new_window.cmd_get_size()
        qtile.widgets_map['debug'].update(str(target))
        #Popen('~/Documents/kododawanie/projects/whiteout/whiteout', shell=True)


    #_id = str(new_window.info()['id'])
    #Popen('echo ' + str(a) + ' > ~/temp', shell=True)
    #Popen('getxicon -w ' + _id + ' ' + iconPath + _id, shell=True)

@hook.subscribe.client_killed
def killed(zombie):
    _id = str(zombie.info()['id'])
    Popen('rm ' + iconPath + _id + '*', shell=True)

def temp():
    a = check_output("curl -s wttr.in/Wojnów?format=1 | awk '{printf $2}'", shell=True, encoding='utf-8')
    return ['N/A', a][int(bool(len(a)))]

keys = [
    #My stuff
    Key([sup], 'b', lazy.spawn('brave')),
    Key([mod], 'p', lazy.spawn(dmenu)),
    Key([sup], 'f', lazy.spawn('pcmanfm')),
    Key([mod], 'e', lazy.to_screen(0)),
    Key([mod], 'w', lazy.to_screen(1)),   Key([sup], 'm', lazy.spawn('urxvt -e htop')),
    Key([sup], 'bracketleft', lazy.spawn('Straw')),

    Key([], 'XF86AudioRaiseVolume', lazy.function(volumechange(True))),
    Key([], 'XF86AudioLowerVolume', lazy.function(volumechange(False))),
    Key([], 'XF86AudioMute', lazy.function(volumemute)),
    Key([mod, 'shift'], 's', lazy.spawn('sh /usr/bin/screenshot')),
    Key([sup], 'q', lazy.spawn('sh power_menu')),
    Key([sup], 'p', lazy.spawn('feh /home/mcnuggetsx20/Pictures/plan_lekcji.png')),
    Key([mod, 'shift'], 's', lazy.spawn('sh /usr/bin/screenshot')),
    Key([],    'XF86MonBrightnessUp', lazy.spawn('xbacklight -inc 5')),
    Key([],    'XF86MonBrightnessDown', lazy.spawn('xbacklight -dec 5')), 
    Key([mod], 't', lazy.window.toggle_floating()),
    Key([sup], 'j', lazy.window.toggle_minimize()),
    Key([mod], 'Tab', lazy.spawn('rofi -show window')),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([sup], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([sup], "BackSpace", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
]

all_layouts = [
    layout.MonadTall(
        border_focus=violet, 
        single_border_width=0,
        new_client_position='before_current', 
        change_ratio=0.025,
        margin=12,
    ),

    layout.Max(
        border_width=0, 
        border_focus='#000000', 
        margin=8
    ),
]

float_layout = layout.Floating(
    border_width=0,
    border_focus='#000000',
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class = 'Straw'),
        Match(wm_class = 'feh'),
    ]
)

groups = [
    Group(
        name='1', 
        position=1, 
        layouts=all_layouts
    ),

    Group(
        name='2', 
        position=2, 
        layouts=all_layouts
    ),

    Group(
        name='3',
        position=3, 
        layouts=all_layouts
    ),

    Group(
        name='4',
        position=4, 
        layouts=all_layouts, 
        matches = [
            Match(wm_class='discord')
        ]
    ),
        
    Group(
        name='5', 
        position=5, 
        layouts=[float_layout], 
        matches = [
            Match(wm_class='teams')
        ]
    ),
]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], str(i.position), lazy.group[i.name].toscreen()),
        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], str(i.position), lazy.window.togroup(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

widget_defaults = dict(
    font='JetBrains Mono Bold', 
    fontsize=14,
    padding=0,
    #foreground=black,
    #background=gray_orange,
    inactive='#FFFFFF',
)
extension_defaults = widget_defaults.copy()

def network_current():
    st = check_output("nmcli -t connection show --active | awk -F ':' '{print $1 " + '"\\n"' + " $(NF-1)}'", shell=True, encoding='utf-8').split('\n')[:-1]
    st.append('None')
    st.append('None')

    current_net_dev = network_devices[st[1].split('-')[-1]]
    return current_net_dev

bar_background = '#282A2E'
bar_foreground = light_orange
screens = [
    Screen(
        wallpaper='~/Pictures/wallpaper/solar_comma_light.png',
        wallpaper_mode='fill',
        top=bar.Bar(
            background=bar_background,
            widgets=[
                widget.TextBox(
                    text='C',
                    font='Bartek',
                    fontsize=31,
                    foreground=gray_orange,
                ),

                widget.GroupBox(
                    font='JetBrains Mono',
                    active=gray,
                    inactive=dimmed,
                    background=bar_background,
                    foreground = bar_background,
                    this_current_screen_border=bar_foreground,
                    this_screen_border=green,
                    highlight_method='block',
                    block_highlight_text_color=bar_background,
                    highlight_color=bar_background,

                ),

                widget.TextBox(
                    text='A',
                    font='Bartek',
                    fontsize=31,
                    foreground=gray_orange,
                ),

                widget.TextBox(
                    text=' ',
                    font='JetBrains Mono',
                    foreground=black,
                    background = gray_orange,
                ),

                widget.GenPollText(
                    name='disk',
                    foreground=black,
                    background=gray_orange,
                    func=space_check, 
                    update_interval=4,
                ),

                widget.TextBox(
                    text='B',
                    font='Bartek',
                    fontsize=31,
                    foreground=gray_orange,
                ),


                widget.Spacer(
                    length=3,
                ),

                widget.TaskList(
                    #parse_text=remtext, 
                    parse_text = lambda text: ' ' + text + ' ',
                    borderwidth=0, 
                    margin_x=0, 
                    margin_y=0, 
                    icon_size=18, 
                    txt_floating='',
                    font='JetBrains Mono',
                    #background = dimmed,
                ),

                widget.Spacer(
                    length=45,
                ),
                widget.Prompt(
                    font = 'JetBrains Mono',
                ),

                widget.Systray(),
                widget.StatusNotifier(),

                widget.GenPollText(
                    func = network_current,
                    name = 'network_device1',
                    fontsize = 22,
                    font = 'Bartek',
                    background = bar_background,
                    foreground = gray,
                    interval = 2,
                    mouse_callbacks={'Button1' : lazy.spawn('Straw')},
                ),

                widget.Spacer(14),

                widget.TextBox(
                    text = ' ',
                    name = 'AudioDeviceIndicator1',
                    foreground = gray,
                    background = bar_background,
                    font='JetBrains Mono',
                ),

                widget.TextBox(
                    name = 'vol_level1',
                    text=vol1()[0],
                    foreground=bar_foreground,
                    background=bar_background,
                    font = 'Ubuntu Bold',
                    fontsize=12,
                ),

                widget.TextBox(
                    name = 'vol_rest1',
                    text=vol2(),
                    font = 'Ubuntu Bold',
                    fontsize=12,
                    func = vol2,
                    foreground=gray,
                    background=bar_background,
                ),

                widget.TextBox(
                    text='(',
                    foreground=bar_foreground,
                    background=bar_background,
                ),

                widget.TextBox(
                    name='vol_number1',
                    text = vol1()[1]+'%',
                    foreground=gray,
                    background=bar_background,
                ),

                widget.TextBox(
                    text=')',
                    foreground=bar_foreground,
                    background=bar_background,
                ),

                widget.Spacer(14),

                widget.TextBox(
                    text=' ',
                    font = 'JetBrains Mono',
                    foreground=bar_foreground,
                    background=bar_background,
                ),

                widget.Battery(
                    foreground=gray, 
                    background=bar_background,
                    format='{char}{percent:2.0%} {hour:d}:{min:02d}', 
                    charge_char='',
                    discharge_char='' ,
                    update_interval=2
                ),

                widget.Spacer(15),

                widget.TextBox(
                    text=' ',
                    font = 'JetBrains Mono',
                    foreground = gray,
                    background = bar_background,
                ),
                widget.GenPollText(
                    func = temp,
                    update_interval = 1000,
                    foreground = bar_foreground,
                    background = bar_background,
                ),

                widget.TextBox(
                    text = 'A',
                    font = 'Bartek',
                    fontsize= 31,
                    foreground = gray_orange,
                ),

                widget.TextBox(
                    text = ' ',
                    font = 'JetBrains Mono',
                    foreground = black,
                    background = gray_orange,
                ),

                widget.Clock(
                    foreground=black,
                    background=gray_orange,
                    format="%H:%M:%S",
                    update_interval=1,
                ),

                widget.TextBox(
                    text = 'BA',
                    font = 'Bartek',
                    fontsize= 31,
                    foreground = gray_orange,
                ),

                widget.TextBox(
                    text = ' ',
                    font = 'JetBrains Mono',
                    foreground = black,
                    background = gray_orange,
                ),

                widget.Clock(
                    foreground=black,
                    background=gray_orange,
                    format="%a: %d.%m.'%y",
                ),

                widget.TextBox(
                    text = 'B',
                    font = 'Bartek',
                    fontsize= 31,
                    foreground = gray_orange,
                ),

        ],
        size=18)
    ),
    Screen(
        wallpaper='~/Pictures/wallpaper/solar_comma_light.png',
        wallpaper_mode='fill',
        top=bar.Bar(
            background='#29271c',
            widgets=[
                widget.TextBox(
                    text='CA',
                    font='Bartek',
                    fontsize=31,
                    foreground=gray_orange,
                ),
                widget.GroupBox(
                    font='Roboto Mono',
                    active=black,
                    inactive=black,
                    background=gray_orange,
                    this_current_screen_border=black,
                    this_screen_border=green,
                    highlight_method='block',
                    block_highlight_text_color=gray_orange,
                ),

                widget.TextBox(
                    text='B',
                    font='Bartek',
                    fontsize=31,
                    foreground=gray_orange,
                ),
            ],
            size=18,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

wmname = "QTile"

