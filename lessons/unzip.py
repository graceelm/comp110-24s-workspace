"""Splitting a dictionary into two lists."""

__author__ = "730654117"


def get_keys(my_dict: dict[str, int]) -> list[str]:
    """Returns a list of keys in dictionary."""
    my_list: list[str] = list()
    for key in my_dict:
        my_list.append(key)
    return my_list


def get_values(input: dict[str, int]) -> list[int]:
    """Returns a list of values in dictionary."""
    list1: list[int] = list()
    for item in input:
        list1.append(input[item])
    return list1