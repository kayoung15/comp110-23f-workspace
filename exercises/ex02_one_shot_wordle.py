"""EX02 - One Shot Wordle - Real Thing."""

__author__ = "730508421"

"""Establishing Secret Word and Named Constants"""
secret_word = "python"
guess: str = str(input("What is your 6-letter guess? "))
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

"""Response to Player Input"""
while guess != secret_word:
    if len(guess) < len(secret_word) or len(guess) > len(secret_word):
        guess: str = str(input(f"That was not 6 letters! Try again: "))
    
    if len(guess) == len(secret_word) and guess == secret_word:
    
        guess_idx = 0
        result = str(f"")

    while guess_idx < len(secret_word):
        guess_check = guess[guess_idx]
        secret_word_check = secret_word[guess_idx]
        guessed_char_exists = False
        alternate_idx = 0

    while not guessed_char_exists and alternate_idx < len(secret_word):
        if alternate_idx != guess_idx and secret_word[alternate_idx] == guess_check:
            guessed_char_exists = True
        else:
            alternate_idx = alternate_idx + 1

        if guessed_char_exists:
            result = result + YELLOW_BOX
        elif guess_check == secret_word_check: 
            result = result + GREEN_BOX 
        else:
            result = result + WHITE_BOX 
            guess_idx = guess_idx + 1
        
        print(f"Not quite. Play again soon!")
        print(result)
        exit ()

if guess == secret_word:
    print (f"Woo! You got it! ")
    print (f"{GREEN_BOX * len(secret_word)}")
