#*****************************************XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX********************************************
# print("Wlcome to the Rollercoaster!")
# height = int(input("What is your height?"))
# bill = 0

# if height >120 :
#     print("You can ride the roallercoaster !")
#     age= int(input("Enter your age:"))
#     if age < 12:
#         bill = 5
    
#     elif age <= 18:
#         bill = 7

#     elif age > 45 and age< 55:
#         bill =0 
    
#     else:
#         bill = 12

#     ans = input("Do you want photos? y or n?")
#     if  ans == "y":
#         bill = bill+3
#         print(f"pay $ {bill}")
#     if  ans == "n":
#          print(f"Pay ${bill}")

# else:
#     print("Sorry, you have to grow taller before ypu can ride") 


# ***************************XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX******************************************

# print("Welcome to Python Pizza Delivery!")

# size = (input("What size of pizza do you want? S, M, L ?"))
# add_pepperoni = input("Do you want pepperoni? y or n? ")
# extra_chesse = input(" Do you want extra cheese? y or n?")

# bill = 0
# if size == "S":
#     bill = 15
# if size == "M":
#     bill = 20
# if size == "L":
#     bill = 25
# if add_pepperoni == "y":
#     if size == "S":
#         bill = bill+2
#     if size == "M" or "L":
#         bill = bill+3  
# if extra_chesse == "y":
#     bill = bill+1
    
# print(f"your final bill is ${bill}")

#***************************************XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX*********************************************


name1 = input("Enter your name: ")
name2 = input("Enter you crush's name: ")
 
name1_upper_case = name1.upper()                                                     # variable.lower()--------> converts string into lower case
name2_upper_case = name2.upper()                                                     # variable.upper()--------> converts string into upper case
                                                         # variable.count("element to be counted")--------> gives the count of particular element.

a = name1_upper_case.count( "T") + name2_upper_case.count("T")
b = name1_upper_case.count( "R") + name2_upper_case.count("R")
c = name1_upper_case.count( "U") + name2_upper_case.count("U")
d = name1_upper_case.count( "E") + name2_upper_case.count("E")

total = a+b+c+d

e = name1_upper_case.count( "L") + name2_upper_case.count("L")
f = name1_upper_case.count( "O") + name2_upper_case.count("O")
g = name1_upper_case.count( "V") + name2_upper_case.count("V")
h = name1_upper_case.count( "E") + name2_upper_case.count("E")

total1 = e+f+g+h

a = int((f"{total}{total1}"))
# print(a)
print(f"love score is {total}{total1}")

if (a) <10 or a>90:
    print(f"Your score is {a}, you go together like coke and mentos")

elif a>40 and a< 50:
     print(f"Your score is {a}, you are alright together")

else:
    print(f"your score is {a}")

#***********************************XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX****************************************************


# num = int(input("Enter a number: "))
# if (num%2 == 0):
#     print("Given number is even")
# else:
#     print("Given number is odd")

# print('''*******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
# direction = input("You are at a cross road. Where do ypu want to go? Left or Right ").lower()
# if direction == "right":                                                                         # "str".casefold() ----> makes the string case insensetive 
#     print("Game over")
# elif direction == "left":
#     swim_wait = input('You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.')
#     if swim_wait == "swim":
#         print("Game Over.")
#     else:
#         colour = input("You are at an island unharmed. There is a house with 3 doors. One red, One yellow, and one blue. Which colour do you choose?").lower()
#         if colour == "yellow":
#             print("YOU WIN")
#         elif colour == "red":
#             print("You Entered a room with fires. Game Over")
#         else:
#             print("You entered a room full of beasts. Game Over")