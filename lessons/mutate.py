"""Mutating Functions."""

__author__ = "730654117"


def manual_append(a: list[int], b: int) -> None:
    """Append list."""
    a.append(b)


def double(a: list[int]) -> None:
    """Double all values in list."""
    list_idx: int = 0
    while list_idx < len(a):
        a[list_idx] *= 2
        list_idx += 1