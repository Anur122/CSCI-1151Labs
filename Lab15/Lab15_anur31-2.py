"""
Program Name: Lab15_anur-2.py
Author: Abdullahi Nur
Purpose: This program creates two plots using matplotlib. One plot shows the first 5 cubic numbers, and the other shows the first 5000 cubic numbers.
Starter Code: None
Date: 05/05/2026
"""

import matplotlib.pyplot as plt

x_values_5 = [1, 2, 3, 4, 5]
y_values_5 = [1, 8, 27, 64, 125]
plt.plot(x_values_5, y_values_5)

plt.title("First 5 Cubes")
plt.xlabel("Value")
plt.ylabel("Cube of Value")

plt.savefig("cubes_5.png")
plt.clf()

x_values_5000 = list(range(1, 5001))

y_values_5000 = []
for x in x_values_5000:
    y_values_5000.append(x**3)

plt.plot(x_values_5000, y_values_5000)

plt.title("First 5000 Cubes")
plt.xlabel("Value")
plt.ylabel("Cube of Value")

plt.savefig("cubes_5000.png")