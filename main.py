# Number Guessing Game

# import random
#
# random_num = random.randint(1, 100)
# while True:
#     guess = input("Guess the number between 1 and 100: ")
#     if not guess.isdigit():
#         print("Please enter a valid number!")
#         continue
#     guess = int(guess)
#     if guess > random_num:
#         print("Too high!")
#     elif guess < random_num:
#         print("Too low!")
#     else:
#         print("Congratulations! You guessed the number.")
#         break

###################################################################

import random

random_num = random.randint(1, 100)
while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))
        if guess > random_num:
            print("Too high!")
        elif guess < random_num:
            print("Too low!")
        else:
            print("Congratulations! You guessed the number.")
            break
    except ValueError:
        print("Please enter a valid number!")