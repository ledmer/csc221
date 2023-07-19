from gasp import *

begin_graphics()         

def place_player():
   Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True)

def move_player():
    print("I'm moving...")
    update_when('w')
     

finished = False

place_player()

while not finished:
    move_player()

end_graphics()