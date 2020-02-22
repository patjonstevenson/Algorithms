#!/usr/bin/python

import sys
from collections import namedtuple
from functools import reduce

Item = namedtuple('Item', ['index', 'size', 'value'])

def sum_items_capacity(items):
  return reduce(lambda x,y: x + y[1], items, 0)

def knapsack_solver(items, capacity):
  # # if not items:
  # #   return 
  # sorted_items = sorted(items, key=lambda x: x[2], reverse=True)
  # print(f"Sorted items: {[item[2]/item[1] for item in sorted_items]}")
  # selected = []
  # remaining_capacity = capacity
  # value = 0
  # i = 0
  # while remaining_capacity and i < len(sorted_items):
  #   if remaining_capacity - sorted_items[i][1] >= 0:
  #     selected.append(sorted_items[i])
  #     remaining_capacity -= sorted_items[i][1]
  #     value += sorted_items[i][2]
  #   i += 1
  # return {'Value': value, 'Chosen': [item[0] for item in selected]}
  if not items:
    return items
  elif sum_items_capacity > capacity:
    return 
  else:
    return
  

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')