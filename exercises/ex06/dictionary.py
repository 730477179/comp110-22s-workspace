"""EX06: Dictionary Functions."""
__author__ = "730477179."


def invert(x: dict[str, str]) -> dict[str, str]:
    """Swaps Key and Values."""
    inverted: dict[str, str] = {}
    for key in x:
        inverted[x[key]] = key
    return inverted


def count(x: list[str]) -> dict[str, int]:
    """Counts occurences of strings."""
    result_dictionary: dict[str, int] = {}
    i: int = 0
    while i < len(x):
        if x[i] in result_dictionary:
            result_dictionary[x[i]] += 1 
        else: 
            result_dictionary[x[i]] = 1
        i += 1
        
    return result_dictionary


def favorite_color(x: dict[str, str]) -> str:
    """Returns String of Favorite Color."""
    favorite_colors_holder: list[str] = []
    string_for_answer: str = ""
    for key in x:
        favorite_colors_holder.append(x[key])
    counted_dictionary: dict[str, int] = count(favorite_colors_holder)
    max: int = 0 
    for key in counted_dictionary:
        if counted_dictionary[key] > max:
            max = counted_dictionary[key]
            string_for_answer = key
          
    return string_for_answer