import random
lives_stages = ['''
   +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''              
  +---+
  |   |
      |
      |
      |
      |
=========''' 
 ]

print("welcome to hagaman game")
words_list=['action','reaction','addiction','remedy','comedy']
computer_choice_word = random.choice(words_list)
#print(computer_choice_word)
placeholder=""
for letter in computer_choice_word:
    placeholder+="_"
print(placeholder)
word_len= len(computer_choice_word) 
correct_letters = []
right_guess = False
lives = 6
while not right_guess and lives!=0:
    display=''
#getting input from the user and changing it into a lower case letter
    user_choice_letter = input('guess a letter in the word: ').lower()
    for letter in computer_choice_word:
        if user_choice_letter == letter:
            display += letter
            correct_letters.append(user_choice_letter)    
        elif letter in correct_letters:
            display +=letter
        else :
            display += '_'
        
    print(lives)
    print(display)
    if user_choice_letter not in computer_choice_word:
        lives -=1
    print(lives_stages[lives])
    if "_" not in display:
        print("you win")
        right_guess=True 
    if lives==0 and display !=computer_choice_word:
            print('You loose!, better luck next time')   
print(computer_choice_word)
    
    


