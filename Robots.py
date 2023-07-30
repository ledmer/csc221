from gasp import *
import time
from random import randint
import screenrobots as screen
class Junk:
    pass
class Player:   
    pass
class Robot:
    pass
def check_lost():
    global playing, robot_x, robot_y, robots
    for robot in range(len(robot_x)):
        if ((player.x == robot_x[robot]) and (player.y == robot_y[robot])):
            playing = False
            return True
    if len(robots) == 0:
        playing = False
     
def place_player():
    global player
    player = Player()
    player.x = randint(2,63)
    player.y = randint(2,47)
    player.shape = Circle((10 * player.x + 5, 10 * player.y + 5), 5, filled=True)

def collided(thing1, list_of_things):
    for thing2 in list_of_things:
        if thing1.x == thing2.x and thing1.y == thing2.y:
            return True
    return False

def teleport():
    global player
    while True:
        new_x = randint(1, 63)
        new_y = randint(1, 47)
        
        if new_x != robot_x and new_y != robot_y:
            player.x = new_x
            player.y = new_y
            break
def junkgen():
    global junk_x, junk_y, robot_x, robot_y, robots, junk
    del_robots = []
    for rob_index in range(len(robot_x)):
        for junk_index in range(len(junk_x)):
            if robot_x[rob_index] == junk_x[junk_index] and robot_y[rob_index] == junk_y[junk_index]:
                del_robots.append(rob_index)
                print(rob_index , "s")

    for del_robot1 in range(len(robot_x) - 1):
        del_robot2 = del_robot1 + 1
        while del_robot2 < len(robot_x):
            if robot_x[del_robot1] == robot_x[del_robot2] and robot_y[del_robot1] == robot_y[del_robot2]:
                if del_robot1 not in del_robots:
                    del_robots.append(del_robot1)
                if del_robot2 not in del_robots:
                    del_robots.append(del_robot2)

                junk_x.append(robot_x[del_robot2])
                junk_y.append(robot_y[del_robot2])
            del_robot2 += 1

    for junk_ind in range(len(junk_x)):
            junk.append(Box((10 * junk_x[junk_ind], 10 *  junk_y[junk_ind]), 10, 10, color = color.GREEN, filled=True))
    
    for junk1 in range(len(junk_x) - 1):
        junk2 = junk1 + 1
        while junk2 < len(junk_x):
            if (junk_x[junk1] == junk_x[junk2] and junk_y[junk1] == junk_y[junk2]):
                junk.pop(junk1)
            junk2 += 1
    print(del_robots,"delrob")
    print(len(robots))
    i = 0
    for del_robot in del_robots:
        robot_x.pop(del_robot - i)
        robot_y.pop(del_robot - i)
        robots.pop(del_robot - i)
        i += 1
def place_robot ():
    global player, robot_x, robot_y, robots

    x = randint(2, 62)
    y = randint(2, 47)
    while x > player.x - 10 and x < player.x + 10:
        x = randint(2, 47)
    while y > player.y - 10 and y < player.y + 10:
        y = randint(2, 63)
    robot_x.append(x)
    robot_y.append(y)
    robots.append(Circle((10 * robot_x[-1] + 5, 10 * robot_y[-1] + 5), 5, filled=True, color="Red"))
   
def move_robot():
    global robots, playing, robot_x, robot_y

    for rob in range(len(robot_x)): 
        if player.x > robot_x[rob]:
            robot_x[rob] += 1
        elif player.x < robot_x[rob]:
            robot_x[rob] -= 1
        if player.y > robot_y[rob]:
            robot_y[rob] += 1
        elif player.y < robot_y[rob]:
            robot_y[rob] -= 1
        move_to(robots[rob], (10 * robot_x[rob] + 5, 10 * robot_y[rob] + 5))

def player_move():
    global key, player, robots, teleport_times

    key = update_when('key_pressed')
    while key == "t":
        teleport()
        move_to(player.shape, (10 * player.x + 5, 10 * player.y + 5))
        key = update_when('key_pressed')
        teleport_times += 1
    if key == 'KP_Right'or key == 'KP_6' :
        player.x += 1
    elif key == 'KP_Left'or key == 'KP_4':
        player.x -= 1
    elif key == 'KP_Up'or key == 'KP_8':
        player.y += 1
    elif key == 'KP_Down'or key == 'KP_2':
        player.y -= 1
    elif key == 'KP_Prior'or key == 'KP_9':
        player.x += 1 
        player.y += 1
    elif key == 'KP_Home'or key == 'KP_7':
        player.x -= 1 
        player.y += 1 
    elif key == 'KP_End'or key == 'KP_1':
        player.x -= 1
        player.y -= 1 
    elif key == 'KP_Next'or key == 'KP_3': 
        player.x += 1 
        player.y -= 1 
    if player.x > 63:
        player.x = 1
    if player.y > 47:
        player.y = 1
    if player.x < 0:
        player.x = 63
    if player.y < 0:
        player.y = 47
    move_to(player.shape, (10 * player.x + 5, 10 * player.y + 5))
    time.sleep(0.02)

def Game():
    screen.start_screen()
    screen.lines()
    global playing, robot_x, robot_y, robots, junk_x, junk_y, key, junk, turn, teleport_times
    key = ""
    robot_x = []
    robot_y = []
    robots = []
    junk = []
    junk_y = []
    junk_x = []
    playing = True
    teleport_times = 0
    turn = 0
    robot_max = 0
    place_player()
    place_robot()
    while playing:
        turn += 1 
        if turn % 4 == 0 and robot_max < 10:
            place_robot()
            robot_max += 1
        player_move()
        move_robot()
        junkgen()
        lost = check_lost() 
    if lost:
        keep_playing = screen.loose_screen()
    else: 
        keep_playing = screen.win_screen(turn, teleport_times)
    if keep_playing:
        Game()
begin_graphics(title = "Robots")
Game()
end_graphics()
