from getpass import getpass
import random
from gasp.utils import read_yesorno

def find_rangn():
    try:
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

def find_n(f, games_played = 1):
    try:
        ans = float(input(f"Player{games_played} Guess{f}: "))
        while not ans == rann:
            if ans > rann:
                print("Too High!")
                f += 1
            elif ans < rann:
                print("Too Low!")
                f += 1
            ans = float(input(f"Player{games_played} Guess{f}: "))
    except ValueError:
        print("use numbers as input")
        find_n(f)
    else:
        print(f"it took you {f} tries")
    
def player_ans(games_played):
    try:
        x = 1
        if games_played % 2 == 0:
            x += 1
        rang = int(input(f"Player{x} Give a number as max range: "))
        while rang <= 1:
            print("not numbers less than 1 :3")
            rang = int(input(f"Player{x} Give a number as max range: "))
        numb = int(getpass("Secret number: "))
        while numb > rang or numb < 0:
            print("Give a number inside the range!!")
            numb = getpass(f"Player{x} Secret number: ")
        print("\n" + f"Guess a number between 0 and {rang}")
        return numb
    except ValueError:
        print("Use numbers!!")
        find_rangn()

games_played = 0
game = True
while game == True:
    player2 = read_yesorno('Wanna play 2 player game?')
    i = 1
    print(f"Game {games_played}:")
    if player2 == False:
        rann = find_rangn()
        find_n(i)
    elif player2 == True:
        rann = player_ans(games_played)
        find_n(i, games_played % 2 + 1)
    game = read_yesorno('Would you like another game? ')
    games_played += 1


