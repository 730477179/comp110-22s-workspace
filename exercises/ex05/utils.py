"""EX05: Function and Test Practice."""


def only_evens(a: list[int]) -> list[int]: 
    """Find the even values in a list."""
    i: int = 0
    even_values: list[int] = list()
    while i < len(a):
        if a[i] % 2 == 0:
            even_values.append(a[i])
            i = i + 1
        else:
            i = i + 1
    print(even_values)
    return even_values


def sub(a: list[int], b: int, c: int) -> list[int]:
    """Give the values of list at range of index."""
    new_list_for_sub: list[int] = []
    i: int = 0
    if len(a) == 0 or b > len(a) or c <= 0:
        return new_list_for_sub
    if b < 0:
        b = 0
    if c > len(a):
        c = len(a)
    i = b
    while i < c:
        new_list_for_sub.append(a[i])
        i = i + 1
    return new_list_for_sub


def concat(a: list[int], b: list[int]) -> list[int]:
    """Combines two lists of integers."""
    all_values: list[int] = a + b
    return all_values