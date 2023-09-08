"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730508421"

"""Prompting for Inputs"""

five_character_word: str = input("Enter a 5-character word: ")
if len(five_character_word) != 5:
    print("Error: Word must contain 5 characters.")
    exit()

single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + single_character + " in " + five_character_word)

"""Checking Indices"""
# Initialize the string I want to count
word_string = str(five_character_word)
# Initialize my counter for number of character found
number_of_character: int = 0

if word_string[0] == single_character:
    number_of_character = number_of_character + 1
    print(single_character + " found at index 0")

if word_string[1] == single_character:
    number_of_character = number_of_character + 1
    print(single_character + " found at index 1")

if word_string[2] == single_character:
    number_of_character = number_of_character + 1
    print(single_character + " found at index 2")

if word_string[3] == single_character:
    number_of_character = number_of_character + 1
    print(single_character + " found at index 3")

if word_string[4] == single_character:
    number_of_character = number_of_character + 1
    print(single_character + " found at index 4")

"""Counting Matching Indices"""
if int(number_of_character) == 0:
    print("No instances of " + single_character + " found in " + five_character_word)

if int(number_of_character) == 1:
    print(str(number_of_character) + " instance of " + single_character + " found in " + five_character_word)

if int(number_of_character) > 1:
    print(str(number_of_character) + " instances of " + single_character + " found in " + five_character_word)