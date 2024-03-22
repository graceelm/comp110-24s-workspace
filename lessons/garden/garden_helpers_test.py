"""Test my garden functions."""

__author__ = "730654117"


from lessons.garden.garden_helpers import add_by_kind
from lessons.garden.garden_helpers import add_by_date
from lessons.garden.garden_helpers import lookup_by_kind_and_date


def test_add_by_kind_use() -> None:
    """Use case - should add new flower to flowers category."""
    test: dict[str, list[str]] = {"flower": ["daisy", "peony"], "vegetable": ["carrot", "lettuce"]}
    kind_test: str = "flower"
    plant_test: str = "zinnia"
    assert add_by_kind(test, kind_test, plant_test) == {"flower": ["daisy", "peony", "zinnia"], "vegetable": ["carrot", "lettuce"]}


def test_add_by_kind_edge() -> None:
    """Edge case - duplicate of flower."""
    test: dict[str, list[str]] = {"flower": ["daisy", "peony"], "vegetable": ["carrot", "lettuce"]}
    kind_test: str = "flower"
    plant_test: str = "daisy"
    assert add_by_kind(test, kind_test, plant_test) == {"flower": ["daisy", "peony", "zinnia"], "vegetable": ["carrot", "lettuce"]}


def test_add_by_date_use() -> None:
    """Use case - should add new plant in correct month."""
    test: dict[str, list[str]] = {"May": ["strawberry"], "June": ["tomato"]}
    date_test: str = "May"
    plant_test: str = "lettuce"
    assert add_by_date(test, date_test, plant_test) == {"May": ["strawberry", "lettuce"], "June": ["tomato"]}


def test_add_by_date_edge() -> None:
    """Edge case - empty string for plant argument."""
    test: dict[str, list[str]] = {"May": ["strawberry"], "June": ["tomato"]}
    date_test: str = "May"
    plant_test: str = ""
    assert add_by_date(test, date_test, plant_test) == {"May": ["strawberry", "lettuce", ""], "June": ["tomato"]}

    
def test_lookup_by_kind_and_date_use() -> None:
    """Use case - should locate plant by kind and date."""
    test_by_kind: dict[str, list[str]] = {"flower": ["daisy", "peony"], "vegetable": ["carrot", "tomato"]}
    test_by_date: dict[str, list[str]] = {"May": ["strawberry"], "June": ["tomato"]}
    test_kind: str = "vegetable"
    test_date: str = "June"
    assert lookup_by_kind_and_date(test_by_kind, test_by_date, test_kind, test_date) == "vegetables to plant in June: ['tomato']"


def test_lookup_by_kind_and_date_edge() -> None:
    """Edge case - month input is not in dictionary."""
    test_by_kind: dict[str, list[str]] = {"flower": ["daisy", "peony"], "vegetable": ["carrot", "tomato"]}
    test_by_date: dict[str, list[str]] = {"May": ["strawberry"], "June": ["tomato"]}
    test_kind: str = "vegetable"
    test_date: str = "March"
    assert lookup_by_kind_and_date(test_by_kind, test_by_date, test_kind, test_date) == "vegetables to plant in March: ['']"