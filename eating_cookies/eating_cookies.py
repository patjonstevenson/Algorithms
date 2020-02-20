#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
cache = {}
def eating_cookies(n, cache=cache):
  ways = 0
  print(f'n: {n}')
  if n == 1 or n == 0:
    print("\nn == 1 or n == 0\n")
    return 1
  elif n < 0:
    print("\nn < 0\n")
    return 0
  elif n in cache:
    return cache[n]
  else:
    for i in range(1, 4)[::-1]:
      print(f"i: {i}")
      print(f'n-i: {n-i}')
      print(f"\nWays before eating_cookies recursion: {ways}\n")
      ways += eating_cookies(n-i)
      print(f"\nWays after eating_cookies recursion: {ways}\n")
  cache[n] = ways
  return ways

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')