"""
Program Name: Restaurant Tip Calculator (Lab 2 - Option 1)
Author: Abdullahi Nur
Purpose: Prompts the user for a dinner bill total, then calculates and displays 15% and 20% tip suggestions and the totals with each tip.
Starter Code Info: None
Date: January 27, 2026
"""

print("This program will calculate tip suggestions (15% and 20%) based on your dinner bill total.\n")

bill_total = float(input("Enter the total dinner bill amount: $"))

tip_15 = bill_total * 0.15
tip_20 = bill_total * 0.20

total_with_15 = bill_total + tip_15
total_with_20 = bill_total + tip_20

print(f"\nSuggested 15% tip: ${tip_15:.2f}")
print(f"Total with 15% tip: ${total_with_15:.2f}")

print(f"\nSuggested 20% tip: ${tip_20:.2f}")
print(f"Total with 20% tip: ${total_with_20:.2f}")
