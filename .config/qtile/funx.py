from subprocess import check_output, Popen, run

def space_check():
    return ' ' + check_output("df -h | grep sda2 | awk '{print $3}'", shell=True, encoding='utf-8')[:-1] + ' '

def remtext(text):
    return ''

def vol1():
    com = check_output('pulsemixer --get-volume', shell=True, encoding='utf-8').split()
    #   =====|----
    return com[0]

def volumechange(ok):
    def a(qtile):
        val = -5 + 10 * int(ok)
        run('pulsemixer --change-volume ' + str(val), shell=True) #change
        a = vol1()
        qtile.widgets_map['volumebox1'].update(' ' + a + '% ')
    return a

def volumemute(qtile):
    mt = check_output('pulsemixer --get-mute', shell=True, encoding='utf-8')[:-1]
    Popen('pulsemixer --toggle-mute', shell=True)
    if mt=='0':
        qtile.widgets_map['volumebox1'].update(' M ')
        return
    a=vol1()
    qtile.widgets_map['volumebox1'].update(' ' + a + '% ')


