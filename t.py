from gasp import *
import time
from random import randint
def loose():
    time.sleep(1)
    clear_screen()
    Text("You Lost :'c",(320, 270), size=40)
    key_text = Text("Press esc to stop playing", (320, 100), size=12)
    en = update_when('key_pressed')
    clear_screen()
    if en == "Escape":
        return True
    return False
    
def rob():
    global robot
    global game
    global player_x
    global player_y 
    global robot_x
    global robot_y
    robot = Circle((10 * robot_x + 5, 10 * robot_y + 5), 5, filled=True, color="Red")
    if player_x > robot_x:
        robot_x += 1
    elif player_x < robot_x:
        robot_x -= 1
    if player_y > robot_y:
        robot_y += 1
    elif player_y < robot_y:
        robot_y -= 1
def py():
    global player_x
    global player_y 
    global robot_x
    global robot_y
    global robot
    
    player = Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True)
    key = update_when('key_pressed')
    remove_from_screen(robot)
    Text(key,(320, 100), size=12)
    if key == 'KP_Right':
        player_x += 1
    elif key == 'KP_Left':
        player_x -= 1
    elif key == 'KP_Up':
        player_y += 1
    elif key == 'KP_Down':
        player_y -= 1
    elif key == 'KP_Prior':
        player_x += 1 
        player_y += 1
    elif key == 'KP_Home':
        player_x -= 1 
        player_y += 1 
    elif key == 'KP_End':
        player_x -= 1
        player_y -= 1 
    elif key == 'KP_Next': 
        player_x += 1 
        player_y -= 1 
    if player_x == 63:
        player_x = 1
    if player_y == 47:
        player_y = 1
    if player_x == 0:
        player_x = 63
    if player_y == 0:
        player_y = 47

    remove_from_screen(player)
    return
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

def GGame():
    start_screen()
    lines()
    global game
    global player_x 
    global player_y 
    global robot_x
    global robot_y
    global robot
    robot = Circle((1, 1), 1, filled=True)
    game = True
    player_x = randint(2,63)
    player_y = randint(2,47)
    robot_x = randint(2, 62)
    robot_y = randint(2, 47)
    while robot_x > player_x-10 and robot_x < player_x+10:
        robot_x = randint(2, 47)
    while robot_x > player_x-10 and robot_x < player_x+10:
        robot_y = randint(2, 63)
    while game:
        if player_x == robot_x and player_y == robot_y:
            game = False
        py()
        rob()

    lost = loose()
    if not lost:
        GGame()


begin_graphics(title = "Robots")

GGame()
end_graphics()