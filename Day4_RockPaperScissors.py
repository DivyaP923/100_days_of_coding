import random
print("welcome to rock paper scissors game.")
computer_choice = ["rock","paper","scissors"]
user_input = input("choose rock, paper or scissors: ")
computer_result = random.choice(computer_choice)
print("computer choice: ", computer_result)
while True:
    if computer_result == user_input:
       computer_result = random.choice(computer_choice)
       print("it's a draw")   
       user_input = input("Please choose again rock, paper or scissors: ")
    elif computer_result == "rock" and user_input=="paper":
        print('Hurry!, you win') 
        break  
    elif computer_result == "paper" and user_input=="rock":
        print('sorry you loose, better luck next time')
        break
    elif computer_result == "rock" and user_input=="scissors":
        print('Hurry!, you win')
        break
    elif computer_result == "scissors" and user_input=="rock":
        print('sorry you loose, better luck next time')
        break
    elif computer_result == "scissors" and user_input=="rock":
        print('Hurry!, you win')
        break
    elif computer_result == "rock" and user_input=="scissors":
        print('sorry you loose, better luck next time')
        break
    elif computer_result == "scissors" and user_input=="paper":
        print('sorry you loose, better luck next time')
        break
    elif computer_result == "paper" and user_input=="scissors":
        print('Hurry!, you win')
        break
    else:
        print("invalid input")
        break
    
        
 