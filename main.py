from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")
bidders = {}
bidding_finished = False

while not bidding_finished:
  name=input("What is your name?: ")
  price=int(input("What's your bid?: $"))
  bidders[name]=price
  should_continue=input("Are there any other bidders? Type 'yes' or 'no'.\n")
  clear()
  if should_continue=="no":
    bidding_finished=True
    find_highest_bidder(bidders)
    
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}") 