import random as rd
chance = 0
found = False
num = rd.randint(1, 100)
print("you have 8 chance to guess the digit")
print("the digit is between 1 to 100")
while(chance < 8):
    answer = int(input("enter your guess: "))
    if answer == num:
        print(num," is the correct answer")
        found = True
        break
    elif answer > num:
        print(answer," is greater than the answer")
    else:
        print(answer," is less than the answer")
    chance = chance+1
if not found:
    print("You have used all your chances.The correct answer is ",num)


