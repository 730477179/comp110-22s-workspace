"""Union type gives flexibility to single variables."""

from typing import Union


def log(info: Union[str, int]) -> None:
    """Info can be str or int!"""
    if is instance(info, str):
        print(f"str: {info}")
    else:
        print(f"int: {info}")

    
log("hello")
log(110)

# We can have have a single parameter and pass multiple types to it.
