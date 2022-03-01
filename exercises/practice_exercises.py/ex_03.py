"""Third set of practicing writing code."""

"""Tar Heel Arithmetic."""
user_number: str = input("Enter an int: ")

if int(user_number) % 2 == 0  and int(user_number) % 7 == 0:
    print("TAR HEELS")
elif int(user_number) % 2 == 0:
    print("TAR")
elif int(user_number) % 7 == 0:
    print("HEELS")
else:
    print("CAROLINA")
