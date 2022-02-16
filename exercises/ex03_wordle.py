"""Structured Wordle."""

__author__ = "730477179"

i = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
SECRET: str = "smilers"


def contains_char(user_input: str, single_character: str) -> bool:
    """Searching for a single letter."""
    i = 0
    assert len(single_character) == 1
    while i < len(user_input):
        if single_character == user_input[i]:
            i = i + 1
            return True 
        else:
            i = i + 1
    return False


def emojified(Guess: str, SECRET: str) -> str:
    """Printing the correct color boxes."""
    emoji_storage: str = ""

    """Codifying the emoji boxes"""
    assert len(Guess) == len(SECRET)

    i = 0
    while i < len(SECRET):
        if contains_char(SECRET, Guess[i]) is True and SECRET[i] == Guess[i]:
            emoji_storage = emoji_storage + GREEN_BOX
        else: 
            if contains_char(SECRET, Guess[i]) is True and SECRET[i] != Guess[i]:
                emoji_storage = emoji_storage + YELLOW_BOX
            else: 
                if contains_char(SECRET, Guess[i]) is False:
                    emoji_storage = emoji_storage + WHITE_BOX
        i = i + 1 
    return emoji_storage


def input_guess(expected_length: int) -> str:
    """Ensuring guess is expected length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars word! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    SECRET: str = "codes"
    turns: int = 0
    success: bool = False
    while turns < 6 and success is False:
        turns = turns + 1
        print(f"=== Turn {turns}/6 === ")
        user_word = input_guess(len(SECRET))
        print(emojified(user_word, SECRET))
        if user_word == SECRET:
            return print(f"You won in {turns}/6!")   
    if success is False: 
        return print("X/6 - Sorry, try again tomorrow!")

        
if __name__ == "__main__":
    main()   