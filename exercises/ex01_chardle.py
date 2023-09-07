"""EX01 - Chardle - A cute step toward Wordle."""

_author_ = "730508421"

"""Prompting for Inputs"""

five_character_word: str = input("Enter a 5-character word: ")
single_character: str = input("Enter a single character word: ")
print("Searching for " + single_character + " in " + five_character_word)

"""Checking Indices"""
# Initialize the string I want to count
word_string = str(five_character_word)
# Initialize my counter for number of character found
num_of_char: int = 0

if word_string[0] == single_character:
    num_of_char = num_of_char + 1
    print (single_character + " found at index 0")

if word_string[1] == single_character:
    num_of_char = num_of_char + 1
    print (single_character + " found at index 1")

if word_string[2] == single_character:
    num_of_char = num_of_char + 1
    print (single_character + " found at index 2")

if word_string[3] == single_character:
    num_of_char = num_of_char + 1
    print (single_character + " found at index 3")

if word_string[4] == single_character:
    num_of_char = num_of_char + 1
    print (single_character + " found at index 4")

"""Counting Matching Indices"""
if int(num_of_char) == 0:
    print ("No instances of " + single_character + " found in " + five_character_word)
else:
    print (str(num_of_char) + " instances of " + single_character + " found in " + five_character_word)