print("Welcome to the tip Calculator.")
bill = float(input("What was the total bill? $"))
tip= int(input("What percentage tip would you like to give? 10, 12, or 15?"))
number_of_person = int(input("How many people to split the bill?"))

bill = bill + (tip/100)*bill  # or, bill = bill*(1+tip/100)

split = round(bill/number_of_person, 2)
split = "{:.2f}".format(split)                # format specifier 
print(f"Each Person should pay : ${split}")

