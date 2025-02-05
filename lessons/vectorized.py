from __future__ import annotations
from typing import Union
# allows us to accept two different types at one parameter


class StrArray:
    items: list[str]

    def __init__(self, items): 
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"
    
    def __add__ (self, rhs: Union[str, StrArray]) -> StrArray:
        """Add is a vectorized operation that applies to all items. When rhs is a str, it is concatenated to every item in a new StrArray."""
        """When rhs is a str, it is concatenated to every item in a new StrArray."""
        if isinstance(rhs, str):
            result: list[str] = []
            for item in self.items:
                result.append(item + rhs)
            return StrArray(result)
        else:
            result: list[str] = []
            for i in range (0, len(self.items)):
                result.append(self.items[i] + rhs.items[i])
            return StrArray([result])




        # Establish a result list of strings that is empty
        # Loop through every item in self.items
        # Append the concatenation off items with rhs to your result list
        # After loop, return a new StrArray object constructed with result list

        results: list[str] = []
        for item in self.items:
        # you have to use self.items to specify that it's from self
            results.append(item + rhs)
        # you could have also done result.items.append(item + rhs) if not using a magic method
        # After loop, return a new StrArray object constructed with result list
        return StrArray(results)

first: StrArray = StrArray(["Armando", "Brady", "Caleb"])
last: StrArray = StrArray(["Bacot", "Manek", "Love"]) 
print(first + "!")
print(first)
print(first + last)

