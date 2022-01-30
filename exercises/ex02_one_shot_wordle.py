
"""One Shot Wordle"""
__author__ = 730477179

from cgi import test


SECRET: str = "python"
six_letter_guess: str = input("What is your 6-letter guess?")

if six_letter_guess == SECRET:
    print ("Woo!You got it!")
else:
    print("Not quite. Play again soon!")

while len(six_letter_guess) != len(SECRET):
    new_input: str = input( "That was not 6 letters! Try again:") 


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX:str = "\U0001F7E8"

i: int = 0
emoji_storage: str = ""

while i < len(SECRET):
    if six_letter_guess[i] == SECRET[i]:
        print(GREEN_BOX)
        i= i+ 1
    else: 
        print(WHITE_BOX)
        i = i+ 1
    
Guessing: bool = False
idx: int = 0
Guessing == False
while Guessing and idx < len(SECRET): 
    if SECRET[i] != six_letter_guess[idx]:
        print(YELLOW_BOX)
    else:
        idx = idx + 1




