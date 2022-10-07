from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

auction_status = True
auction = {}
#another way to find winner
def find_winner_bidder():
    highest_bid = 0
    winner = ""
    for bidder in auction:
        bid_amount = auction[bidder]
        #note by doing this, you will need to change the input as an integer for this to work
        if bidding_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
        

while auction_status == True:
    user_name = input("What is your name?").lower()
    bidding_price = input("What is your bid? $")
    auction[user_name] = bidding_price
    status = input("Are there any other bidder? Type 'yes' or 'no'.").lower()
    clear()
    if status == "no":
        auction_status == False
        #using max () to get maximum value key in a dictionary
        find_winner = max(auction, key=auction.get)
        print(f"The winner is {find_winner} with a bid of $ {auction[find_winner]}.")
