print("Welcome to Treasure Island. ")
print("your work is to find the treasure. ")
direction1 = input("Let's get started!, choose Left or right if right click r if left click l ")
if direction1 == "l" or direction1 == "L":
    action = input("want to swim or wait? if you choose to swim type s or if you choose to wait type w ")
    if action == "w" or action == "W":
        door = input("which Door you want Blue, red or yellow? if you want blue door type b, if you want red door type r or if you want yellow door please type y ")
        if door == "y" or door == "Y":
            print("Hurry!, you win\n Game over.")
        elif door == "r" or door == "R":
            print("you fell into Lava.\n Game over.")
        else:
            print("eaten by beasts.\n Game over.")
    elif action == 's' or action == 'S':
        print("Attacked by trout.\n Game Over.")

else:
    print("fall into a hole.\n Game over")
