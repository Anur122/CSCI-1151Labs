"""
Program Name: Pick Up Sticks
Author: Abdullahi Nur
Purpose: Two players take turns picking up 1 to 4 sticks.
Whoever takes the last stick wins.
Starter Code: None
Date: 02/17/2026
"""

sticks = 13
player = 1

print("Welcome to Pick Up Sticks.")
print("There are 13 sticks.")
print("You can take 1 to 4 sticks.")
print("Whoever takes the last stick wins.")
print()

while sticks > 0:

    print("There are", sticks, "sticks left.")
    print("Player", player)
    
    take = int(input("How many sticks will you take? "))

    while take < 1 or take > 4 or take > sticks:
        print("That is not allowed.")
        take = int(input("Try again: "))

    sticks = sticks - take
    print()

    if sticks == 0:
        print("Player", player, "wins!")
        break

    if player == 1:
        player = 2
    else:
        player = 1

input("Press Enter to exit.") 