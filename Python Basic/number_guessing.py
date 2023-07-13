import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

natural_number =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100,]

choosed_number = random.choice(natural_number)
print(f"psst, correct answer is {choosed_number}")
EASY_LEVEL_ATTEMPT =8
HARD_LEVEL_ATTEMPT =4
difficulty_level = input("Choose a difficulty level. Type'easy' or 'hard': ")
if difficulty_level == "easy":
     print(f"you have {EASY_LEVEL_ATTEMPT} attempts remaing to guess the number.")
    
else:
     print(f"you have {HARD_LEVEL_ATTEMPT} attempts remaing to guess the number.")

#********************************************** USING FUNCTION *****************************************************************

def game():
    player_guess = int(input("Make a guess: "))
    if difficulty_level == "easy":
        attempts = EASY_LEVEL_ATTEMPT
    if difficulty_level == "hard":
        attempts =HARD_LEVEL_ATTEMPT
  
    if player_guess == choosed_number:
        print(f"you got it! The answer was {player_guess}")
    
    else:
        while attempts >= 1 and player_guess != choosed_number:
           
            if player_guess > choosed_number:
                print("Too high")    
            if player_guess < choosed_number:
                print("Too low")
            attempts-=1
            if attempts == 0:
                print("You are out of turns, you Loose")
                break
            print("Guess again")
            print(f"You have {attempts} attempts remaing to guess the number")  
            player_guess = int(input("Make a guess: "))
            if player_guess == choosed_number:
                print(f"you got it! The answer was {player_guess}")
game()

# ************************************************* USING IF ELSE WHILE ****************************************************************

# if difficulty_level == "easy":
#     attempts = EASY_LEVEL_ATTEMPT
# if difficulty_level =="hard":
#     attempts = HARD_LEVEL_ATTEMPT
# player_guess = int(input("Make a guess: "))

# while attempts >= 1:
    
#     if player_guess == choosed_number:
#         print(f"you got it! The answer was {player_guess}")
#         break       
#     else:
#             if player_guess > choosed_number:
#                 print("Too high")    
#             if player_guess < choosed_number:
#                 print("Too low")
#             attempts-=1
#             if attempts == 0:
#                 print("You are out of turns, you Loose")
#                 break
#             print("Guess again")
#             print(f"You have {attempts} attempts remaing to guess the number")
#             player_guess = int(input("Make a guess: "))
    
# ********************************************************************************************************************************************  

# TO EXIT A DEFINED FUNCTION WE CAN USE "RETURN" STATEMENT. 
