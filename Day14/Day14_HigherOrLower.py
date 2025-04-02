import random
import art
from game_board import data

print(art.logo)
a_random = random.choice(data)
print(f"Compare A: {a_random['name']}, {a_random['description']} from {a_random['country']}")
print(art.versus)
guess = True
score = 0
def design(current_score, a):
    """Displays updated game status when the user is correct."""
    print(f"you'r right, current score: {current_score}")
    print(f"Compare A: {a['name']}, {a['description']} from {a['country']}")
    print(art.versus)


while guess == True:
    b_random = random.choice(data)
    # Ensure A and B are not the same
    while b_random == a_random:
        b_random = random.choice(data)

    print(f"Against B: {b_random['name']}, {b_random['description']} from {b_random['country']}")
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
     
    if user_input == 'a':
        if a_random['follower_count']>=b_random['follower_count']:
            score +=1
            design(score, a_random)
        else:
            # Clear the screen and only show the final result
            print("\033[H\033[J", end="") # ANSI escape code to clear the terminal screen
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            guess = False
    elif user_input == 'b':
        if b_random['follower_count']>=a_random['follower_count']:
            score += 1
            a_random= b_random
            design(score, a_random)
        else:
            # Clear the screen and only show the final result
            print("\033[H\033[J", end="") # ANSI escape code to clear the terminal screen
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            guess = False