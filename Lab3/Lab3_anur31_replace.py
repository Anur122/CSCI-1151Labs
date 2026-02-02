"""
Program Name: Lab 3 Part 3 – Replace an Item in a List
Author: Abdullahi Nur
Purpose: Import a list, replace one item with 'binoculars',
and display parts of the list using slice notation.
Starter Code Info: None
Date: 2/2/26
"""
from Lab3_anur31_add import cars

cars[3] = "binoculars"
print(cars)

binoculars_index = cars.index("binoculars")

print(cars[:binoculars_index])

print(cars[binoculars_index])

print(cars[binoculars_index + 1:])