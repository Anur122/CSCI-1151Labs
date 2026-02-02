"""
Program Name: Lab 3 Part 2 – Add to a List
Author: Abdullahi Nur
Purpose: Import a list from Part 1, add additional items,
and print the list in reverse alphabetical order.
Starter Code Info: None
Date: 2/2/26
"""

from Lab3_anur31_list import cars

cars.append('KIA')
cars.append('jeep')
cars.append('volkswagen')
cars.append('lexus')
cars.append('bmw')
print(cars)

cars.sort(reverse=True)
print(cars)