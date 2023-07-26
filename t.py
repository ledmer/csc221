from gasp import *
import time
from random import randint

def junkgen():
    global junk_x
    global junk_y
    global player_x
    global player_y 
    global robot_x
    global robot_y
    global robot
    for zz in range(len(robot_x)-1):
        z = zz + 1
        while z < len(robot_x)-1:    
            if robot_x[zz] == robot_x[z] and robot_y[zz] == robot_y[z]:
                print("robot lost")
                junk_x.append(robot_x.pop(z))
                junk_y.append(robot_y.pop(z))
                robot.pop(z)
                robot_x.pop(zz)
                robot_y.pop(zz)
                robot.pop(zz)
            z += 1
        for m in range(len(junk_x)-1):
            if robot_x[zz] == junk_x[m] and robot_y[zz] == junk_x[m]:
                robot_x.pop(zz)
                robot_y.pop(zz)
                robot.pop(zz)
    for jk in range(len(junk_x)):
        Box((10 * junk_x[jk],10 *  junk_y[jk]), 10,10,color = color.GREEN)
def robotcraft ():
    global player_x
    global player_y 
    global robot_x
    global robot_y
    global robot
    x = randint(2, 62)
    y = randint(2, 47)
    while x > player_x-10 and x < player_x+10:
        x = randint(2, 47)
    while y > player_y-10 and y < player_y+10:
        y = randint(2, 63)
    robot_x.append(x)
    robot_y.append(y)

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
    
def rob(i):
    global robot
    global game
    global player_x
    global player_y 
    global robot_x
    global robot_y
    
    if i % 4 == 0:
        robotcraft()

    for ra in range(len(robot_x)-1): 
        robot.append(Circle((10 * robot_x[ra] + 5, 10 * robot_y[ra] + 5), 5, filled=True, color="Red"))
        if player_x > robot_x[ra]:
            robot_x[ra] += 1
        elif player_x < robot_x[ra]:
            robot_x[ra] -= 1
        if player_y > robot_y[ra]:
            robot_y[ra] += 1
        elif player_y < robot_y[ra]:
            robot_y[ra] -= 1
def py():
    global player_x
    global player_y 
    global robot_x
    global robot_y
    global robot
    
    player = Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True)
    key = update_when('key_pressed')
    for ra in robot:
        remove_from_screen(ra)
    if key == 'KP_Right'or key == 'KP_6' :
        player_x += 1
    elif key == 'KP_Left'or key == 'KP_4':
        player_x -= 1
    elif key == 'KP_Up'or key == 'KP_8':
        player_y += 1
    elif key == 'KP_Down'or key == 'KP_2':
        player_y -= 1
    elif key == 'KP_Prior'or key == 'KP_9':
        player_x += 1 
        player_y += 1
    elif key == 'KP_Home'or key == 'KP_7':
        player_x -= 1 
        player_y += 1 
    elif key == 'KP_End'or key == 'KP_1':
        player_x -= 1
        player_y -= 1 
    elif key == 'KP_Next'or key == 'KP_3': 
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

def GGame(i):
    start_screen()
    lines()
    global game
    global player_x 
    global player_y 
    global robot_x
    global robot_y
    global robot
    global junk_x
    global junk_y
    robot_x = []
    robot_y = []
    robot = []

    junk_y = []
    junk_x = []
    game = True
    player_x = randint(2,63)
    player_y = randint(2,47)
    robotcraft()
    while game:
        i += 1
       # for mm in range(len(robot_x)):
            #if (player_x == robot_x[mm]) and (player_y == robot_y[mm]):
                #game = False
        junkgen()
        py()
        rob(i)
        
    lost = loose()
    if not lost:
        GGame(i)


begin_graphics(title = "Robots")
i = 0
GGame(i)
end_graphics()
