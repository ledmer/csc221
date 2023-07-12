from gasp import *
import time

def stop_smiling(x, y):
    n = 30
    while n < 90:
        Circle((320 + x, 240 + y), 100, color="green", filled=True)
        Circle((280 + x, 270 + y), 20, color="black", filled=True)
        Circle((360 + x, 270 + y), 20, color="black", filled=True)
        Arc((320 + x, 240 + y), 80, 180+n, 360-n, thickness = 4)
        Line((300+x,220+y),(320+x,250+y),thickness = 4)
        Line((300+x,220+y),(340+x,220+y),thickness = 4)
        
        Line((360+x,340+y),(320+x,380+y),thickness = 4)
        Line((280+x,340+y),(321+x,380+y),thickness = 4)
        Line((280+x,340+y),(360+x,340+y),thickness = 4)
        
        n += 15
        time.sleep(1)

def serious_f(x, y):
    n = 0
    i = 0
    while n < 30:
        if n == 25:
            i += 20
        Circle((320 + x, 240 + y), 100, color="green", filled=True)
        Circle((280 + x - i, 270 + y), 20, color="black", filled=True)
        Circle((360 + x - i, 270 + y), 20, color="black", filled=True)
        Line((290 + n + x, 200 + y), (350 + n + x, 200 + y),thickness = 4)
        Line((300+x,220+y),(320+x,250+y),thickness = 4)
        Line((300+x,220+y),(340+x,220+y),thickness = 4)
        Line((360+x,340+y),(320+x,380+y),thickness = 4)
        Line((280+x,340+y),(321+x,380+y),thickness = 4)
        Line((280+x,340+y),(360+x,340+y),thickness = 4)
        n += 25
        time.sleep(0.9)

def move(i):
    if i == 0:
        return 0,0
    elif i == 1:
        return 120, 100
    elif i == 2:
        return -120, 100
    elif i == 3:
        return -120, -100
    elif i == 4:
        return 120, -100

begin_graphics()
n = ""
i = 0

while not n == "x":
    if i == 4:
        i = 0
        x, y = move(i)
        stop_smiling(x, y)
        serious_f(x, y)
        n = update_when('key_pressed')
        i += 1
        if n == "x":
            break
        clear_screen()
    x, y = move(i)
    stop_smiling(x, y)
    serious_f(x, y)
    clear_screen()
    i += 1

end_graphics()