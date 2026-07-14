import random

secret_number = random.randint(1, 100)

while True:
    guess = input("Guess the secret number between 1 and 100: ")
    if int(guess) == secret_number:
        print("Congratulations! You guessed the secret number.")
        break
    elif int(guess) < secret_number:
        print("Too low! Try again.")
    else:
        print("Try again!")