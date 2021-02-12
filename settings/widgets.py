from libqtile import widget
from settings.theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

base = lambda fg='light', bg='dark': {
    'foreground': colors[fg],
    'background': colors[bg]
}

separator = lambda: widget.Sep(**base(), linewidth=0, padding=5)

icon = lambda fg='text', bg='dark', fontsize=16, text="?": widget.TextBox(
    **base(fg, bg),
    fontsize=fontsize,
    text=text,
    padding=3
)

powerline = lambda fg="light", bg="dark": widget.TextBox(
   **base(fg, bg),
    text="", 
    fontsize=37,
    padding=-2
)

powerline2 = lambda fg="light", bg="dark": widget.TextBox(
   **base(fg, bg),
    text=" | ", 
    fontsize=25,
    padding=-2
)

#MOUSE CALLBACKS

def update_sys(qtile):
    qtile.cmd_spawn('alacritty -e sudo pacman -Syu')

def open_htop(qtile):
    qtile.cmd_spawn('alacritty -e htop')


workspaces = lambda: [
    separator(),
    widget.GroupBox(
        **base(fg='light'),
        font='UbuntuMono Nerd Font',
        fontsize=16,
        margin_y=3,
        margin_x=0,
        padding_y=8,
        padding_x=5,
        borderwidth=1,
        active=colors['active'],
        inactive=colors['inactive'],
        rounded=False,
        highlight_method='block',
        urgent_alert_method='block',
        urgent_border=colors['urgent'],
        this_current_screen_border=colors['focus'],
        this_screen_border=colors['grey'],
        other_current_screen_border=colors['dark'],
        other_screen_border=colors['dark'],
        disable_drag=True
    ),
    separator(),
    widget.WindowName(**base(bg='dark', fg='focus'), fontsize=12, padding=5),
    separator(),
]

primary_widgets = [

    *workspaces(),

    separator(),

    #powerline2('grey', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='dark', fg='color2'), scale=0.65),


    # widget.CurrentLayout(**base(bg='dark', fg='light'), padding=5),

    powerline2('grey', 'dark'),

    icon(bg="dark", fg="color4", text=' '), # Icon: nf-fa-download
    
    widget.Pacman(
        **base(fg='light'), 
        update_interval=1800,
        mouse_callbacks = {'Button1': update_sys}
    ),

    powerline2('grey', 'dark'),

    icon(bg="dark", fg="color5", text=' '),

    widget.Memory(
        **base(bg='dark', fg='light'),
        mouse_callbacks = {'Button1': open_htop}
    ),

    # icon(bg="dark", fg="color1", text=' '),

    # widget.CPU(
    #     **base(bg='dark', fg='light'),
    #     mouse_callbacks = {'Button1': open_htop}
    # ),

    powerline2('grey', 'dark'),

    icon(bg="dark", fg="color3", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='dark', fg='light'), format='%d/%m/%Y - %H:%M '),

    powerline2('grey', 'dark'),

    widget.Systray(background=colors['dark'], padding=5),

]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()


#"#ffb86c" color amarillo
#a3be8c verde
#81a1c1 celeste
