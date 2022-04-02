from libqtile import bar, layout, widget
from libqtile import hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from subprocess import check_output, Popen
from funx import *
from lib import *

@hook.subscribe.client_new
def func(new_window):
    if new_window.name=='QPanel':
        new_window.cmd_static(screen=0)

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
dgray  = '#312D2D'
gray   = '#D0D0D0'
red    = '#C61717'
dred   = '#6b1015'
solar  = '#fdf6e3'   

mod = "mod1"
sup = "mod4"
terminal = "alacritty"

keys = [
    #My stuff
    Key([sup], 'b', lazy.spawn('brave')),
    Key([mod], 'p', lazy.spawn('dmenu_run')),
    Key([sup], 'f', lazy.spawn('pcmanfm')),
    Key([sup], 'm', lazy.spawn('urxvt -e htop')),
    Key([sup], 't', lazy.spawn('sh qpanel')),
    Key([sup], 'k', lazy.spawn('pkill -f qpanel')),
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
    layout.MonadTall(border_focus='#F0AF16', new_client_position='before_current', change_ratio=0.025),
    layout.Max(border_width=0, border_focus='#000000', margin=8),
]

float_layout = layout.Floating(
    border_width=0,
    border_focus='#000000',
    float_rules=[
        Match(title='QNetwork'),
        Match(wm_class = 'feh'),
        Match(wm_class = 'python -B main.py'),
    ]
)

groups = [
        Group('1', layouts=all_layouts),
        Group('2', layouts=all_layouts),
        Group('3', layouts=all_layouts),
        Group('4', layouts=all_layouts),
        Group('5', layouts=[float_layout]),
        ]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])


widget_defaults = dict(
    font='Fixedsys', 
    fontsize=14,
    padding=0,
    #foreground='#000000',
    #background=,
    inactive='#FFFFFF',
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper='~/Pictures/wallpaper/orange_comma.jpg',
        wallpaper_mode='fill',
        top=bar.Bar(widgets=[
            widget.Clock(
                foreground=black,
                background=violet,
                format=" %A ",
            ),

            widget.Clock(
                foreground=black, 
                background=orange,
                format=" %d.%m.'%y ",
            ),

            widget.Clock(
                foreground=black,
                background=dblue,
                format=" %H:%M:%S ",
                update_interval=1,
            ),

            widget.TextBox(
                text=' ',
                foreground=black,
                background=white,
            ),

            widget.CurrentLayout(
                foreground=black,
                background=white,
            ),


            widget.TextBox(
                text=' ',
                foreground=black,
                background=white,
            ),

            widget.Spacer(
                length=3,
            ),

            widget.TaskList(
                parse_text=remtext, 
                borderwidth=0, 
                margin_x=0, 
                margin_y=0, 
                icon_size=18, 
                txt_floating=''
            ),

            widget.Spacer(
                length=bar.STRETCH,
            ),

            widget.Systray(),

            widget.GenPollText(
                foreground=black,
                background=white,
                func=space_check, 
                update_interval=4,
            ),

            widget.CPU(
                foreground=black, 
                background=violet, 
                format=' CPU {load_percent}% ', 
                update_interval=2.0,
            ),

            widget.TextBox(
                name='volumebox1',
                text=' ' + vol1() + '% ',
                foreground=black,
                background=ored,
            ),

            widget.Battery(
                foreground=black, 
                background=lime,
                format=' {char}{percent:2.0%} {hour:d}:{min:02d} ', 
                charge_char='',
                discharge_char='',
                update_interval=2
            ),

            widget.GroupBox(
                active=black,
                inactive=black,
                #foreground=black,
                background=orange,
                this_current_screen_border=orange,
                this_screen_border=orange,
                highlight_method='block',
                block_highlight_text_color=white,

            ),

            widget.Image(
                background=orange, 
                filename = '/home/mcnuggetsx20/.config/qtile/arch_black.png',
            ),
            

        ],
        size=18)
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
