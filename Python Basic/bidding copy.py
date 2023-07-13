import os
from bidding_art import logo
print(logo)


highest_bid = 0
bid ={}

a = True
while a:
    name = input("Enter th ename of bidder: ")
    bidprice = int(input("Enter the bid price: "))
    bid[name]= bidprice
    user_input = (input(("Are there any other bidder? Type 'Yes' or 'No'")))
    
    if user_input == "Yes".lower():
        os.system('CLS')
    else:
        a = False

for key in bid:
    if bid[key] > highest_bid:
        highest_bid = bid[key]
        winner = key
print(f"The winner is {winner} with a highwst bid of ${highest_bid}")
print(bid)
        
            
    


