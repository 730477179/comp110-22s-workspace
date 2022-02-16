"""An example of for in syntax."""

names: list[str] = ["Lily", "Pakiza", "Lauren"]

# Example of Iterating through names using a while loop

i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

# For in loop that performs same thing as while loop above
for name in names:
    print(name)