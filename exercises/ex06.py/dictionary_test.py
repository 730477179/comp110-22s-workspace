"""Test for our dictionary functions"""
__author__ = """730477179."""

from dictionaries import invert, count, favorite_colors 


def test_invert_one() -> None:
    """Testing Invert with two Key-Value Pairs."""
    invert_one: dict[str, str] = {"hello":"kitty", "kit":"kat"}
    assert invert(invert_one) == {"kitty":"hello", "kat": "kit"}


def test_invert_two() -> None:
    """Testing Invert with one Key- Value Pairs. """
    invert_two: dict[str, str] = {"sun":"rise", "bed": "time", "baby":"girl"}
    assert invert(invert_two) == {"rise":"sun", "time":"bed", "girl": "baby"}

def test_invert_three() -> None:
    """Edge Case"""


def test_count_one() -> None:
    """ Edge case: Testing a Three- way tie"""


def test_count_two() -> None:
    """ Use Case: """
    count_two: list[str] = ["blue", "blue", "red", "yellow"]
    assert count(count_two) == {"blue": 2, "red": 1, "yellow": 1 }


def test_count_three() -> None:
    """Another Use Case."""
    count_three: list[str] = ["blue", "blue", "blue", "blue"]
    assert count(count_three) == {"blue" : 4}


def test_favorite_colors_one() -> None:
    """Use Case 1."""
    favorite_colors_one: dict[str,str] = {"Lily": "Blue", "Margaret":"Red", "Mary": "Blue"}
    assert favorite_colors(favorite_colors_one) == "blue"


def test_favorite_colors_two() -> None:
    """Use Case 2."""
    favorite_colors_two: dict[str,str] = {"Lily" : "Purple", "Anna": "Green", "Helen": "Green"}
    assert favorite_colors(favorite_colors_two) == "Green"

def test_favorirte_colors_three() -> None:
    """Edge Case."""
