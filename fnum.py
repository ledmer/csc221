import random
i = 1
def find_n(f):
    try:
        ans = int(input(f"Guess{f}: "))
        while not ans == x:
            if ans > x:
                print("Too High!")
                f += 1
                ans = int(input(f"Guess{f}: "))
            elif ans < x:
                print("Too Low!")
                f += 1
                ans = int(input(f"Guess{f}: "))
    except:
        print("use numbers as output")
        find_n(f)
    print(f"it took you {f} tries")


x = random.randint(0, 1000)
print("Guess a number between 0 and 1000")
find_n(i) 

