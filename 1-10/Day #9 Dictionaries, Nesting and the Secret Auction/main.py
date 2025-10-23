import art

print(art.logo)
auction_participants = {}
keep_asking = True
winner = {
    "name" : '',
    "bid" : 0
}

while keep_asking:
    name = input('What is your name?: ')
    bid = int(input('What is your bid?: $'))
    auction_participants[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")

    if more_bidders == "no":
        keep_asking = False
    print('\n' * 100)

for bidder in auction_participants:
    bid = auction_participants[bidder]
    if bid > winner["bid"]:
        winner["name"] = bidder
        winner["bid"] = bid

print(f'The winner is {winner["name"]} with a bid of ${winner["bid"]}')