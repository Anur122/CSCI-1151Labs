"""
Program Name: Word Analyzer
Author: Abdullahi Nur
Purpose: This program allows the user to select one of four text files,processes the file, and displays a word frequency report using OOP.
Starter Code: None
Date: 03/31/2026
"""

from pathlib import Path
import string


class WordAnalyzer:
    def __init__(self, filepath):
        self.__filepath = Path(filepath)
        self.__frequencies = {}

    def process_file(self):
        try:
            if not self.__filepath.exists():
                raise FileNotFoundError

            translator = str.maketrans('', '', string.punctuation)

            with self.__filepath.open('r', encoding='utf-8') as file:
                for line in file:
                    line = line.translate(translator)
                    line = line.lower()
                    words = line.split()
                    for word in words:
                        if word in self.__frequencies:
                            self.__frequencies[word] += 1
                        else:
                            self.__frequencies[word] = 1

            return True

        except FileNotFoundError:
            print("Error: File not found.")
            return False

    def print_report(self):
        words = sorted(self.__frequencies.keys())
        print()
        for word in words:
            print(f"{word:<10} :: {self.__frequencies[word]}")
        print()


def main():
    lab_folder = Path(r"C:\Users\Abdul\Documents\CSCI1151\PythonLabs\CSCI-1151Labs\Lab10")

    files = {
        "1": lab_folder / "princess_mars.txt",
        "2": lab_folder / "monte_cristo.txt",
        "3": lab_folder / "tarzan.txt",
        "4": lab_folder / "treasure_island.txt"
    }

    file_names = {
        "1": "Princess Mars",
        "2": "Monte Cristo",
        "3": "Tarzan",
        "4": "Treasure Island"
    }

    while True:
        print("\n--- Word Analyzer ---")
        print("Please select a file to analyze:")

        for key in file_names:
            print(f"{key}. {file_names[key]}")

        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "5":
            print("\nGoodbye!")
            break
        elif choice in files:
            filepath = files[choice]
            print(f"\nProcessing '{filepath.name}'...\n")
            analyzer = WordAnalyzer(filepath)
            success = analyzer.process_file()
            if success:
                analyzer.print_report()
        else:
            print("\nInvalid choice. Please select from 1-5.")

        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()