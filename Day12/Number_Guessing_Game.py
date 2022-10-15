#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
print(logo)

import random
secret_number = random.randrange(1, 101)

print("Welcome to the Number Guessing Game!")

difficulty_level = input("Please input the difficulty level: 'easy' or 'hard'.").lower()

def max_number_turns():
    if difficulty_level == "hard":
        number_turns = 5
    else:
        number_turns = 10
    return number_turns

def winner():
    if guess_number == secret_number:
        print("You win!")
        return

number_turns = max_number_turns()
game_status = True

while game_status == True:
    guess_number = int(input("Please guess a number from 1 to 100. "))
    if guess_number != secret_number:
        if guess_number > secret_number:
            print("Too high")
        else:
            print("Too low")
        number_turns -= 1
        if number_turns > 0:
            print(f"You have {number_turns} turn(s) left.")
        else:
            print("You have run out of turn. Game over!")
            game_status = False
            
    else:
        print(f"You win. The correct answer is {secret_number}.")
        game_status = False
   


