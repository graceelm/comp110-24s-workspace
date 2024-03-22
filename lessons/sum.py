"""Summing the elements of a list using different loops!"""

__author__ = "730654117"


def w_sum(vals: list[float]) -> float:
    """Returns sum of all values in list using while loop."""
    w_idx: int = 0
    total: float = 0.0
    while w_idx < len(vals):
        total += vals[w_idx]
        w_idx += 1
    return total


def f_sum(vals: list[float]) -> float:
    """Returns sum of all values in list using for loop."""
    total: float = 0.0
    for num in vals:
        total += num
    return total


def f_range_sum(vals: list[float]) -> float:
    """Returns sum of all values in list using range."""
    total: float = 0.0
    for num in range(0, len(vals)):
        total = total + vals[num]
    return total