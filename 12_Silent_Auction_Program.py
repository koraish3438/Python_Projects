import os

def winner_bidder(bidder_details):
    highest_bid = 0
    winner = ""
    for bidder in bidder_details:
        bidding_price = bidder_details[bidder]
        if bidding_price > highest_bid:
            highest_bid = bidding_price
            winner = bidder
    print(f"Here is the list of all bidders {bidder_details}")
    print(f"The winner is {winner} with a bid price of {highest_bid}")

bidders_data = {}

print("Silent Auction Program start now!")
wanna_end = False
while not wanna_end:
    name = input("Enter your name : ")
    bid_price = int(input("Enter your bid price : "))

    bidders_data[name] = bid_price

    more_bidders = input("Are there more bidders? Type 'yes' or 'no' : ").lower()
    if more_bidders == "no":
        wanna_end = True
        winner_bidder(bidders_data)
    elif more_bidders == "yes":
        os.system('cls')
    else:
        print("Enter valid input!")
        play_again = input("Do you want to continue...? Type 'yes' or 'no' : ").lower()
        if play_again == "yes":
            os.system('cls')
            wanna_end = False
        else:
            wanna_end = True
            print("Ok! See you later..")