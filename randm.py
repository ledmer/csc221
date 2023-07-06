import random
print("WELCOME! READY FOR A MATH GAME?")
questions = int(input("How many questions do you want? "))

nar = 0
a = 0
i = 10
for x in range(questions):
      num1 = random.randint(int(a),int(i))
      num2 = random.randint(int(a),int(i))
      ans = int(input(f"What is {num1} times {num2}? "))
      rans = num1*num2
      if not rans == ans:
          i /= 1.3
          if not a < 0:
              a /= 2
          if rans-3 < ans and rans+3 > ans:
              print(f"Close!!, the answer was {rans}\n")
          else:
              print(f"You are wrong, its {rans}\n")      
      else:
            print(f"You are right!, the answer is {rans}\n")
            nar += 1
            i *= 1.4
            a += 5
print(f"{nar} out of {questions}", end =" ")
if nar == questions:
    print("EXCELLENT PERFECT SCORE!!!!!!")
elif nar > 0.7 * questions:
    print("NICE, Almost Perfect")
elif nar >= 0.5 * questions:
    print("Good!")
elif nar == 0:
    print("._. really??")
else:
    print("keep trying :c")
