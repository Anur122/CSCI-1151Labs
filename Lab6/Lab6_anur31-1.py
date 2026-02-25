"""
Program Name: User Login System
Author: Abdullahi Nur
Purpose: Simulate a login system using a dictionary of usernames and passwords.
Starter Code: None
Date: 02/24/2026
"""

users = {
    "guest": "guest",
    "gwalters": "S3curePass!",
    "admin": "Admin123",
    "anur31": "pass123"
}

username = input("Enter username: ")

if username not in users:
    print("\nUser not found. Exiting.")
else:
    tries = 3

    while tries > 0:
        password = input("Enter password: ")

        if password == users[username]:
            if username == "guest":
                print("\nWelcome, guest. You have Guest access.")
            else:
                print("\nWelcome,", username + ".", "You have Security Level 1.")
            break
        else:
            tries = tries - 1
            if tries > 0:
                print("Access Denied. Try again.")
            else:
                print("\nToo many failed attempts. Account locked.")