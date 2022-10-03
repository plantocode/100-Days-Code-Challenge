print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

first_choice = input("You are at a cross walk, would you like to left or right? L or R\n")
if first_choice == "L":
  second_choice = input("You came to the river, would you wait for a boat or swim across the river? Wait or Swim\n")
  if second_choice == "Wait":
      third_choice = input("You came across three doors: red, yellow, blue. Which one will you choose? R, Y or B\n")
      if third_choice == "Y":
        print("YOU WIN!!!")
      else:
        print("Yout got burned and died! Haha!")
  else:
    print("The alligator ate you!")
else:
  print("You got shot by the ranger!")


print('''
                      _       _ 
                     (_)     (_)
  __ _  ___ _ __ ___  _ _ __  _ 
 / _` |/ _ \ '_ ` _ \| | '_ \| |
| (_| |  __/ | | | | | | | | | |
 \__, |\___|_| |_| |_|_|_| |_|_|
  __/ |                         
 |___/                          

''')
