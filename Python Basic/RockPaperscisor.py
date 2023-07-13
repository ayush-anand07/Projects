import random
list = ["Rock", "Paper", "Scissors"]
Rock = ''' 
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----" '''

Paper = '''
..................
..................                
..................
..................              
'''

scissors = '''  
 _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\' '''

user_input = int(input("What do you choose? Type 0 for Rocks, 1 for Paper or 2 for  Scissors."))
# a = len(list)
computer_chose = random.randint(0, 2)
if user_input >= 3 or user_input< 0 :
    print("invalid choice")


if user_input == 0:
    print(Rock)
    if computer_chose == 1:
        print("computer choose:\n" )
        print(Paper)
        print("Computer Won")
    elif computer_chose == 2:
        print("computer choose:\n" )
        print(scissors)
        print("Player Won")



if user_input == 1:
    print(Paper)
    if computer_chose == 0:
        print("computer choose:\n" )
        print(Rock)
        print("Playe Won")
    elif computer_chose == 2:
        print("computer choose:\n" )
        print(scissors)
        print("Computer Won")


if user_input == 2:
    print(scissors)
    if computer_chose == 0:
        print("computer choose:\n" )
        print(Rock)
        print("Computer Won")
    elif computer_chose == 1:
        print("computer choose:\n" )
        print(Paper)
        print("Player Won")

if user_input == computer_chose:
    if user_input and computer_chose == 0:
        print("Player chose:\n")
        print(Rock)
        print("Computer chose:\n")
        print(Rock)
    if user_input and computer_chose == 1:
        print("Player chose:\n")
        print(Paper)
        print("Computer chose:\n")
        print(Paper)
    if user_input and computer_chose == 0:
        print("Player chose:\n")
        print(scissors)
        print("Computer chose:\n")
        print(scissors)
