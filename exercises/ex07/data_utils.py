"""Dictionary related utility functions."""

__author__ = "730477179"
from csv import DictReader

# Define your functions below

def read_csv_rows(filename: str) -> list[dict[str,str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str,str]] = []

    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()
    return result

def column_values(table: list[dict[str,str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result

def columnar(row_table: list[dict[str,str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result

def head(x: dict[str, list[str]], y: int) -> dict[str, list[str]]:
    head_dict: dict = {}

    return head_dict




def select(x: dict[str, list[str]], y: list[str]) -> dict[str, list[str]]:
    new_dict: dict[str, list[str]] = {}
    for key in y:
        new_dict[key] = y 
    return new_dict 












    return 

def count(x: list[str]) -> dict[str, int]:
    dictionary_holder: dict = {}


    return 