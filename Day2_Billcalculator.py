print("Welcome to bill calculator")
cost = float(input("whats your bill amount? "))
tip_percent = int(input("how much do you want to tip 0, 5, 10? "))
number_of_persons = int(input("how many people do we need to split the bill with: "))
cost_tip = (cost*float(tip_percent/100))+cost
person_share = cost_tip/float(number_of_persons)
print("each person should pay : ",round(person_share,2), "Rupees")
print("Thank you, have a great day")