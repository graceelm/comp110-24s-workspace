"""EX04 - List Utility Functions."""

__author__ = "730654117"


def all(list1: list[int], num1: int) -> bool:
    """Returns whether all list values are the same as a given integer."""
    list_idx: int = 0
    while list_idx < len(list1):
        if list1[list_idx] == num1:
            list_idx += 1
        else:
            return False
    return True


def max(input: list[int]) -> int:
    """Returns largest value in list."""
    # raise value error if input is empty
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        input_idx: int = 0
        max_num: int = (input[0])
        while input_idx < len(input):
            if input[input_idx] > max_num:
                max_num = input[input_idx]
                input_idx += 1
            else:
                input_idx += 1
        return max_num


def is_equal(my_list1: list[int], my_list2: list[int]) -> bool:
    """Returns whether all values are equal in both lists."""
    idx_1: int = 0
    idx_2: int = 0
    while idx_1 < len(my_list1) and idx_2 < len(my_list2):
        if my_list1[idx_1] == my_list2[idx_2]:
            idx_1 += 1
            idx_2 += 1
        else:
            return False
    return True


def extend(input1: list[int], input2: list[int]) -> None:
    """Append second list to first list."""
    idx: int = 0
    while idx < len(input2):
        input1.append(input2[idx])
        idx += 1