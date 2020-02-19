#!/usr/bin/python

import sys

def making_change(amount, denominations):
    ways = 0
    print(F"\nAmount: {amount}")
    for denomination in denominations[::-1]:
        print(f"Denomination: {denomination}")
        rem = amount % denomination
        print(f"Remainder: {rem}")
        [denom, *rest] = denominations
        if not rest:
            return ways
        elif rem:
            return ways + making_change(rem, rest)
            # print(f"Number of ways in if: {ways}")
        else:
            print("In else")
            ways += 1
            print(f"Number of ways in else: {ways}")
            print(amount/denomination + 1)
            for j in range(1, int(amount/denomination + 1)):
                new_amount = amount - j * denomination
                print(f"New Amount: {new_amount}")
                ways += making_change(new_amount, rest)
                print(f"Ways: {ways}")
    return ways

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")