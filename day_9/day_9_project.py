#Secret Auction Program

import os
import art

bids = {}
maxBidder = ""
maxBid = 0
flag = True

print(art.logo)
print("Welcome to the secret auction program.")

while flag == True:

    name = input("What is your name?: ")
    bidAmount = int(input("What's your bid?: "))

    bids[name] = bidAmount

    otherBidders = input("Are there any other bidders? Type 'yes' or 'no'")
    if otherBidders == 'no':
        flag = False

    os.system('cls')

for name in bids:
    if bids[name] > maxBid:
        maxBidder = name
        maxBid = bids[name]

print(f"The winner is {maxBidder} with a bid of ${maxBid}")