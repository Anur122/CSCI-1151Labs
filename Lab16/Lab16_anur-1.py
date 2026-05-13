"""
Program Name: Lab16_anur-1.py
Author: Abdullahi Nur
Purpose: This program reads Ohio unemployment data from a CSV file and creates a line graph using matplotlib.
Starter Code: None
Date: 05/12/2026
"""

import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = "OHUR.csv"

dates = []
unemployment_rates = []

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            unemployment_rate = float(row[1])

        except ValueError:
            print("Missing or invalid data")

        else:
            dates.append(current_date)
            unemployment_rates.append(unemployment_rate)

plt.plot(dates, unemployment_rates)

plt.title("Ohio Unemployment (by Month): 1976 - 2022")
plt.xlabel("Date")
plt.ylabel("Unemp Rate")

plt.gcf().autofmt_xdate()

plt.savefig("ohio_unemployment.png")

plt.show()