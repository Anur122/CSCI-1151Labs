"""
Program Name: UPC Validator
Author: Abdullahi Nur
Purpose: This program asks the user for a 12 digit UPC code and checks
if it is valid by calculating the correct check digit using a function.
Starter Code: None
Date: 03/10/2026
"""

def find_UPC(first11):
    odd_sum = 0
    even_sum = 0

    # add odd position digits
    for i in range(0, 11, 2):
        odd_sum += int(first11[i])

    # add even position digits
    for i in range(1, 11, 2):
        even_sum += int(first11[i])

    total = (odd_sum * 3) + even_sum
    remainder = total % 10

    check_digit = (10 - remainder) % 10

    return check_digit


# input validation
while True:
    upc = input("Enter a 12-digit UPC: ")

    if len(upc) != 12 or not upc.isdigit():
        print("Invalid input. UPC must be exactly 12 digits.\n")
    else:
        break


first11 = upc[:11]
given_digit = int(upc[11])

print("\nThe first 11 digits are '" + first11 + "'.")
print("The provided check digit is '" + upc[11] + "'.")

print("\nCalculating...")

expected_digit = find_UPC(first11)

print("The expected check digit is", expected_digit, ".")

if expected_digit == given_digit:
    print("\nThis is a VALID UPC.")
else:
    print("\nThis is an INVALID UPC.")