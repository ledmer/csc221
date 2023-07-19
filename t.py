from gasp import *
import time

def lines():
    line_x = 0
    line_y = 0
    for y in range(0,480,10):
        Line((0,y),(640,y),thickness=.01,color='lightgray')
    for x in range(0,640,10):
        Line((x,0),(x,640),thickness=.01,color='lightgray')

def place_player(player_x,player_y):
    Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True)

def start_screen():
    key_text = Text("ROBOTS!!!", (320, 270), size=48)
    key_text = Text("Press any key to start", (320, 100), size=12)
    update_when('key_pressed')
    clear_screen()

def GGame():
    start_screen()
    lines()
    player_x = 5
    player_y = 5
    robot_x = 40
    robot_y = 40
    game = True
    while game:
        player = Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True)
        robot = Circle((10 * robot_x + 5, 10 * robot_y + 5), 5, filled=True, color="Red")
        key = update_when('key_pressed')
        
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
        elif key == "q":
            return
        remove_from_screen(player)
        if player_x == robot_x and player_y == robot_y: 
            game = False
        if player_x > robot_x:
            robot_x += 1
        elif player_x < robot_x:
            robot_x -= 1
        if player_y > robot_y:
            robot_y += 1
        elif player_y < robot_y:
            robot_y -= 1
        remove_from_screen(robot)
    time.sleep(1)
    clear_screen()
    Text("You Lost :'c",(320, 270), size=40)
    key_text = Text("Press esc to stop playing", (320, 100), size=12)
    man = update_when('key_pressed')
    if man == "Escape":
        return
    GGame()


begin_graphics(title = "Robots")

GGame()
end_graphics()