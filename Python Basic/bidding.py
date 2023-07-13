import builtins
import os
from bidding_art import logo
print(logo)

name = input("Enter th ename of bidder: ")
bidprice = int(input("Enter the bid price: "))
highest_bid = 0

bid = [
    {
    "name": name,
    "bidprice": (f"${ bidprice}")
    }
    
]

def new_bidder(n_name, b_bidprice):
    new_member = {
        "name": name,
        "bidprice":f"${bidprice}"     
    }
    bid.append(new_member)

a = True
while a:
    user_input = (input(("Are there any other bidder? Type 'Yes' or 'No'")))
    os.system('CLS')
    if user_input == "Yes".lower():
        name = input("Enter th ename of bidder: ")
        bidprice = int(input("Enter the bid price: "))
        new_bidder(n_name = name, b_bidprice= bidprice)    
    else:
        a = False

print(bid)
    


