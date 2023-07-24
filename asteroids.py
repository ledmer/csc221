# GASP games Asteroids Sheet
# Written by Silas Riggs

############################################################
# This version of Asteroids is not fully completed yet.    #
# You can move around and shoot,                           #
# but no collisions have been implemented yet.             #
############################################################

from gasp import games
from gasp import color
import math
import random

SCREENWIDTH = 640
SCREENHEIGHT = 480


class KeepsToScreen:
    # This class is designed as a mix-in
    def keep_to_screen(self):

        oldpos = (x, y) = self.pos()

        if x > SCREENWIDTH:
            x = 0
        if x < 0:
            x = SCREENWIDTH
        if y > SCREENHEIGHT:
            y = 0
        if y < 0:
            y = SCREENHEIGHT

        if (x, y) != oldpos:
            self.move_to((x, y))


class Asteroid(games.Sprite, games.Mover, KeepsToScreen):
    # The larger ASTEROID_SPEED is, the slower the asteroids will move
    ASTEROID_SPEED = 100

    def __init__(self, screen, x, y, size=2):
        image = self.images[size]

        self.init_sprite(screen=screen, x=x, y=y, image=image)
        max_speed = 20 // (size + 1)
        dx = random.randint(1, max_speed) / self.ASTEROID_SPEED
        dy = random.randint(1, max_speed) / self.ASTEROID_SPEED
        self.init_mover(dx, dy)

    def moved(self):
        self.keep_to_screen()

    def hit(self, what_hit_me):
        if isinstance(what_hit_me, Bullet):
            new_size = self.size - 1
            if new_size >= 0:
                self.destroy()


class Ship(games.Polygon, games.Mover, KeepsToScreen):
    THRUST = 0.01
    LIST_POINTS = ((0, 0), (6, -20), (12, 0))

    def __init__(self, screen):
        self.init_polygon(screen=screen, x=SCREENWIDTH/2, y=SCREENHEIGHT/2,
                          shape=Ship.LIST_POINTS, color=color.RED)
        self.init_mover(dx=0, dy=0)
        self.cooldown = 0
        self.max_cooldown = 25

    def moved(self):
        self.keep_to_screen()
        if self.screen.is_pressed(games.K_a):
            self.rotate_by(3)
        if self.screen.is_pressed(games.K_d):
            self.rotate_by(-3)
        if self.screen.is_pressed(games.K_SPACE):
            self.thrust()
        if self.screen.is_pressed(games.K_RETURN):
            self.cooldown += 1
            if self.cooldown >= self.max_cooldown:
                self.fire()
                self.cooldown = 0
        else:
            self.cooldown = self.max_cooldown
        if self.screen.is_pressed(games.K_ESCAPE):
            my_screen.quit()

    def lose_game(self):
        message = games.Text(screen=self.screen, x=SCREENWIDTH / 2, y=SCREENHEIGHT / 2, text="Game Over", size=90,
                             color=color.RED)

    def hit(self, what_hit_me):
        self.destroy()
        self.lose_game()

    def thrust(self):
        angle = self.angle()

        change_in_v = angle_and_length(angle, Ship.THRUST)
        v = self.get_velocity()
        new_v = add_vectors(v, change_in_v)
        self.set_velocity(new_v)

    def fire(self):
        Bullet(screen=self.screen, ship_pos=self.pos(),
               ship_velocity=self.get_velocity(), ship_angle=self.angle())


class Bullet(games.Circle, games.Mover, KeepsToScreen):
    SPEED = 5
    TIME_TO_LIVE = 50
    SIZE = 2

    def __init__(self, screen, ship_pos, ship_velocity, ship_angle):
        offset = Bullet.SIZE + 21

        offset_vec = angle_and_length(ship_angle, offset)
        velocity = angle_and_length(ship_angle, Bullet.SPEED)
        x, y = ship_pos

        self.init_circle(screen, x, y, Bullet.SIZE, color.YELLOW)

        vx, vy = velocity
        self.init_mover(vx, vy)

        self.time_left = Bullet.TIME_TO_LIVE

    def hit(self, what_hit_me):
        self.destroy()

    def moved(self):
        self.keep_to_screen()
        self.time_left -= 1
        if self.time_left <= 0:
            self.destroy()


def angle_and_length(angle, length):
    radian_angle = angle * math.pi / 180
    x = -(length * math.sin(radian_angle))
    y = -(length * math.cos(radian_angle))
    return x, y


def add_vectors(first, second):
    x = first[0] + second[0]
    y = first[1] + second[1]
    return x, y


my_screen = games.Screen(width=SCREENWIDTH, height=SCREENHEIGHT)

my_ship = Ship(my_screen)
stars = games.load_image("img_stars.bmp")
Asteroid.image = games.load_image("img_asteroid.bmp")
Asteroid.images = []
for scale in [.25, .5, 1]:
    new_image = games.scale_image(Asteroid.image, scale)
    Asteroid.images.append(new_image)

my_screen.set_background(stars)
for size in [0, 1, 2, 1]:
    Asteroid(screen=my_screen, x=random.randint(0, SCREENWIDTH),
             y=random.randint(0, SCREENHEIGHT), size=size)

my_screen.mainloop()
