"""EX02 - One Shot Wordle - Real Thing."""

__author__ = "730508421"

# Establishing Secret Word
secret_word = "python"
guess: str = str(input("What is your 6-letter guess? "))

# Named Constants
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Response to Player Input
while len(guess) < len(secret_word) or len(guess) > len(secret_word):
    guess = str(input("That was not 6 letters! Try again: "))
    
    # Checking Indices for Correct Matches
if len(guess) == len(secret_word) and guess != secret_word:
    # Establishing Variables for Check
    guess_idx = 0
    result = str("")
    # Establishing the Check Loop
    while guess_idx < len(secret_word) or guess_idx > len(secret_word):
        guess_check = guess[guess_idx]
        secret_word_check = secret_word[guess_idx]
        # Boolean variable to keep track of whether the guessed character exists anywhere else in the word 
        guessed_char_exists = False
        # Variable to keep track of the alternate indices of the secret word you are checking for a match
        alternate_idx = 0
            
        # Loop to check of guessed character is in secret word
        while not guessed_char_exists and alternate_idx < len(secret_word):
            if alternate_idx != guess_idx and secret_word[alternate_idx] == guess_check:
                guessed_char_exists = True
            else:
                alternate_idx = alternate_idx + 1

            # If boolean is true (guessed character is somewhere in secret word), print yellow box
            if guessed_char_exists:
                result = result + YELLOW_BOX
            elif guess_check == secret_word_check: 
                result = result + GREEN_BOX   # If guessed character is same place in secret word, print green box
            else:
                result = result + WHITE_BOX   # If guessed character is not on secret word, print white box
            guess_idx = guess_idx + 1
        
        print("Not quite. Play again soon!")
        print(result)
        exit()

# Guess equals Secret Word
if guess == secret_word:
    print("Woo! You got it! ")
    print(f'{GREEN_BOX * len(secret_word)}')