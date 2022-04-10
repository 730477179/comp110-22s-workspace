"""Dictionary related utility functions."""

__author__ = "730477179"
from ast import Return
from calendar import c
from csv import DictReader
from urllib.request import HTTPDefaultErrorHandler

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    result: list[dict[str, str]] = []
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(data_cols_head: dict[str, list[str]], y: int) -> dict[str, list[str]]:
    """Produce a column based table given N."""
    head_dict: dict[str, list[str]] = {}
    if y > len(data_cols_head): 
        y = len(data_cols_head)
    for column in data_cols_head:
        head_list: list[str] = []
        i: int = 0
        while i < y:
            head_list.append(data_cols_head[column][i])
            i += 1
        head_dict[column] = head_list
 
    return head_dict


def select(x: dict[str, list[str]], y: list[str]) -> dict[str, list[str]]:
    """Produce a new column based table from a data subset."""
    new_dict: dict[str, list[str]] = {}
    for key in y:
        new_dict[key] = x[key]
    return new_dict 


def concat(first: dict[str, list[str]], second: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine two column-based tables."""
    concat_dict: dict[str, list[str]] = {}
    for column in first:
        concat_dict[column] = first[column]
    for column in second:
        if column in concat_dict:
            concat_dict[column] += second[column]
        else: 
            concat_dict[column] = second[column]
    return concat_dict


def count(x: list[str]) -> dict[str, int]:
    """Count the indices of occurences."""
    dict_holder: dict[str, int] = {}
    i: int = 0
    while i < len(x):
        if x[i] in dict_holder:
            dict_holder[x[i]] += 1
        else: 
            dict_holder[x[i]] = 1
        i += 1      
    return dict_holder

def responses(x: dict[str, int]) -> int:
    responses: int = 0
    for key in x:
        responses += x[key]
    return responses


def average(x: dict[str, int]) -> float:
    division: int = responses(x)
    avg_holder: float = 0.0
    for key in x:
        avg_holder += x[key]
    avg_holder: float = avg_holder/division
    return avg_holder
    


    