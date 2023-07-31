from gasp import *
import time
from random import randint
import screenrobots as screen
class Junk :
    pass
class Player:   
    pass
class Robot:
    pass
def check_lost():
    global playing, robots
    for robot in robots:
        if ((player.x == robot.x) and (player.y == robot.y)):
            playing = False
            return True
    if len(robots) == 0:
        playing = False
        return False
def place_player():
    global player
    player = Player()
    player.x = randint(2,63)
    player.y = randint(2,47)
    player.shape = Circle((10 * player.x + 5, 10 * player.y + 5), 5, filled=True)

def teleport():
    global player, robots, key, teleport_times, tp_txt
    remove_from_screen(tp_txt)
    still_same = True
    while still_same:
        still_same = False
        player.x = randint(1, 63)
        player.y = randint(1, 47)
        for robot in robots:
            if player.x == robot.x and player.y == robot.y:
                player.x = randint(1, 63)
                player.y = randint(1, 47)
                still_same = True
    move_to(player.shape, (10 * player.x + 5, 10 * player.y + 5))
    teleport_times -= 1
    tp_txt = Text(f"Teleport Left: {teleport_times}",(540, 440), size=15)
    key = update_when('key_pressed')
    

def junkgen():
    global robots, junks
    del_robots = []
    for robot in robots:
        for junk in junks:
            if robot.x == junk.x and robot.y == junk.y:
                del_robots.append(robot)

    for A in range(len(robots) - 1):
        B = A + 1
        while B < len(robots):
            if robots[A].x == robots[B].x and robots[A].y == robots[B].y:
                if robots[A] not in del_robots:
                    del_robots.append(robots[A])
                if robots[B] not in del_robots:
                    del_robots.append(robots[B])
                junk = Junk()
                junk.x = robots[A].x
                junk.y = robots[A].y
                junk.shape = (Box((10 * junk.x, 10 *  junk.y), 10, 10, color = color.GREEN, filled=True))
                junks.append(junk)  
            B += 1
    for del_robot in del_robots:
        remove_from_screen(del_robot.shape)
        robots.remove(del_robot)
def place_robot ():
    global player, robots
    robot = Robot()
    robot.x = randint(2, 62)
    robot.y = randint(2, 47)
    while robot.x > player.x - 10 and robot.x < player.x + 10:
        robot.x = randint(2, 63)
    while robot.y > player.y - 10 and robot.y < player.y + 10:
        robot.y = randint(2, 47)
    robot.shape = (Circle((10 * robot.x + 5, 10 * robot.y + 5), 5, filled=True, color="Red"))
    robots.append(robot)
def move_robot():
    global robots, playing

    for robot in robots:
        if player.x > robot.x:
            robot.x += 1
        elif player.x < robot.x:
            robot.x -= 1
        if player.y > robot.y:
            robot.y += 1
        elif player.y < robot.y:
            robot.y -= 1
        move_to(robot.shape, (10 * robot.x + 5, 10 * robot.y+ 5))

        
def player_move():
    global key, player, robots, teleport_times,tp_txt
    key = update_when('key_pressed')
    while key == "t" and not teleport_times == 0:
        teleport()
    if key == 'KP_Right'or key == 'KP_6':
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

def Game(games_won):
    if games_won == 0:
        screen.start_screen()
    screen.lines()
    global playing, robots, key, junks, turn, teleport_times, tp_txt
    key = ""
    junks = []
    robots = []
    playing = True
    turn = 0
    robot_max = 0
    teleport_times = 5
    place_player()
    place_robot()
    tp_txt = Text(f"Teleport Left: {teleport_times}",(540, 440), size=15)
    while playing:
        turn += 1
        if turn % 2 == 0 and robot_max < 10 + games_won * 2:
            place_robot()
            robot_max += 1
        player_move()
        move_robot()
        junkgen()
        lost = check_lost()

    if lost:
        keep_playing = screen.loose_screen(games_won)
        games_won = 0
    else:
        games_won += 1
        keep_playing = screen.win_screen(turn, games_won)
    if keep_playing:
        Game(games_won)

begin_graphics(title = "Robots")
games_won = 0
Game(games_won)
end_graphics()
