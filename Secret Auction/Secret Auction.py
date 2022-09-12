#Secret_Auction
from Secret_Auction_art import logo
print(logo)

auction = {}

while True:
  bidding_person = input("What is your name? ")
  bidding_amount = int(input("Bidding Amount : "))
  auction[bidding_person] = bidding_amount
  if input("Is their anyone left? ").lower() == "no":
    break

highest_bid = 0
for bids in auction.values():
  if bids > highest_bid:
    highest_bid = bids

for person in auction:
  if auction[person] == highest_bid:
    print(f"{person} is the winner of the auction with bidding amount {highest_bid}")
