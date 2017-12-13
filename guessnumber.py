# Filename : guessnumber.py

# generate a random number between 1 and 9, ask the user to guess
# tell the user if they guessed too high or low or exactly right.
# keep the game going until the user types "exit"
# keep track of how many guesses the user has taken, and when game ends print


import random

number = random.randint(1,9)
guess = 0
count = 0

while guess != number and guess != "exit":
    guess = int(input("Guess number between 1 and 9: "))

    if guess == "exit":
        break

    guess = int(guess)
    count += 1

    if guess < number:
        print('Too low!')
    elif guess > number:
        print('Too high!')
    else:
        print('You got it!')
        print('And it only took you', count, "tries!")
