import random

num = random.randint(1, 100)

while True:
    guess = int(input("Guess the number: "))
    if guess > num:
        print("Too High")
    elif guess < num:
        print("Too Low")
    else:
        print("Correct!")
        break
