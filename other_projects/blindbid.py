def add_bidder(bidder_name, bidder_bid):
    new_bidder = {"name": bidder_name, "bid": bidder_bid}
    bidders.append(new_bidder)


def find_max(bidders_bid):
    name_winner = ""
    bid_winner = 0
    biggest_bid = 0
    for bidder in bidders_bid:
        if bidder["bid"] > biggest_bid:
            biggest_bid = bidder["bid"]
            name_winner = bidder["name"]
            bid_winner = bidder["bid"]

    print(f"The winner is {name_winner} that bid exactly ${bid_winner}")


import logo

print(logo.logo_bid)

bidders = []
answer = None

while answer != 'n':
    name = input("What is your name?")
    bid = int(input("How much do you want to bid?: $"))
    add_bidder(name, bid)

    restart = input("Is there somebody else who is willing to participate? | yes - 'y' | no - 'n': \n")
    if restart == 'n':
        break

find_max(bidders)