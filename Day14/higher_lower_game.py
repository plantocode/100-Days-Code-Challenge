from art import logo
from art import vs
import random
from game_data import data
from replit import clear

GAME_STATUS = True

print(logo)
choice_a = data[random.choice(range(0,(len(data)+1)))]

current_score = 0

while GAME_STATUS  == True:
    print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")
    print(vs)
    choice_b = data[random.choice(range(0,(len(data)+1)))]
    print(f"Compare B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")
    
    user_response = input("Who has more follower? Type 'A' or 'B': ").lower()

    if choice_a['follower_count'] > choice_b['follower_count']:
        winner = "a"
    else:
        winner = "b"
    
    if user_response != winner:
        clear()
        print(logo)
        print(f"Sorry that's wrong! Final score: {current_score}")
        GAME_STATUS = False
    
    else:
        current_score += 1
        clear()
        print(logo)
        print(f"You're right! Current score: {current_score}.")
        choice_a = choice_b
        
       
    
    
    

