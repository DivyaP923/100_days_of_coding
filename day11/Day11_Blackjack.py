import random
import art
print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

def deal_cards():
    global user_cards,computer_cards
    user_cards = random.choices(cards,k=2)
    computer_cards = random.choices(cards,k=2)
    print(computer_cards)
    print(f'your cards: {user_cards} current score: {sum(user_cards)}')
    print(f'computers first card: {computer_cards[0]}')

deal_cards()

while sum(user_cards)<21:
    user_pick = input('type "yes" to pick another card otherwise type "no"').lower()
    if user_pick == 'yes':
        card_picked = random.choice(cards)
        user_cards.append(card_picked)
        print(user_cards)
        print(f"your current score {sum(user_cards)}")
    else:
        break
print(f"your final score{sum(user_cards)}")

while 11 in user_cards and sum(user_cards)>21:
    user_cards.remove(11)
    user_cards.append(1)

while sum(computer_cards)<17:
    computer_cards.append(random.choice(cards))

if sum(user_cards)>21:
    print(computer_cards)
    print("you busted, dealer wins")
elif sum(user_cards) > sum(computer_cards):
    print(computer_cards)
    print("you busted, dealer wins")
elif sum(computer_cards)>21:
    print(computer_cards)
    print("Dealer busted, You win!")
elif sum(user_cards) < sum(computer_cards):
    print(computer_cards)
    print("Dealer busted, You win!")
else:
    print("its a draw")