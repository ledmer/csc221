from gasp import *
def lines():
    
begin_graphics()
lines()
key_text = Text("ROBOTS!!!", (320, 270), size=48)
key_text = Text("Press any key to start", (320, 100), size=12)
update_when('key_pressed')
clear_screen()
p_x = 320
p_y = 220
while True:
    player = Circle((p_x, p_y), 100)
    key = update_when('key_pressed')
    remove_from_screen(player)
    if key == 'Right':
        p_x += 10
    if key == 'Left':
        p_x -= 10
    if key == 'Up':
        p_y += 10
    if key == 'Down': 
        p_y -= 10 
    elif key == "q":  
        break       
end_graphics()