import random

num = random.randint(1,100)

print("Guess the number between 1 - 100")
guess = None

while guess != num:
    guess = int(input())
    if guess < num:
        print("Higher")
    if guess > num:
        print("Lower")
    if guess == num:
        print("Correct")
