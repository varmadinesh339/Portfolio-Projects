

bids = {}

status_bid = False
while not status_bid:
    name = input("What is your Name? ")
    bid_amount = int(input("What is your bid amount? "))
    bids[name] = bid_amount
    choice = input("Do You have more bidders 'yes' or 'no'")
    choice = choice.lower()

    if choice == 'no':
        status_bid = True
    elif choice == 'yes':
        print('\033c',end ='')

high_amount = 0

winner = ""
for bidder in bids:
    bid_amount = bids[bidder] 
    if bid_amount   >  high_amount:
        high_amount = bid_amount
        winner = bidder

print(f"The winner is {winner} with the highest bid amount is {high_amount}")