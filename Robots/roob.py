from gasp import *
import time
from random import randint

    
class Player:
    def __init__(self):
        self.x = randint(2, 63)
        self.y = randint(2, 47)
        self.shape = Circle((10 * self.x + 5, 10 * self.y + 5), 5, filled=True)
    
    def teleport(self):
        self.x = randint(1, 63)
        self.y = randint(1, 47)
        move_to(self.shape, (10 * self.x + 5, 10 * self.y + 5))
    def player_move(self):
        key = update_when('key_pressed')
        while key == "t":
            self.teleport()
            key = update_when('key_pressed')
        if key == 'KP_Right'or key == 'KP_6':
            self.x += 1
        elif key == 'KP_Left'or key == 'KP_4':
            self.x -= 1
        elif key == 'KP_Up'or key == 'KP_8':
            self.y += 1
        elif key == 'KP_Down'or key == 'KP_2':
            self.y -= 1
        elif key == 'KP_Prior'or key == 'KP_9':
            self.x += 1 
            self.y += 1
        elif key == 'KP_Home'or key == 'KP_7':
            self.x -= 1 
            self.y += 1 
        elif key == 'KP_End'or key == 'KP_1':
            self.x -= 1
            self.y -= 1 
        elif key == 'KP_Next'or key == 'KP_3': 
            self.x += 1 
            self.y -= 1 
        if self.x > 63:
            self.x = 1
        if self.y > 47:
            self.y = 1
        if self.x < 0:
            self.x = 63
        if self.y < 0:
            self.y = 47
        move_to(self.shape, (10 * self.x + 5, 10 * self.y + 5))
        time.sleep(0.02)
    def check_lost(self):
        for robot in robots:
            if ((player.x == robot.x) and (player.y == robot.y)):
                playing = False
                return True
        if len(robots) == 0:
            playing = False
            return False

class Robot:
    def __init__(self):
        self.x = randint(2, 62)
        self.y = randint(2, 47)
        while self.x > player.x - 10 and self.x < player.x + 10:
            self.x = randint(2, 63)
        while self.y > player.y - 10 and self.y < player.y + 10:
            self.y = randint(2, 47)
        self.shape = (Circle((10 * self.x + 5, 10 * self.y + 5), 5, filled=True, color="Red"))
    
    def chase(self):
        if player.x > robot.x:
            robot.x += 1
        elif player.x < robot.x:
            robot.x -= 1
        if player.y > robot.y:
            robot.y += 1
        elif player.y < robot.y:
            robot.y -= 1
        move_to(robot.shape, (10 * robot.x + 5, 10 * robot.y+ 5))

class Junk:
    
begin_graphics(title = "Robots")
player = Player()
robots = []
robot = Robot()
while True:
    player.player_move()
    robot.chase()
end_graphics()
