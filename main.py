# start to python day-11 code
# starting code is basics learned
# main project code at end

# Author: Rushikesh Dikey
# Date: 27-03-2022
# went on vacation
import math
import os
from time import sleep
# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
screen_clear()
# The secret auction program
bids = {}
bidding_finished = False

def find_highest_bidder(bidder_record):
    highest_bid = 0
    winner = ""
    for bidder in bidder_record:
        bid_amount = bidder_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} and highest bid is {highest_bid}")
while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("What is your bid ₹"))
    bids[name] = price
    done = input("Do you want to continue Yes or No? ").lower()
    if done == 'no':
        bidding_finished = True
    elif done == 'yes':
        screen_clear()

print(bids)
find_highest_bidder(bids)
