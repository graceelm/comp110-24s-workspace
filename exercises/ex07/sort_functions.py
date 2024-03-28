"""Functions that implement sorting algorithms."""

__author__ = "730654117"

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm. Insert into an already sorted list."""
    sorted: int = 0
    n: int = len(x)
    for unsorted in range(1, n):
        # Compare numbers and swap
        num = x[unsorted]
        while sorted >= 0 and x[sorted] > num:
            x[sorted + 1] = x[sorted]
            sorted -= 1
        x[sorted + 1] = num
        sorted = unsorted
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. Repeatedly find the minimum and swap it."""
    n = len(x)
    for i in range(n):
        # Find index of lowest of unsorted numbers
        min = i
        for num in range(i + 1, n):
            if x[num] < x[min]:
                min = num
        # Put minimum in correct order
        x[i], x[min] = x[min], x[i]
    return None