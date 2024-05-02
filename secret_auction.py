from secret_auction_art import logo
print(logo)

def find_highest_bid(bidding_record) :
  highest_bid = 0
  winner  = ""
  #bidding_record = { "Angela" : 123 , "james" : 321 }
  for bidder in bidding_record :
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid :
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
    
bidding_finished = False
while not bidding_finished :
  bids={}
  name=input("What is your name? ")
  price=int(input("What is your bid? $"))
  #adding name and price into dictionary, name as key and price as value
  bids[name]=price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
  if should_continue == "yes" :
    bidding_finished = False
  elif should_continue == "no" :
    bidding_finished = True
    find_highest_bid(bids)

