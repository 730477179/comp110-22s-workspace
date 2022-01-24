"""EX01- Chardle - A cute step toward Wordle."""

__author__ = "730477179"

five_letter_word: str = input("Enter a 5 character word:")
if len(five_letter_word) < 5:
    print("Error: Word must contain 5 characters")
    quit()
if len(five_letter_word) > 5:
    print("Error: Word must contain 5 characters")
    quit()

one_letter_input: str = input("Enter a single character:")
if len(one_letter_input) > 1:
    print("Error: Character must be a single character.")
    quit()
if len(one_letter_input) < 1:
    print("Error: Character must be a single character.")
    quit()

matching_character: int = 0

print("searching for "+ one_letter_input +" in "+ five_letter_word)

if (five_letter_word[0] == one_letter_input):
    print(one_letter_input + " found at index 0")
    matching_character = matching_character + 1 
else:
    matching_character = matching_character

if (five_letter_word[1] == one_letter_input):
    print(one_letter_input + " found at index 1")
    matching_character = matching_character + 1 
else:
    matching_character = matching_character
if(five_letter_word[2] == one_letter_input):
    print(one_letter_input + " found at index 2")
    matching_character = matching_character + 1 
else:
    matching_character = matching_character
if(five_letter_word[3] == one_letter_input):
    print(one_letter_input + " found at index 3")
    matching_character = matching_character + 1 
else:
    matching_character = matching_character
if(five_letter_word[4] == one_letter_input):
    print(one_letter_input + " found at index 4")
    matching_character = matching_character + 1 
else:
    matching_character = matching_character


if (matching_character == 0):
    print("No instances of " + one_letter_input + " found in " + five_letter_word)
else:
    if (matching_character == 1):
        print("1 instance of "+ one_letter_input + " found in " + five_letter_word)
    if(matching_character == 2):
        print("2 instances of " + one_letter_input + " found in " + five_letter_word)
    if(matching_character == 3):
        print("3 instances of " + one_letter_input + " found in " + five_letter_word)
    if(matching_character == 4):
        print("4 instances of "+ one_letter_input + " found in " + five_letter_word)
    if(matching_character == 5):
        print("5 instances of " + one_letter_input + " found in " + five_letter_word)