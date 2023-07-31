from gasp import *
def ordinal(n):
    if 4 <= n <= 20:
      suffix = 'th'
    elif n == 1 or (n % 10) == 1:
      suffix = 'st'
    elif n == 2 or (n % 10) == 2:
      suffix = 'nd'
    elif n == 3 or (n % 10) == 3:
      suffix = 'rd'
    elif n < 100:
      suffix = 'th'
    ord_num = str(n) + suffix
    return ord_num
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

def loose_screen(games_won):
    time.sleep(1)
    clear_screen()
    Text("You Lost :'c",(320, 270), size=40)
    key_text = Text("Press esc to stop playing, Enter for another game", (320, 100), size=12)
    key = update_when('key_pressed')

    while not key == "Return":
        if key == "Escape":
            return False
        key = update_when('key_pressed')
    clear_screen()
    return True

def win_screen(turn, teleport_times, games_won):
    time.sleep(1)
    clear_screen()
    Text("You WIN!!!",(320, 270), size=40)

    Text(f"{ordinal(games_won)} Game won!",(540, 440), size=15)
    Text(f"It took you {turn} turns and {teleport_times} teleports!",(320, 160), size=20)
    Text("Press esc to stop playing, Enter to keep playing", (320, 100), size=12)
    key = update_when('key_pressed')
    while not key == "Return":
        if key == "Escape":
            return False
        key = update_when('key_pressed')
    clear_screen()
    return True
