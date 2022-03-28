"""Dictionary related utility functions."""

__author__ = "730477179"
from csv import DictReader
from unittest import result

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

def head(data_cols_head: dict[str, list[str]], y: int) -> dict[str, list[str]]:
    head_dict: dict[str, list[str]] = {}
    if y > len(data_cols_head): 
        y = len(data_cols_head)
    for column in data_cols_head:
        head_list: list[str] = []
        i: int = 0
        while i <= y:
            head_list.append(data_cols_head[column][i])
            i += 1
        head_dict[column] = head_list
 
    return head_dict

# data: dict[str, list[str]] = {'letters': ['a','b','c','d'], 'numbers': ['1','2','3','4']}
# print(head(data, 3))

def select(x: dict[str, list[str]], y: list[str]) -> dict[str, list[str]]:
    new_dict: dict[str, list[str]] = {}
    for key in y:
        new_dict[key] = y 
    return new_dict 


def concat(first: dict[str, list[str]], second: dict[str, list[str]]) -> dict[str, list[str]]:
    concat_dict: dict[str, list[str]] = {}
    for column in first:
        concat_dict[column] = first[column]
    for column in second:
        if second[column] == concat_dict[column]:
            concat_dict[column] = first[column] + second[column]
        elif second[column] != concat_dict[column]:
            concat_dict[column] = second[column]
    return concat_dict

def count(x: list[str]) -> dict[str, int]:
    dict_holder: dict[str, int] = {}
    i: int = 0
    while i < len(x):
        for x[i] in x:
            if  x[i] in dict_holder:
                dict_holder[x[i]] += dict_holder[x[i]]
            elif x[i] not in dict_holder:
               dict_holder[x[i]] = 1
        i += 1      
    return dict_holder