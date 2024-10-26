from art import logo

list_bids = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for name in bidding_record:
        if bidding_record[name] > highest_bid:
            highest_bid = bidding_record[name]
            winner = name

    print(f"The winner is {winner} with a bid of ${highest_bid}")

def handle_bid():
    print(logo)
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))

    list_bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == 'yes':
        print("\n" * 20)
        handle_bid()
    else:
        find_highest_bidder(list_bids)

handle_bid()

