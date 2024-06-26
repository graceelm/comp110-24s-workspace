"""EX05- Dictionary Functions."""

__author__ = "730654117"


def invert(dict_input: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values in a list."""
    inverted_dict = {}
    for key in dict_input:
        if dict_input[key] in inverted_dict:
            raise KeyError("Keys cannot repeat!")
        else:
            inverted_dict[dict_input[key]] = key
    return inverted_dict


def favorite_color(colors: dict[str, str]) -> str:
    """Returns the color that appears most frequently."""
    appearances: dict[str, int] = {}
    for key in colors:
        if colors[key] in appearances:
            appearances[colors[key]] += 1
        else:
            appearances[colors[key]] = 1
        favorite: str = colors[key]
    for elem in appearances:
        if appearances[elem] > appearances[favorite]:
            appearances[elem] = favorite
    return favorite


def count(list_input: list[str]) -> dict[str, int]:
    """Counts the appearances of values in a list."""
    new_dict: dict[str, int] = {}
    for elem in list_input:
        if elem not in new_dict:
            new_dict[elem] = 1
        else:
            new_dict[elem] += 1
    return new_dict


def alphabetizer(uncategorized_list: list[str]) -> dict[str, list[str]]:
    """Categorizes words by their first letter."""
    categorized_dict: dict[str, list[str]] = {}
    for elem in uncategorized_list:
        if (elem[0].lower()) not in categorized_dict:
            categorized_dict[(elem[0].lower())] = [elem]
        else:
            categorized_dict[(elem[0].lower())] += [elem]
    return categorized_dict


def update_attendance(attendance_dict: dict[str, list[str]], day: str, student: str) -> None:
    """Update the dictionary with new attendance information."""
    if day in attendance_dict:
        if student not in attendance_dict[day]:
            attendance_dict[day].append(student)
    else:
        attendance_dict[day] = []
        attendance_dict[day].append(student)