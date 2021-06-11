from replit import clear
from art import logo3

print(logo3)

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    # bidding_record[name] = price
    # print(bidding_record)
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

cor = ["yes", "no"]

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    print(bids)
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    while should_continue not in cor:
        print("Please insert correct operation")
        should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":

        bidding_finished = True
        # find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()


bids = {
    "Angela": 123,
    "James": 321
}

# find_highest_bidder(bidding_record)

find_highest_bidder(bids)