# ################################SCOPE##############################

# enemies = 1

# def increase_enemy():
#     enemies = 2
#     print(f"enemies inside finction: {enemies}") 

# increase_enemy()
# print(f"enemies outside function: {enemies}")

# # Local Scope              Local variable is available for only defination block

# # def drink_potion():
# #     potion_strength = 2
# #     print(potion_strength)

# # drink_potion()

# # print(potion_strength)

# # GLOBAL SCOPE         Global variable are available for all part of code

# player_health = 10
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#     print(player_health)

# drink_potion()


# game_level = 3

# enemies = ['Skeleteon', 'Zombie', 'Alien']
# if game_level <5:
#     new_enemy = enemies[0]

# print(new_enemy)

# game_level = 3
# def create_enemy():

#     enemies = ['Skeleteon', 'Zombie', 'Alien']
#     if game_level <5:
#         new_enemy = enemies[0]

# print(new_enemy)                   # THIS WILL GIVE ERROR

# enemies = 1

# def increase_enemy():
#     # global enemies #----------> "global enemies" will allow us to modify our global variable. This is not recommended
#     enemies = 0      #--------->  """ This is the correct way to modify global variable """
#     enemies += 2 
#     print(f" enemies inside funcction: {enemies}")
#     return enemies

# enemies = increase_enemy()
# print(f"enemies outside function: {enemies}")


# """These two enemies variable are entirely different
# first enemy variable is global variable
# second enemy vaariable is local variable"""

#***************************CONSTANTS*******************

# PI = 3.14
# URL = "www.google.com"
