from subprocess import check_output, Popen, run

def space_check():
    return check_output("df -h | grep sda2 | awk '{print $3}'", shell=True, encoding='utf-8')[:-1]

def remtext(text):
    return ''

def volumemute(qtile):
    mt = check_output('pulsemixer --get-mute', shell=True, encoding='utf-8')[:-1]
    Popen('pulsemixer --toggle-mute', shell=True)
    if mt=='0':
        qtile.widgets_map['vol_number1'].update(' M ')
        return
    a=vol1()
    qtile.widgets_map['vol_number1'].update(' ' + a + '% ')

def vol1():
    com = check_output('pamixer --get-volume', shell=True, encoding='utf-8').split()
    #   =====|----
    seg1 = (int(com[0]) // 15) * 'I'
    return [seg1, com[0]]

def vol2():
    return ((10 - len(vol1()[0])) * 'I')[:-1]

def volumechange(ok):
    def a(qtile):
        if ok:
            val = 5
        else:
            val = -5

        run('pulsemixer --change-volume ' + str(val), shell=True) #change

        a = vol1()
        b = vol2()

        qtile.widgets_map['vol_level1'].update(a[0])
        qtile.widgets_map['vol_rest1'].update(b)
        qtile.widgets_map['vol_number1'].update(a[1]+'%')

        qtile.widgets_map['vol_level2'].update(a[0])
        qtile.widgets_map['vol_rest2'].update(b)
        qtile.widgets_map['vol_number2'].update(a[1]+'%')
    return a
