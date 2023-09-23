"""EX03 - Structured Wordle."""

__author__ = "730508421"

# Part 1: contains_char: declaring the function
def contains_char(search_word: str, char_to_find: str) -> bool:
    """Return True if the single character put is found at any index of the given word."""
    assert len(char_to_find) == 1
    
    search_word_idx: int = 0
    # Loop to test if single character is in strings word
    while search_word_idx < len(search_word):
        if search_word[search_word_idx] == char_to_find:
            return True
        search_word_idx = search_word_idx + 1
    return False