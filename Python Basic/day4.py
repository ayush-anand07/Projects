# Randomisation

import random           #-----> module
# random_integer = random.randint(1, 10)    #random.randint(a, b) will give a random int between a and b, both inclusive.
# print(random_integer)

# #0.0000000000 - 0.9999999999999.....
# random_float = random.random() *5             # will gove a random float between [0, 1)
# print(random_float)                           # we can expand the range of this random float number by multiplying the required number on RHS


# ***********************XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX*******************************

                                         # TOSS

# random_choice = random.randint(0,1)
# if random_choice == 0:
#     print("Heads")

# else:
#     print("Tails")

#************************XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX****************************************************

# LISTS

#  SYNTAX: list name = [item1 ,item2]

# states_of_India = ["Bihar", "Mumbai",  "Jarkhand", "Assam", "Kerla"] 
# print(states_of_India[0])
# states_of_India.append("Karnatka")
# print(states_of_India[0])

# name_strings = input("Enter the name of your friends :")
# name_string_list = name_strings.split(", ")

# a = len(name_string_list)

# random_name = random.randint(0,a-1)
# print(name_string_list[random_name] + " will pay th bill")

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[0][1])
# dirty_dozen[0][1] = "Ayush"
# print(dirty_dozen[0][1])



# row1 = ["1" , "2" , "3"]                     
# row2 = ["4" , "5" , "6"]                    
# row3 = ["7" , "8" , "9"]    
                                           

# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")


# position = input("where do you want to put the treasure? ")

# horizontal = int(position[0]) 
# vertical =   int(position[1])
# map[vertical-1][horizontal-1] = "X"
 
# print(f"{row1}\n{row2}\n{row3}")
