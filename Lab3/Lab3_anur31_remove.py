"""
Program Name: Lab 3 Part 4 – Remove an Item from a List
Author: Abdullahi Nur
Purpose: Import a list, remove the item 'binoculars',
print the updated list, and display the total number of items.
Starter Code Info: None
Date: 2/2/26
"""

from Lab3_anur31_replace import cars

cars.remove('binoculars')
print(cars)

print(f"Total number of items being brought: {len(cars)}")