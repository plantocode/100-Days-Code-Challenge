#1. Create a greeting for your program.
greeting = "Welcome to the Band Name Generator."
print(greeting)

#2. Ask the user for the city that they grew up in.
#by putting the "\n" after the string prior to " indicate the input to be on another line
#print(input("What's the name of the city you grew up in?\n"))
question1 = "What's the name of the city you grew up in?\n"
answer1 = input(question1)
print(answer1)

#3. Ask the user for the name of a pet.
question2 = "What is the name of your pet?\n"
answer2 = input(question2)
print(answer2)

#4. Combine the name of their city and pet and show them their band name.
band_name = answer1 + " " + answer2
print("Your band name could be " + band_name + ".")

#5. Make sure the input cursor shows on a new line, see the example at:
