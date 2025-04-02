user_exists = True
bid = {}

while user_exists:
    #getting inputs from the user
    name = input("Enter the  name of the bidder: ")
    value = int(input("Enter the bid amount: "))
    bid[name] = value
    user_present = input("Are there any other bidders? if yes type 'yes' otherwise type 'no': ").lower()
    print("\n" *50)
    if user_present == 'no':
        user_exists = False
    

#looping through the dictionary to find the highest bid amount
max_value = 0
for bidder in bid:
    if bid[bidder]>max_value:
        max_value = bid[bidder]
print(f"the bid winner is {bidder} with the bid amount Rs.{max_value} ")


