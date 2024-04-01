from random import randint
MAX_VAL: int = 10 ** 5
MIN_VAL: int = -10 ** 5

def random_descending_list(n: int) -> list[int]:
    """Generate a list of random descending integers."""
    new_list: list[int] = []
    idx: int = 0
    new_list.append(randint(MIN_VAL, MAX_VAL))
    while len(new_list) < n:
        new_list.append(randint(MIN_VAL, new_list[idx]))
        idx += 1
    return new_list