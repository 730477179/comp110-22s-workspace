"""Fortune Cookie."""
from random import randint

print("Your fortune cookie says...")

assigned_number: int = (randint(0,6)) 

if assigned_number == 0:
    print("You will meet the love of your life soon.")
elif assigned_number == 1:
    print("Something incredible will happen to you today.")
elif assigned_number == 2:
    print("You are doing well, keep going")
elif assigned_number == 3:
    print("You will becme great if you believe in yourself")
elif assigned_number == 4:
    print("You are very talented in many ways")
elif assigned_number == 5:
    print("When fear hurts you, conquer it and defeat it")
elif assigned_number == 6:
    print("It's amazing how much good you can do if you don't care who gets the credit")
elif assigned_number == 7:
    print("You will get A in Calc")

"""Repeat beat."""

beat: str = input("What beat do you want to repeat? ")
response: int
repetition: str = input(f"How many times do you want to repeat it? ")

i: int = 0
counter: int = 0
beat_storer: str = ""
spacer: str = " "
if int(repetition) < 0: 
    beat_storer = "No beat..."
while i != int(repetition):
    beat_storer = beat + spacer + beat_storer
    i = i + 1

print(beat_storer)

"""Count Letters."""
letter: str = input("What letter would you like to search for?:")
word: str = input("Enter a word:")

counter_variable: int = 0
encounters: int = 0
while counter_variable < len(word):
    if word[counter_variable] == letter:
        encounters = encounters + 1
        counter_variable = counter_variable+ 1
    else:
        encounter = encounters
        counter_variable = counter_variable + 1

print(f"Count: {encounters}")
