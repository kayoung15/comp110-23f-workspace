"""EX03 - Structured Wordle."""

__author__ = "730508421"

# Part 1: contains_char: declaring the function
def contains_char(search_word: str, char_to_find: str) -> bool:
    """Return True if the single character put is found at any index 
    of the given word."""
    assert len(char_to_find) == 1
    search_word_idx = 0

# Loop to test if single character is in strings word
    while search_word_idx < len(search_word):
        if search_word[search_word_idx] == char_to_find:
            return True
        search_word_idx = search_word_idx + 1
    return False

# Part 2: emojified
def emojified(guess: str, secret: str) -> str:
    """Will Emojify Player's Guess based on if character in guess word 
    matches secret word"""
    assert len(guess) == len(secret)
    
    # Emoji Constants
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    
    # Establishing index and result string
    guess_idx: int = 0
    result = str("")
    
    #Loop to create result string
    while guess_idx < len(secret):
        if guess[guess_idx] == secret[guess_idx]:
            result = result + GREEN_BOX
        elif contains_char(secret, guess[guess_idx]):
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX
        guess_idx = guess_idx + 1
    
    return result

# Part 3: input_guess
def input_guess(expected_len: int) -> str:
    """Given an integer “expected length” of a guess as a parameter, 
    it will prompt the user for a guess and continue prompting them until 
    they provide a guess of the expected length"""

    # Prompt the user to enter their guess
    guess_word: str = str(input(f'Enter a {expected_len} character word? '))

    # Response to Player Input
    while len(guess_word) != expected_len:
        guess_word = str(input(f'That was not {expected_len} chars! Try again: '))
    return guess_word

# Part 4: main
def main() -> None:
    """The entrypoint of the game and main game loop."""

    # Establishing variable needed to be tracked of
    secret_word: str = "codes"
    number_of_tries: int = 1
    max_tries: int = 6
    guess_word: str = ""

    # Main Game Loop
    while number_of_tries <= max_tries and guess_word != secret_word:
        print(f'=== Turn {number_of_tries}/{max_tries} ===')
        guess_word = input_guess(len(secret_word))
        print(emojified(guess_word, secret_word))
        number_of_tries = number_of_tries + 1
    
    if guess_word == secret_word: # If player guesses secret word correctly
        print(f'You won in {number_of_tries - 1}/{max_tries} turns!')
    else: # If player guesses incorrect and runs out of turns
        print(f'X/{max_tries} - Sorry, try again tomorrow!')
if __name__ == "__main__":
    main()