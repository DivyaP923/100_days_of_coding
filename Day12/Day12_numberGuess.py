import art
import random

print(art.logo)
print("Welcome to Number Guess game")
print("I am thinking of a number in between 1 to 100")
difficulty_level = input('Choose a difficulty. Type "easy" or "hard" ').lower()
computer_choice = random.randint(1,100)


def number_guess(level,choice):
    chances = 0
    if level == 'easy':
        chances = 10
        print(" You have 10 attempts to guess the correct number ")
    elif level == 'hard':
        chances = 5
        print(" You have 5 attempts to guess the correct number")
    while chances!=0:
        user_guess = int(input("Make a guess: "))
        if user_guess > choice:
            print("Too high")
            chances -=  1
        elif user_guess < choice:
            print("Too low")
            chances -=  1
        else :
            print(f" You guessed it correct, the number was {choice}")
            chances = 0
            
        if chances > 0:
            print(f"You have {chances} attempts remaining.")
        else:
            print(f"Sorry, you're out of guesses. The correct number was {choice}.")
        


number_guess(difficulty_level,computer_choice)









