from gasp import *
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

begin_graphics()

start_screen()

lines()
player_x = 5
player_y = 5
while True:
    player = Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True)
    key = update_when('key_pressed')
    for y in range(0,480,20):
        key = update_when('key_pressed')
        Text(key, (320, 100+y), size=12)
    remove_from_screen(player)
    if key == 'Right':
        player_x += 1
    if key == 'Left':
        player_x -= 1
    if key == 'Up':
        player_y += 1
    if key == 'Down': 
        player_y -= 1
    if player_x > 63:
        player_x = 1
    if player_y > 47:
        player_y = 1
    if player_x < 0:
        player_x = 63
    if player_y < 0:
        player_y = 47
    elif key == "q": 
        break       
end_graphics()