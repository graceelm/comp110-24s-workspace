"""Number guessing game."""
from random import randint

SECRET: int = randint(1,5) 
correct: bool = False

while correct == False:
    guess: int = int(input("Guess a number between 1 and 5: "))
    if guess > 5:
        print("Error! Guess is too high!")
    if guess < 1:
        print("Error! Your guess is too low!")
    if guess == SECRET:
        print(f"You got it right! {guess} is the secret number!")
        correct = True
    else:
        print("Try again!")