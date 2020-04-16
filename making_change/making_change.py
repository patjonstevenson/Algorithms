#!/usr/bin/python

import sys

def making_change(amount, denominations, cache=None):
    if amount == 0:
        return 1
    elif amount < 0:
        return 0
    elif cache and cache[amount] > 0:
        return cache[amount]
    else:
        if cache is None:
            cache = {n: 0 for n in range(1, amount+1)}
            cache[0] = 1
        ways = 0
        used = []
        for denom in denominations:
            if denom <= amount:
                ways += making_change(amount - denom, [den for den in denominations if den not in used])
                used.append(denom)
        cache[amount] = ways
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