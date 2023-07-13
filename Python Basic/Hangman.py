
import random
import hangman_words
import hangman_art
import os

choosen_word = random.choice(hangman_words.word_list)
# print(choosen_word)
display= [ ]
stages = hangman_art.stages
lives =6 

# creates as many spaces in choosen words
for letter in choosen_word:
    display += "_"
print(f"{' '.join(display)}")
# created a condition for loop   
end_of_game = False

print(hangman_art.logo)
# created a loop to run until correct word is guessed

while not end_of_game: 
    guess = input("Guess a letter: ").lower()  
    os.system('CLS')  
    if guess in display:
      print(f"You already guessed {guess}") 
    
    for position in range (len(choosen_word)):  
        letter = choosen_word[position]  
        if letter == guess:
             display[position] = letter
   
    if  guess not in choosen_word:
          print(f"You guessed {guess}, that's not in the word. You loose a life. ")
          lives-= 1
          
          if lives == 0:
            end_of_game = True
            print("You Loose") 
          

    print(f"{' '.join(display)}")
    print(stages[lives])


    if "_" not in display:
       end_of_game = True
       print(" You Win")
    
 
   
    