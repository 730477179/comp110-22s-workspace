"""Tests for Excercise 5."""


from utils import only_evens, sub, concat


def test_sub_one() -> None:
    """Tests function when given empty list."""
    a: list[int] = [2, 3, 4, 5, 6]
    assert sub(a, 7, 5) == []


def test_sub_two() -> None:
    """Tests function when c is greater than number of indices."""
    sub_test_two: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(sub_test_two, 2, 7) == [3, 4, 5, 6]


def test_sub_three() -> None:
    """Tests function when start index is less than 0."""
    sub_test_three: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(sub_test_three, -1, 3) == [1, 2, 3]


def test_only_evens_one() -> None:
    """Tests function with a regular list of values."""
    evens: list[int] = [2, 3, 4, 5, 6]
    assert only_evens(evens) == [2, 4, 6]


def test_only_evens_two() -> None:
    """Tests function when given empty list."""
    second_test_for_evens: list[int] = []
    assert only_evens(second_test_for_evens) == []


def test_only_evens_three() -> None:
    """Test function with all odd values."""
    third_test_for_evens: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(third_test_for_evens) == []


def test_concat_one() -> None:
    """Tests regular function with regular lists."""
    a: list[int] = [1, 2]
    b: list[int] = [3, 4]
    assert concat(a, b) == [1, 2, 3, 4]
 

def test_concat_two() -> None:
    """Tests function when given empty list."""
    list_one: list[int] = []
    list_two: list[int] = []
    assert concat(list_one, list_two) == []


def test_concat_three() -> None:
    """Tests function when given descending list."""
    first_list: list[int] = [6, 5, 4]
    second_list: list[int] = [3, 2, 1]
    assert concat(first_list, second_list) == [6, 5, 4, 3, 2, 1]