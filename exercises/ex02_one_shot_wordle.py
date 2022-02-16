"""One Shot Wordle."""

__author__ = "730477179"

SECRET: str = "python"
six_letter_guess: str = input(f"What is your {len(SECRET)}-letter guess? ")


while len(six_letter_guess) != len(SECRET):
    six_letter_guess = input(f"That was not {len(SECRET)} letters! Try again: ") 

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0
emoji_storage: str = ""


while i < len(SECRET):
    Guessing: bool = False
    idx: int = 0
    if six_letter_guess[i] == SECRET[i]: 
        emoji_storage = emoji_storage + GREEN_BOX         
    else: 
        while Guessing is False and idx < len(six_letter_guess):
            if SECRET[idx] == six_letter_guess[i]:
                Guessing = True
            else: 
                idx = idx + 1    
        if Guessing is True:
            emoji_storage = emoji_storage + YELLOW_BOX 
        else:
            emoji_storage = emoji_storage + WHITE_BOX                         
    i = i + 1           
print(emoji_storage)

if six_letter_guess == SECRET:
    print("Woo!You got it!")
else:
    print("Not quite. Play again soon!")