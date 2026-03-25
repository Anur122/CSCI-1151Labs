"""
Program Name: Coin Class
Author: Abdullahi Nur
Purpose: Represents a coin that can be tossed.
Starter Code: None
Date: 03/24/2026
"""

import random

class Coin:
    def __init__(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def get_sideup(self):
        return self.__sideup