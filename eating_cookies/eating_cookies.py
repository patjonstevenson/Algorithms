#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
# cache = {}
def eating_cookies(n, cache=None):
  # ways = 0
  # print(f'n: {n}')
  if n == 0:
    # print("\nn == 1 or n == 0\n")
    return 1
  elif n < 0:
    # print("\nn < 0\n")
    return 0
  elif cache and cache[n] > 0:
    return cache[n]
  else:
    if cache is None:
      cache = {}
      # print(cache)
    ways = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    cache[n] = ways
    # print(cache)
    return ways

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are only {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')