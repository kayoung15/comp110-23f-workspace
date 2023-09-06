"""EX01 - Chardle - A cute step toward Wordle."""

_author_ = "730508421"

"""Prompting for Inputs"""

five_character_word: str = input("Enter a 5-character word: ")
single_character: str = input("Enter a single character word: ")
print("Searching for " + single_character + " in " + five_character_word)