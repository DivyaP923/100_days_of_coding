cost = float(input("whats your bill amount? "))
tip_percent = int(input("how much do you want to tip 0, 5, 10? "))
number_of_persons = int(input("how many people do we need to split the bill with: "))
cost_tip = (cost*float(tip_percent/100))+cost
total_cost = cost_tip/float(number_of_persons)
print("your total cost would be: ",total_cost, "Rupees")