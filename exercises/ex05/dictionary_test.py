"""EX06- Testing Dictionary Functions."""

__author__ = "730654117"


from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_use() -> None:
    """Test basic use case for inverting keys and values."""
    t: dict[str, str] = {"April": "showers", "May": "flowers"} 
    assert invert(t) == {"showers": "April", "flowers": "May"}


def test_invert_use_1() -> None:
    """Test basic use case for inverting keys and values."""
    t: dict[str, str] = {"Monday": "sunny", "Tuesday": "rainy", "Wednesday": "cloudy"}
    assert invert(t) == {"sunny": "Monday", "rainy": "Tuesday", "cloudy": "Wednesday"}


def test_invert_edge() -> None:
    """Test edge case for when user inputs empty string."""
    t: dict[str, str] = {"Strawberry": "fruit", "Carrot": "vegetable", "Tomato": ""}
    assert invert(t) == {"fruit": "Strawberry", "vegetable": "Carrot", "": "Tomato"}


def test_favorite_color_use() -> None:
    """Test basic use case for returning color that appears most frequently."""
    t: dict[str, str] = {"Maya": "red", "Joey": "blue", "Tommy": "pink", "Emma": "blue"}
    assert favorite_color(t) == "blue"


def test_favorite_color_use_1() -> None:
    """Test use case for returning first color when all colors have equal values."""
    t: dict[str, str] = {"Evelyn": "yellow", "Elton": "blue", "Margaret": "green", "Earl": "red"}
    assert favorite_color(t) == "yellow"


def test_favorite_color_edge() -> None:
    """Test edge case for when multiple colors are reported for one name."""
    t: dict[str, str] = {"Harper": "green", "Finn": "yellow", "Daisy": "orange" and "green", "Sofia": "pink"}
    assert favorite_color(t) == "green"


def test_count_use() -> None:
    """Test basic use case for counting appearances of values in a list."""
    t: list[str] = ["green", "blue", "red", "blue"]
    assert count(t) == {"green": 1, "blue": 2, "red": 1}


def test_count_use_1() -> None:
    """Test basic use case for counting appearances of values in a list."""
    t: list[str] = ["Leo", "August", "Sam", "June", "Lena", "Leo", "August", "June", "Lena"]
    assert count(t) == {"Leo": 2, "August": 2, "Sam": 1, "June": 2, "Lena": 2}


def test_count_edge() -> None:
    """Test edge case for when user inputs empty string."""
    t: list[str] = [""]
    assert count(t) == {"": 1}


def test_alphabetizer_use() -> None:
    """Test basic use case for categorizing words by first letter."""
    t: list[str] = ["Animal", "Apple", "Book", "Banana", "Car", "Candle", "Dog", "Door"]
    assert alphabetizer(t) == {"a": ["Animal", "Apple"], "b": ["Book", "Banana"], "c": ["Car", "Candle"], "d": ["Dog", "Door"]}


def test_alphabetizer_use_1() -> None:
    """Test basic use case for categorizing words by their first letter."""
    t: list[str] = ["Bronte", "Hemmingway", "Wilde", "Austen", "Woolf", "Hugo"]
    assert alphabetizer(t) == {"b": ["Bronte"], "h": ["Hemmingway", "Hugo"], "w": ["Wilde", "Woolf"], "a": ["Austen"]}


def test_alphabetizer_edge() -> None:
    """Test edge case for when user inputs letters only."""
    t: list[str] = ["A", "B", "C", "D"]
    assert alphabetizer(t) == {"a": ["A"], "b": ["B"], "c": ["C"], "d": ["D"]}


def test_update_attendence_use() -> None:
    """Test basic use case for updating dict with new attendence information."""
    t: dict[str, list[str]] = {"Monday": ["Jordan", "Emma"], "Tuesday": ["Emma", "Grace"], "Wednesday": ["Jordan", "Emma"]}
    day: str = "Wednesday"
    student: str = "Grace"
    update_attendance(t, day, student)
    assert t == {"Monday": ["Jordan", "Emma"], "Tuesday": ["Emma", "Grace"], "Wednesday": ["Jordan", "Emma", "Grace"]}


def test_update_attendence_use_1() -> None:
    """Test basic use case for updating dict with new attendence information."""
    t: dict[str, list[str]] = {"Thursday": ["Sam", "Eric"], "Friday": ["Josh", "Sam"]}
    day: str = "Friday"
    student: str = "Eric"
    update_attendance(t, day, student)
    assert t == {"Thursday": ["Sam", "Eric"], "Friday": ["Josh", "Sam", "Eric"]}


def test_update_attendence_edge() -> None:
    """Test edge case for when adding a repeated name."""
    t: dict[str, list[str]] = {"Monday": ["Alex", "Sadie", "Alyssa"], "Tuesday": ["Alex", "Sadie", "Alyssa", "Grace"]}
    day: str = "Monday"
    student: str = "Alex"
    update_attendance(t, day, student)
    assert t == {"Monday": ["Alex", "Sadie", "Alyssa"], "Tuesday": ["Alex", "Sadie", "Alyssa", "Grace"]}