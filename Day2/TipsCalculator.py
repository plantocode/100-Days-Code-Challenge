#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

welcome_message = "Welcome to the tip calculator."
print (welcome_message)

total_bill = int(input("What was the total bill? $"))
print(total_bill)

percent_tip = (int(input("What percentage tip would you like to give? 10, 12, or 15?"))/100)
print(percent_tip)

number_people = int(input("How many people to split the bill?"))
print(number_people)

per_person_bill = total_bill * (1+ percent_tip) / number_people 
round_per_person_bill = "{:.2f}" . format(round(per_person_bill, 2))

print(f"Each person should pay: ${round_per_person_bill}.")
