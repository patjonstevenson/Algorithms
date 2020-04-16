#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  max_batches = math.inf
  for ingred in recipe:
    if ingred not in ingredients:
      return 0
    elif recipe[ingred] > ingredients[ingred]:
      return 0
    else:
      batches = ingredients[ingred] // recipe[ingred]
      if batches < max_batches:
        max_batches = batches
  return max_batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))