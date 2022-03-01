""" Hype Machine."""

from tkinter import LEFT
from turtle import left


name: str = input("What is your name? ")

hype_1: str = (f"You are killing it {name}")
hype_2: str =(f"{name}, you are so loved")
hype_3: str = (f"{name}, I think you're doing incredible.")
hype_4: str = (f"{name}, you are a baddie")
hype_5: str = (f"{name}, you are gorgeous")
hype_6: str = (f"{name}, you are going to kill this")

print(hype_1)
print(hype_2)
print(hype_3)
print(hype_4)
print(hype_5)
print(hype_6)

"""Numeric Operators."""
left_hand_side= int(input("Left-hand side:"))
right_hand_side = int(input("Right-hand side:"))

answer_1: int = (right_hand_side ** left_hand_side)
answer_2: float = (right_hand_side / left_hand_side)
answer_3: int = (right_hand_side // left_hand_side)
answer_4: int = (right_hand_side % left_hand_side)

print(f"{left_hand_side} ** {right_hand_side} is {answer_1}")
print(f"{left_hand_side} / {right_hand_side} is {answer_2}")
print(f"{left_hand_side} // {right_hand_side} is {answer_3}")
print(f"{left_hand_side} % {right_hand_side} is {answer_4}")

"""Relational Operators."""
left_hand_side = int(input("Right:"))
right_hand_side = int(input("Left:"))

answers_one: bool = left_hand_side < right_hand_side 
answers_two: bool = left_hand_side >= right_hand_side
answers_three: bool = left_hand_side == right_hand_side
answers_four: bool = left_hand_side != right_hand_side

print(f"{right_hand_side} < {left_hand_side} is {answers_one}")
print(f"{right_hand_side} >= {left_hand_side} is {answers_two}")
print(f"{right_hand_side} == {left_hand_side} is {answers_three}")
print(f"{right_hand_side} != {left_hand_side} is {answers_four}")