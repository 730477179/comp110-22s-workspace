"""One Shot Wordle."""

__author__ = "730477179"

SECRET: str = "python"
six_letter_guess: str = input("What is your 6-letter guess?")

while len(six_letter_guess) != len(SECRET):
    new_input: str = input("That was not 6 letters! Try again: ") 

if six_letter_guess == SECRET:
    print ( "Woo!You got it!")
else:
    print("Not quite. Play again soon!")




WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0
emoji_storage: str = ""
Guessing: bool = False
idx: int = 0

while Guessing and idx < len(six_letter_guess): 
    if SECRET[idx] == six_letter_guess[i]:
        Guessing = True
        emoji_storage = emoji_storage + GREEN_BOX
        idx = idx + 1
        
    else: 
        emoji_storage = emoji_storage + YELLOW_BOX

while i < len(SECRET):
    if six_letter_guess[i] == SECRET[i]:
        i= i + 1
        emoji_storage = emoji_storage + GREEN_BOX       
    else: 
        emoji_storage = emoji_storage + WHITE_BOX
        i = i + 1
               
print(emoji_storage)