"""EX02 - One Shot Wordle - Real Thing"""

__author__ = "730508421"

#Establishing Secret Word
secret_word = "python"

guess: str = str(input("What is your 6-letter guess? "))

#Named Constants
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

#Response to Player Input
while guess != secret_word:
    if len(guess) < len(secret_word):
        guess: str = str(input(f"That was not 6 letters! Try again: "))
    
    #Checking Indices for Correct Matches
    if len(guess) == len(secret_word):  
    #Establishing Variables for check
        guess_idx = 0
        result = str(f"")
        while guess_idx < len(secret_word):
            guess_check = guess[guess_idx]
            secret_word_check = secret_word[guess_idx]
            
            if guess_check == secret_word_check:
                  result = result + GREEN_BOX
            else:
                 result = result + WHITE_BOX
            guess_idx = guess_idx + 1
        
        print(f"Not quite. Play again soon!")
        print(result)
        exit ()

#Guess equals Secret Word
if guess == secret_word:
        print (f"Woo! You got it! ")
        print (f"{GREEN_BOX}{GREEN_BOX}{GREEN_BOX}{GREEN_BOX}{GREEN_BOX}{GREEN_BOX}")