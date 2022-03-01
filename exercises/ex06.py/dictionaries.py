"""EX06: Dictionary Functions."""


def invert(x:dict[str, str]) -> dict[str, str]:
    """Swaps Key and Values."""
    first_string: str = ""
    second_string: str = ""
    regular: dict[str, str] = {first_string: second_string}
    inverted: dict[str,str] = {second_string: first_string}
    i: int = 0
    while i < len(regular):
        first_string = second_string
        second_string = first_string
        inverted[second_string] = first_string
        i = i + 1
    return inverted


def favorite_colors(x: dict[str,str]) -> str:
    favorite_colors_holder: str = ""
    return favorite_colors_holder

def count(x: list[str]) -> dict[str, int]:
    result_dictionary: dict[str, int] = {}
    i: int = 0
    while i < len(x):
        if x[i] in x == True:
            result_dictionary[x[i]]+= 1 
            i += 1
        elif x[i] in x == False:
            result_dictionary[x[i]] = 1
            i += 1
        
    return result_dictionary

