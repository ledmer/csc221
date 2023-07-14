import random
from gasp.utils import read_yesorno

def find_rangn():
    try:
        rang = 0
        rang = int(input("Give a number as max range: "))
        while rang <= 1:
            print("not numbers less than 1 :3")
            rang = int(input("Give a number as max range: "))
        print(f"Guess a number between 0 and {rang}")
        rann = random.randint(0, rang)
        return rann
    except ValueError:
        print("Use numbers greater than 1!!")
        find_rangn()

def find_n(f):
    try:
        ans = float(input(f"Guess{f}: "))
        while not ans == rann:
            if ans > rann:
                print("Too High!")
                f += 1
                ans = float(input(f"Guess{f}: "))
            elif ans < rann:
                print("Too Low!")
                f += 1
                ans = float(input(f"Guess{f}: "))
    except ValueError:
        print("use numbers as input")
        find_n(f)
    else:
        print(f"it took you {f} tries")

game = True
while game == True:
    i = 1
    rann = find_rangn()
    find_n(i)
    game = read_yesorno('Would you like another game? ')


