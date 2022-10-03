rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choice = [rock, paper, scissors]
user_choice = int(input("Welcome to the Rock, Paper, Scissor game! Select 0 for Rock, 1 for Paper, and 2 for Scissor."))
if user_choice >= 3 or user_choice < 0:
  print("Read the instruction! You died!")
  exit()
else:  
  print(choice[user_choice])


computer_choice = random.randint(0,2)
print(choice[computer_choice])



if (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2):
  print("You lose!")

if user_choice == computer_choice:
  print("It's a tied!")
else:
  print("You win!")
  
