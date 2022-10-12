#can not used "return" unless it is in a function
import random
from art import logo
from replit import clear
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
def sum_hand(num1):
    return (sum(num1))

def have_blackjack(num1):
    if sum(num1) == 21 and len(num1) == 2:
       return True

#Step 1: input
def blackjack():
    print(logo)
    sum_user_hand = 0
    sum_dealer_hand = 0
    user_hand = random.choices(deck, k=2)
    print(f"Your hand is {user_hand}.")

    sum_user_hand = sum_hand(user_hand)
    print (f"Your hand total is {sum_user_hand}")

    dealer_hand = random.choices(deck, k=2)
    print(f"The dealer hand is {dealer_hand[0]}.")

    if have_blackjack(dealer_hand) == True:
        print("Dealer has BlackJack. You lose!")
        return
        
    elif have_blackjack(user_hand) == True:
        print ("You won with Black Jack!")
        return
            
    player_continue = (input("Type 'y' to get another card, 'n' to pass.")) 
    while player_continue == "y" :
        new_card = random.choice(deck)
        user_hand.append(new_card)
        sum_user_hand = sum_hand(user_hand)
        if new_card == 11 and sum_user_hand > 21:
            sum_user_hand -= 10
            
        if sum_user_hand > 21:
            print ("You lose!")
            return
        print (f"Your hand is {user_hand} and current score: {sum_user_hand}")
        player_continue = (input("Type 'y' to get another card, 'n' to pass."))
        
    sum_dealer_hand = sum_hand(dealer_hand)

    while sum_dealer_hand < 17:
        dealer_hand.append(random.choice(deck))
        sum_dealer_hand = sum_hand(dealer_hand)
        print (f"Dealer hand is {dealer_hand} and current score: {sum_dealer_hand}")

    if sum_dealer_hand > 21:
        print("You win!")
    elif sum_user_hand > sum_dealer_hand:
        print("You win!")
    elif sum_user_hand == sum_dealer_hand:
        print("It's a draw!")
    else:
        print("You lose!")
        
play = input("Would you like to play a game of Black Jack? Enter 'y' to play and 'n' to stop.")
while play == "y":
    blackjack()
    play = input("Would you like to play a game of Black Jack? Enter 'y' to play and 'n' to stop.")
    clear()



    
    
        
    
    
        
    

        
    
    


