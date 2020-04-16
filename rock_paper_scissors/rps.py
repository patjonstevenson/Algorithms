#!/usr/bin/python

import sys

def build_list(n, arr):
  if n == 0:
    return [[]]
  elif n == 1:
    return arr
  else:
    new_arr = []
    for possibility in arr:
      new_arr = new_arr + [possibility + ['rock']] + [possibility + ['paper']] + [possibility + ['scissors']]
    # print(new_arr)
    return build_list(n-1, new_arr)

def rock_paper_scissors(n):
  return build_list(n, [['rock'], ['paper'], ['scissors']])



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')