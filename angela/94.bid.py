from replit import clear
# HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while bidding_finished == False:
    name = input("what is your name?:")
    price = int(input("what is your bid?:$"))
    bids[name] = price
    should_bidder = input("Are there any other bidders?\n ")

    if should_bidder == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_bidder == "yes":
        clear()



