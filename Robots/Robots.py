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

    robots.append(robot)


        

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
