############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

card_name = {
    "jack":  10        ,
    "king":  10       ,
    "queen": 10,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "ace": 11,
}

game_is_on = True
while game_is_on:
   
    if input("Do you want to play a game of Blackjack? Type'y' or 'n' ") == "y":
        computer_first_card = random.choice(cards)
        player_card = random.choices(cards, k = 2 )
        current_score = sum(player_card)
        print(f"Computer's first card : {computer_first_card}")
        print(f'Your Cads: {player_card} , current score = {current_score}')
    
        a =True
        while a: 
            another_card = input("Type 'y' to get another card , type'n' to pass: ")

            if another_card == "y":
                new_player_card = random.choice(cards)
                player_card.append(new_player_card)
                player_final_score = sum(player_card)
                print(f'Your card: {player_card} , current score = {player_final_score}')
                print(f"Computer's first card : {computer_first_card}")
                
                if player_final_score >21:
                    print("you loose")
                    break
        
        
            if another_card == "n":   
                player_final_score = sum(player_card)
                computer_card_list = [computer_first_card]
                new_computer_card = random.choice(cards)
                computer_card_list.append(new_computer_card)
                # print(computer_card_list)
                computer_final_score = sum(computer_card_list)
                
                if computer_final_score < 17:
                    new_computer_card = random.choice(cards)
                    computer_card_list.append(new_computer_card)
                    # print(computer_card_list)
                    computer_final_score = sum(computer_card_list)
                    print(f'Your final hand: {player_card} , final score = {player_final_score}')
                    print(f"Computer's final hand : {computer_card_list}, final score: {computer_final_score}")
                
                    if player_final_score < computer_final_score and computer_final_score <21:
                        print("You Loose")
                        break
                    if player_final_score == computer_final_score :
                        print("Draw")
                        break
                    
                    elif player_final_score == 21:
                        print("Player Win with a blackjack")
                        break
                    elif computer_final_score == 21:
                        print("computer win with a Blackjack")
                        break
                    
                    elif computer_final_score >21:
                        print("you won")
                        break

                    elif player_final_score >21:
                        print("you loose")
                        break
                
                    else:
                        print("you won")
                        break
                        
                print(f'Your final hand: {player_card} , final score = {player_final_score}')
                print(f"Computer's final hand : {computer_card_list}, final score: {computer_final_score}")

                if player_final_score < computer_final_score and  computer_final_score <21:
                    print("You Loose")
                    a = False
                
                if player_final_score == computer_final_score :
                    print("Draw")
                    a =False


                elif player_final_score == 21:
                    print("Player Win with a blackjack")
                elif computer_final_score == 21:
                    print("computer win with a Blackjack")
                
                elif computer_final_score >21:
                    print("you won")
                    a = False
                
                elif player_final_score >21:
                    print("You loose")
                    a= False
                # else:
                #     print("you won")
                #     a= False
    else:
        game_is_on = False
        

    







