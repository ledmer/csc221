from gasp import *
def lines():
    line_x = 0
    line_y = 0
    for y in range(0,480,10):
        Line((0,y),(640,y),thickness=.01,color='lightgray')
    for x in range(0,640,10):
        Line((x,0),(x,640),thickness=.01,color='lightgray')

def start_screen():
    key_text = Text("ROBOTS!!!", (320, 270), size=48)
    key_text = Text("Press any key to start", (320, 100), size=12)
    update_when('key_pressed')
    clear_screen()

def loose_screen():
    time.sleep(1)
    clear_screen()
    Text("You Lost :'c",(320, 270), size=40)
    key_text = Text("Press esc to stop playing", (320, 100), size=12)
    en = update_when('key_pressed')
    if en == "Escape":
        return False
    clear_screen()
    return True

def win_screen(turn, teleport_times):
    time.sleep(1)
    clear_screen()
    Text("You WIN!!!",(320, 270), size=40)
    Text(f"It took you {turn} turns and {teleport_times} teleports!",(320, 160), size=25)
    key_text = Text("Press esc to stop playing", (320, 100), size=12)
    en = update_when('key_pressed')
    
    if en == "Escape":
        return False
    clear_screen()
    return True