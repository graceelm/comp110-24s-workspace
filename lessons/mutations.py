"""Practice with mutable objects."""

def remove_first(my_list: list[str]):
    my_list.pop(0)


def get_first(my_list: list[str]):
    return my_list[0]


def get_and_remove_first(my_list: list[str]):
    first_elem: str = my_list[0]
    my_list.pop(0)
    return first_elem